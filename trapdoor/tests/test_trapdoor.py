import os
import pytest # type: ignore
import toml
from datetime import datetime

from ..utils import fs
from ..trapdoor import Trapdoor

def test_initialization_works_out_of_the_box():
    store_name = "trapdoor_test"
    inst = Trapdoor(store_name, testing=True)
    expected_store_directory = os.path.expanduser(os.path.join("~", "." + store_name))
    assert inst.store_name == store_name
    assert inst.store_directory == expected_store_directory
    assert inst.config_filepath == os.path.join(inst.store_directory, "config.toml")
    assert os.path.exists(inst.store_directory) and os.path.isdir(inst.store_directory)
    assert fs.get_file_permissions(inst.store_directory) == 700

    # check the resulting toml file
    with open(inst.config_filepath, mode="r", encoding="utf-8") as f:
        contents = toml.load(f)
    created_at = inst.get("meta.created-at")
    updated_at = inst.get("meta.updated-at")
    assert isinstance(created_at, datetime)
    assert isinstance(updated_at, datetime)
    assert created_at == updated_at

    inst.set("hello.world", "test")
    assert inst.get("hello.world") == "test"
    created_at = inst.get("meta.created-at")
    updated_at = inst.get("meta.updated-at")
    assert created_at < updated_at

    # cleanup
    inst._cleanup()

def test_expand_store_fails_on_no_str():
    store_name = "trapdoor_test"
    with pytest.raises(ValueError, match="`store_directory` is not a string!"):
        Trapdoor(store_name, 12)

def test_repr_matches_expected():
    store_name = "trapdoor_test"
    inst = Trapdoor(store_name, testing=True)
    expected_store_directory = os.path.expanduser(os.path.join("~", "." + store_name))
    assert str(inst) == f"(Store name: {store_name}, Store directory: {expected_store_directory})"
    inst._cleanup()