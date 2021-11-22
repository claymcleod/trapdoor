import os
import toml

from datetime import datetime


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
    
    def set(self, section: str, key: str, value: str):
        key_value_contents = f"""
[{section}]
{key} = "{value}"
            """
        self.contents.update(toml.loads(key_value_contents))
        self._dump_to_file()

    def _load_default_contents(self):
        now = datetime.now()
        self.contents = {
            "meta": {
                "created-at": now,
                "updated-at": now
            }
        }

    def _load_from_file(self):
        with open(self.filepath, mode="r", encoding="utf-8") as f:
            self.contents = toml.load(f)

    def _dump_to_file(self):
        with open(self.filepath, mode="w", encoding="utf-8") as f:
            toml.dump(self.contents, f)