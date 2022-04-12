

def dp_count(S, n):
   
    if n < 0:
        return 0
    # table[i] represents the number of ways to get to amount i
    table = [0] * (n + 1)

    # There is exactly 1 way to get to zero(You pick no coins).
    table[0] = 1

    for coin_val in S:
        for j in range(coin_val, n + 1):
            table[j] += table[j - coin_val]

    return table[n]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
