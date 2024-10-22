#!/usr/bin/env python3
"""
function to safely get the first element of a sequence.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, None otherwise.

    Args:
        lst: Any sequence type (list, tuple, etc.) with elements of any type

    Returns:
        The first element of the sequence if it exists, None otherwise
    """
    if lst:
        return lst[0]
    else:
        return None
