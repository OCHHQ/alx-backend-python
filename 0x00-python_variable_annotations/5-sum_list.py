#!/usr/bin/env python3
"""
Module that provides a function to sum a list of floating point numbers.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floating-point numbers.

    Args:
        input_list: A list of floating-point numbers

    Returns:
        The sum of all numbers in the list as a float
    """
    return float(sum(input_list))
