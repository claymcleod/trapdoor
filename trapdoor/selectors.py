from typing import Any, Dict


def split_selector(selector: str):
    if not isinstance(selector, str):
        raise ValueError(f"Provided selector must be a string: {selector}")

    hierarchy = selector.split(".")
    subkey = hierarchy.pop()
    return hierarchy, subkey

def create_from_selector(selector: str, value: Any):
    hierarchy, subkey = split_selector(selector)
    result = {subkey: value}
    while hierarchy:
        result = {hierarchy.pop(): result}

    return result

def update_from_selector(d: Dict, selector: str, value: Any):
    hierarchy, subkey = split_selector(selector)
    while hierarchy:
        key = hierarchy.pop()
        if not key in d:
            d[key] = {}

        d = d[key]

    d[subkey] = value
    
def select(d: Dict, selector: str):
    hierarchy, subkey = split_selector(selector)
    result = d
    while hierarchy:
        result = result[hierarchy.pop(0)]
    
    return result[subkey]