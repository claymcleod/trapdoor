import os
from typing import Any, Dict, Optional
from datetime import datetime

from .utils import selectors
import toml

CREATED_AT_KEY = "meta.created-at"
UPDATED_AT_KEY = "meta.updated-at"

class ConfigFile:

    def __init__(self, 
        filepath: str,
        selector_split_character: str = "."
    ):
        """Wraps most of the functionality provided by Trapdoor. Simply put, this
        represents a single configuration file and provides the utilities to set
        and retrieve keys from the store.

        :param filepath: Path to the configuration file.
        :type filepath: str
        :param selector_split_character: Split character to use when splitting keys in
                                         a defined selector, defaults to "."
        :type selector_split_character: str, optional

        >>> import os, tempfile
        >>> tempdir = tempfile.mkdtemp()
        >>> store_path = os.path.join(tempdir, "store")
        >>> c = ConfigFile(store_path)
        >>> c.get('meta.updated-at')
        datetime...
        >>> c.get('meta.created-at')
        datetime...
        >>> c.set('hello.world.test', 'key')
        {'meta': {'created-at': ..., 'updated-at': ..., 'hello': {'world': {'test': 'key'}}}
        >>> c.get('hello.world.test')
        'key'
        """

        self.contents: Dict[Any, Any] = {}
        self.filepath = filepath
        self.selector = selectors.Selector(selector_split_character)

        if not os.path.exists(self.filepath):
            self._load_default_contents()
            self._dump_to_file()
        else:
            self._load_from_file()
    
    def set(self, selector: str, value: str) -> Dict:
        """Sets a key using the defined `selector` to the specified
        `value` and syncs the value with the store on disk.

        :param selector: Key path to set the value for.
        :type selector: str
        :param value: Value to set.
        :type value: str
        :return: The new dictionary with the updated value.
        :rtype: Dict
        """
        d = self.selector.update_from(selector, value, self.contents)
        self._dump_to_file()
        return d

    def get(self, selector: str) -> Optional[Any]:
        """Reloads the store from disk and gets a key 
        as defined by the `selector`.

        :param selector: Key to retrieve from the store.
        :type selector: str
        :return: Value from the store for the key. If that key does not exist,
                 then `None` is returned.
        :rtype: Optional[Any]
        """
        self._load_from_file()
        return self.selector.select(selector, self.contents)

    def sync_updated_at(self):
        """Updates the updated_at key in the store."""
        self.set(UPDATED_AT_KEY, datetime.now())
        self._dump_to_file()

    def _load_default_contents(self):
        """Loads some default contents into a new store."""
        now = datetime.now()
        self.set(CREATED_AT_KEY, now)
        self.set(UPDATED_AT_KEY, now)

    def _load_from_file(self):
        """Populates `self.contents` with what's currently stored in the
        configuration file."""
        with open(self.filepath, mode="r", encoding="utf-8") as f:
            self.contents = toml.load(f)

    def _dump_to_file(self):
        """Dumps `self.contents` into the configuration file."""
        with open(self.filepath, mode="w", encoding="utf-8") as f:
            toml.dump(self.contents, f)
