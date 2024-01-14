from string import ascii_lowercase

def is_panagram(s: str) -> bool:
    sentence_set = set(s.lower())
    return set(ascii_lowercase).issubset(sentence_set)
