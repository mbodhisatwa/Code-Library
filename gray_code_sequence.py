def gray_code(bit_count: int) -> list:
    

    # bit count represents no. of bits in the gray code
    if bit_count < 0:
        raise ValueError("The given input must be positive")

    # get the generated string sequence
    sequence = gray_code_sequence_string(bit_count)
    #
    # convert them to integers
    for i in range(len(sequence)):
        sequence[i] = int(sequence[i], 2)

    return sequence


def gray_code_sequence_string(bit_count: int) -> list:
    if bit_count == 0:
        return ["0"]

    if bit_count == 1:
        return ["0", "1"]

    seq_len = 1 << bit_count  
    smaller_sequence = gray_code_sequence_string(bit_count - 1)

    sequence = []

    # append 0 to first half of the smaller sequence generated
    for i in range(seq_len // 2):
        generated_no = "0" + smaller_sequence[i]
        sequence.append(generated_no)

    # append 1 to second half ... start from the end of the list
    for i in reversed(range(seq_len // 2)):
        generated_no = "1" + smaller_sequence[i]
        sequence.append(generated_no)

    return sequence


if __name__ == "__main__":
    import doctest

    doctest.testmod()
