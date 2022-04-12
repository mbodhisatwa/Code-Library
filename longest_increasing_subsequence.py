
from __future__ import annotations


def longest_subsequence(array: list[int]) -> list[int]:  # This function is recursive
   
    array_length = len(array)
    # If the array contains only one element, we return it (it's the stop condition of
    # recursion)
    if array_length <= 1:
        return array
        # Else
    pivot = array[0]
    isFound = False
    i = 1
    longest_subseq: list[int] = []
    while not isFound and i < array_length:
        if array[i] < pivot:
            isFound = True
            temp_array = [element for element in array[i:] if element >= array[i]]
            temp_array = longest_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot] + longest_subsequence(temp_array)
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq


if __name__ == "__main__":
    import doctest

    doctest.testmod()
