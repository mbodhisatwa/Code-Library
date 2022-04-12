def get_word_pattern(word: str) -> str:

    word = word.upper()
    next_num = 0
    letter_nums = {}
    word_pattern = []

    for letter in word:
        if letter not in letter_nums:
            letter_nums[letter] = str(next_num)
            next_num += 1
        word_pattern.append(letter_nums[letter])
    return ".".join(word_pattern)


if __name__ == "__main__":
    import pprint
    import time

    start_time = time.time()
    with open("dictionary.txt") as in_file:
        wordList = in_file.read().splitlines()

    all_patterns: dict = {}
    for word in wordList:
        pattern = get_word_pattern(word)
        if pattern in all_patterns:
            all_patterns[pattern].append(word)
        else:
            all_patterns[pattern] = [word]

    with open("word_patterns.txt", "w") as out_file:
        out_file.write(pprint.pformat(all_patterns))

    totalTime = round(time.time() - start_time, 2)
    print(f"Done!  {len(all_patterns):,} word patterns found in {totalTime} seconds.")
