import os
import shutil
from . import configfile, fs
from typing import Optional


class Trapdoor:

    def __init__(
        self,
        store_name: str,
        store_directory: Optional[str] = None,
        config_filename: Optional[str] = None,
        testing: bool = False
    ):
        self.store_name = store_name
        self.testing = testing

        if store_directory:
            self.store_directory = store_directory
        else:
            self.store_directory = os.path.join("~", "." + self.store_name)
        self._expand_store_directory()
        self._ensure_directory_exists()

        if not config_filename:
            config_filename = "config.toml"

        self.config_filepath = os.path.join(self.store_directory, config_filename)
        self.configfile = configfile.ConfigFile(self.config_filepath)

    def set(self, key: str, value: str):
        self.configfile.set(key, value)
        self.configfile.sync_updated_at()

    def get(self, key: str):
        return self.configfile.get(key)

    def _expand_store_directory(self):
        if not isinstance(self.store_directory, str):
            raise ValueError("`store_directory` is not a string!")
        self.store_directory = os.path.expanduser(self.store_directory)

    def _ensure_directory_exists(self):
        fs.ensure_directory_exists(self.store_directory) 

    def _cleanup(self):
        if not self.testing:
            raise ValueError("You must set `testing=True` to cleanup the directory!")

        shutil.rmtree(self.store_directory)

    def __repr__(self) -> str:
        return f"""(Store name: {self.store_name}, Store directory: {self.store_directory})"""