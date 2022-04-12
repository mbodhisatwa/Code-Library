

from __future__ import annotations


def merge(input_list: list, low: int, mid: int, high: int) -> list:

    result = []
    left, right = input_list[low:mid], input_list[mid : high + 1]
    while left and right:
        result.append((left if left[0] <= right[0] else right).pop(0))
    input_list[low : high + 1] = result + left + right
    return input_list


# iteration over the unsorted list
def iter_merge_sort(input_list: list) -> list:

    if len(input_list) <= 1:
        return input_list
    input_list = list(input_list)

    # iteration for two-way merging
    p = 2
    while p < len(input_list):
        # getting low, high and middle value for merge-sort of single list
        for i in range(0, len(input_list), p):
            low = i
            high = i + p - 1
            mid = (low + high + 1) // 2
            input_list = merge(input_list, low, mid, high)
        # final merge of last two parts
        if p * 2 >= len(input_list):
            mid = i
            input_list = merge(input_list, 0, mid, len(input_list) - 1)
        p *= 2

    return input_list


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item.strip()) for item in user_input.split(",")]
    print(iter_merge_sort(unsorted))