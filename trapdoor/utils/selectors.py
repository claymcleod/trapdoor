from typing import Any, Dict, List, Optional, Tuple

class Selector:

    def __init__(self, split_character: str = '.'):
        self.split_character = split_character
        

    def split(self, selector: str) -> Tuple[List[str], str]:
        """Splits a selector based on the split character designated in
        the `Selector` object.

        :param selector: Selector to split by the split character.
        :type selector: str
        :raises ValueError: If the provided selector is not a string.
        :return: (Hierarchy, Subkey)
        :rtype: Tuple[List[str], str]

        >>> Selector().split("test")
        ([], 'test')
        >>> Selector().split("test.meta.key")
        (['test', 'meta'], 'key')
        >>> Selector().split(123)
        Traceback (most recent call last):
        ...
        ValueError: Provided selector must be a string: 123
        """

        if not isinstance(selector, str):
            raise ValueError(f"Provided selector must be a string: {selector}")

        hierarchy = selector.split(".")
        subkey = hierarchy.pop()
        return hierarchy, subkey

    def select(self, selector: str, d: Dict) -> Optional[Any]:
        """Selects a value from a nested dictionary using the provided `selector`.

        :param selector: The selector to use to look up the value.
        :type selector: str
        :param d: The dictionary to look up the value within.
        :type d: Dict
        :raises KeyError: If any of the keys are not found in the dict. 
        :return: If available, the value returned by the selector. Else None.
        :rtype: Optional[Any]

        >>> Selector().select("test", {"test": "world"})
        'world'
        >>> Selector().select("test.meta.key", {"test": {"meta": {"key": "value"}}})
        'value'
        >>> result = Selector().select("test.meta.wrong-key", {"test": {"meta": {"key": "value"}}})
        >>> result is None
        True
        """

        hierarchy, subkey = self.split(selector)
        result: Any = d
        while hierarchy:
            key = hierarchy.pop(0)
            result = result.get(key)
            if not result:
                return None
        
        if not subkey in result:
            return None
        return result.get(subkey)

    def dict_from(self, selector: str, value: Any) -> Dict:
        """Generates a nested dictionary given a selector and a final
        value to set as the last key.

        :param selector: Selector used to create the dictionary.
        :type selector: str
        :param value: Value to set the final subkey to.
        :type value: Any
        :return: Dictionary containing your new value.
        :rtype: Dict

        >>> Selector().dict_from("test", "value")
        {'test': 'value'}
        >>> Selector().dict_from("test.meta.key", "value")
        {'test': {'meta': {'key': 'value'}}}
        >>> Selector().dict_from(None, "value")
        Traceback (most recent call last):
        ...
        ValueError: Provided selector must be a string: None
        """
        hierarchy, subkey = self.split(selector)
        result = {subkey: value}
        while hierarchy:
            result = {hierarchy.pop(): result}
        return result

    def update_from(self, selector: str, value: Any, d: Dict) -> Dict:
        """Updates the value within `d` at `selector` path to `value`.

        :param selector: Selector to use when updating values in `d`.
        :type selector: str
        :param value: Value to update the key to in `d`.
        :type value: Any
        :param d: The dictionary to update.
        :type d: Dict
        :return: Updated dictionary.
        :rtype: Dict

        >>> Selector().update_from("foo", "baz", {"foo": "bar"})
        {'foo': 'baz'}
        >>> Selector().update_from("foo.bar.baz", "world", {"foo": {"bar": {"baz": "hello"}}})
        {'foo': {'bar': {'baz': 'world'}}}
        """

        hierarchy, subkey = self.split(selector)
        ptr = d
        while hierarchy:
            key = hierarchy.pop(0)
            if not key in ptr:
                ptr[key] = {}

            ptr = ptr[key]
        ptr[subkey] = value
        return d
    