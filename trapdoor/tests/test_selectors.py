import pytest
from .. import selectors 

def test_split_selector_non_str():
    with pytest.raises(ValueError, match="Provided selector must be a string: 123"):
        selectors.split_selector(123)
    
def test_split_selector_single():
    hierarchy, subkey = selectors.split_selector("testing")
    assert hierarchy == []
    assert subkey == "testing"

def test_split_selector_multi():
    hierarchy, subkey = selectors.split_selector("testing.meta.key")
    assert hierarchy == ["testing", "meta"]
    assert subkey == "key"

def test_create_from_single_selector():
    d = selectors.create_from_selector("testing", "value")
    assert d == {"testing": "value"}

def test_create_from_multi_selector():
    d = selectors.create_from_selector("testing.meta.key", "value")
    assert d == {"testing": {"meta": {"key": "value"}}}

def test_select_single_selector():
    d = {"hello": "world"}
    assert selectors.select(d, "hello") == "world"

def test_select_multi_selector():
    d = {"testing": {"meta": {"key": "value"}}}
    assert selectors.select(d, "testing.meta.key") == "value"