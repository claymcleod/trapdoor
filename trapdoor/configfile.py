import os
from typing import Any, Dict

from . import selectors
from datetime import datetime

import toml

CREATED_AT_KEY = "meta.created-at"
UPDATED_AT_KEY = "meta.updated-at"

class ConfigFile:

    def __init__(self, 
        filepath: str,
        selector_split_character: str = "."
    ):
        self.contents: Dict[Any, Any] = {}
        self.filepath = filepath
        self.selector = selectors.Selector(selector_split_character)

        if not os.path.exists(self.filepath):
            self._load_default_contents()
            self._dump_to_file()
        else:
            self._load_from_file()
    
    def set(self, key: str, value: str):
        self.selector.update_from(key, value, self.contents)
        self._dump_to_file()

    def get(self, key: str):
        self._load_from_file()
        return self.selector.select(key, self.contents)

    def _load_default_contents(self):
        now = datetime.now()
        self.set(CREATED_AT_KEY, now)
        self.set(UPDATED_AT_KEY, now)

    def _load_from_file(self):
        with open(self.filepath, mode="r", encoding="utf-8") as f:
            self.contents = toml.load(f)

    def _dump_to_file(self):
        with open(self.filepath, mode="w", encoding="utf-8") as f:
            toml.dump(self.contents, f)

    def sync_updated_at(self):
        self.set(UPDATED_AT_KEY, datetime.now())
        self._dump_to_file()