#!/usr/bin/env python3
"""
retrieving values from a dictionary with proper type annotations.
"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) \
        -> Union[Any, T]:
    """
    Safely retrieves a value from a mapping using a key, with a default value
    if the key is not found.

    Args:
        dct: The input mapping/dictionary to search in
        key: The key to look up in the mapping
        default: The default value to return if key is not found (default=None)

    Returns:
        The value from the mapping if key exists, otherwise the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
