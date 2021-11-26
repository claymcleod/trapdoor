import os
import shutil
from . import configfile
from .utils import fs
from typing import Any, Dict, Optional


class Trapdoor:

    def __init__(
        self,
        store_name: str,
        store_directory: Optional[str] = None,
        config_filename: str = "config.toml",
        testing: bool = False
    ):
        """Trapdoor provides easy access to config files with 
        sane defaults. You can find more information on how to
        customize Trapdoor in the argument documentation below.
        Please see the associated method documentation for more
        information on what the Trapdoor class can do.

        :param store_name: Name of the store. Generally, this will be your
                           application's name. The author recommends you use
                           a short, snakecased moniker.
        :type store_name: str
        :param store_directory: If you'd like to set a particular directory to
                                store your configuration file in, you can set it with
                                this parameter. When not specified, the default
                                functionality is to create a dot folder in the user's
                                home directory with the store name (e.g., the directory
                                for a store name of `trapdoor` would be 
                                `~/.trapdoor/`).
        :type store_directory: Optional[str], optional
        :param config_filename: If you'd like to set a different filename for your config
                                file, you may do so here. Defaults to `config.toml`.
        :type config_filename: str
        :param testing: Parameter to enable testing, this should be False in almost every
                        case (unless you are writing tests for this library). 
                        Defaults to False.
        :type testing: bool, optional
        """
        self.store_name = store_name
        self.testing = testing

        if store_directory:
            self.store_directory = store_directory
        else:
            self.store_directory = os.path.join("~", "." + self.store_name)
        self._expand_store_directory()
        self._ensure_store_directory_exists()

        self.config_filepath = os.path.join(self.store_directory, config_filename)
        self.configfile = configfile.ConfigFile(self.config_filepath)

    def set(self, selector: str, value: str) -> Dict:
        """This method does the following actions:
        
            (1) Sets a key using the defined `selector` to the specified `value`.
            (2) Syncs the value with the store on disk.
            (3) Updates the `UPDATED_AT` key to reflect the latest update time.

        :param selector: Key path to set the value for.
        :type selector: str
        :param value: Value to set.
        :type value: str
        :return: The new dictionary with the updated value.
        :rtype: Dict
        """
        result = self.configfile.set(selector, value)
        self.configfile.sync_updated_at()
        return result 

    def get(self, key: str) -> Optional[Any]:
        """This method does the following actions:
        
            (1) Reloads the store from disk.
            (2) Gets a key as defined by the `selector`.

        :param selector: Key to retrieve from the store.
        :type selector: str
        :return: Value from the store for the key. If that key does not exist,
                 then `None` is returned.
        :rtype: Optional[Any]
        """
        return self.configfile.get(key)

    def _expand_store_directory(self):
        """Expands the store directory by using `os.path.expanduser`.

        :raises ValueError: [description]
        """
        if not isinstance(self.store_directory, str):
            raise ValueError("`store_directory` is not a string!")
        self.store_directory = os.path.expanduser(self.store_directory)

    def _ensure_store_directory_exists(self):
        """Ensures that the store directory exists."""
        fs.ensure_directory_exists(self.store_directory) 

    def _cleanup(self):
        """If testing is enabled, clean up the store by removing the store directory.

        :raises ValueError: If `testing=True` is not provided, this is disallowed.
        """
        if not self.testing:
            raise ValueError("You must set `testing=True` to cleanup the directory!")

        shutil.rmtree(self.store_directory)

    def __repr__(self) -> str:
        return f"""(Store name: {self.store_name}, Store directory: {self.store_directory})"""