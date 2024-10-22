#!/usr/bin/env python3
"""
This module provides a function for zooming arrays by duplicating each element
a specified number of times.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a list where each element in the input tuple is repeated
    based on the zoom factor.

    Args:
        lst: Input tuple of elements to be zoomed
        factor: Number of times each element should be repeated (default=2)

    Returns:
        List containing the zoomed elements
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
