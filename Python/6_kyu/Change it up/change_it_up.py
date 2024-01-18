# Create a function that takes a string as a parameter and does the following, in this order:
#
# Replaces every letter with the letter following it in the alphabet (see note below)
# Makes any vowels capital
# Makes any consonants lower case
# Note:
#
# the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.
# So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)

def changer(s):

    vowels = 'aeiouAEIOU'
    result = ''

    for char in s:
        if char.isalpha():
            char_lower = char.lower()
            char_lower = chr((ord(char_lower) - ord('a') +1) % 26 + ord('a'))

            if char_lower in vowels:
                char = char.upper()
            else:
                char = char_lower

        result += char

    return result
