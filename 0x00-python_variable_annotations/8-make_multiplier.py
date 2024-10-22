#!/usr/bin/env python3
"""
Module that provides a function that creates a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The float value to multiply by

    Returns:
        A function that takes a float and returns the product with multiplier
    """
    def multiplier_function(n: float) -> float:
        """
        Multiplies input number by the multiplier.

        Args:
            n: The number to multiply

        Returns:
            The product of n and multiplier
        """
        return n * multiplier
    return multiplier_function
