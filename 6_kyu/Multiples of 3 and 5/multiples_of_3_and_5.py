def solution(number: int) -> int:
    return sum(n for n in range(number) if n%3 == 0 or n%5 == 0) if number > 0 else 0

