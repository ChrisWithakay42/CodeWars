from collections import Counter

def ordered_count(inp: str) -> list[tuple[str, int]]:
    return list(Counter(inp).items())
