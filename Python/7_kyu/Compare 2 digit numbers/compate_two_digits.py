from collections import Counter


def compare(num1, num2):
    num1_str = str(num1)
    num2_str = str(num2)
    total_digits = len(num1_str)

    counter1 = Counter(num1_str)
    counter2 = Counter(num2_str)

    matching_digits = sum((counter1 & counter2).values())

    similarity_percentage = (matching_digits / total_digits) * 100
    return f"{similarity_percentage:.0f}%"