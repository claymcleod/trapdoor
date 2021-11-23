import os
import toml

from . import selectors
from datetime import datetime

CREATED_AT_KEY = "meta.created-at"
UPDATED_AT_KEY = "meta.updated-at"

class ConfigFile:

    def __init__(self, 
        filepath: str
    ):
        self.contents = {}
        self.filepath = filepath

        if not os.path.exists(self.filepath):
            self._load_default_contents()
            self._dump_to_file()
        else:
            self._load_from_file()
    
    def set(self, key: str, value: str):
        selectors.update_from_selector(self.contents, key, value)
        self._dump_to_file()

    def get(self, key: str):
        self._load_from_file()
        return selectors.select(self.contents, key)

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