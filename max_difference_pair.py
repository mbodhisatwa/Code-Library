def max_difference(a: list[int]) -> tuple[int, int]:
 
    # base case
    if len(a) == 1:
        return a[0], a[0]
    else:
        # split A into half.
        first = a[: len(a) // 2]
        second = a[len(a) // 2 :]

        # 2 sub problems, 1/2 of original size.
        small1, big1 = max_difference(first)
        small2, big2 = max_difference(second)

        # get min of first and max of second
        # linear time
        min_first = min(first)
        max_second = max(second)

        # 3 cases, either (small1, big1),
        # (min_first, max_second), (small2, big2)
        # constant comparisons
        if big2 - small2 > max_second - min_first and big2 - small2 > big1 - small1:
            return small2, big2
        elif big1 - small1 > max_second - min_first:
            return small1, big1
        else:
            return min_first, max_second


if __name__ == "__main__":
    import doctest

    doctest.testmod()
