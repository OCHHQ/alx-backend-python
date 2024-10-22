#!/usr/bin/env python3
"""
Module that provides a function to create a tuple from a string and number.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Creates a tuple from a string and a number.

    Args:
        k: A string to be used as the first element of the tuple
        v: An integer or float to be squared and used as the second element

    Returns:
        A tuple containing the string and the square of the number as a float
    """
    return (k, float(v ** 2))
