#!/usr/bin/env python3
"""Returns the sum of all the elements in the input list `mxd_lst`."""


from typing import List


def sum_mixed_list(mxd_lst: List[float]) -> float:
    """  a list mxd_lst of integers and floats
    and returns their sum as a float """
    return sum(float(i) for i in mxd_lst)
