from string import ascii_lowercase
def solve(arr):
    def is_letter_in_position(letter, position):
        alphabet = ascii_lowercase
        return alphabet.find(letter.lower()) + 1 == position

    result = []
    for word in arr:
        count = sum(is_letter_in_position(letter, position) for position, letter in enumerate(word, 1))
        result.append(count)
    return result