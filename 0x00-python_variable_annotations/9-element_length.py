#!/usr/bin/env python3
"""
function to calculate lengths of elements in an iterable.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    iterable of sequences and returns a list of tuples.

    Args:
        lst: An iterable containing sequences

    Returns:
        A list of tuples where each tuple contains a sequence and its length
    """
    return [(i, len(i)) for i in lst]
