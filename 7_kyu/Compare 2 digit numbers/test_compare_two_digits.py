from compate_two_digits import compare


def test_compare(digits_to_compare):
    expected_results = ["50%", "100%", "100%", "100%", "50%", "50%", "50%", "0%", "0%", "0%", "50%", ]
    for index, digits in enumerate(digits_to_compare):
        assert compare(digits[0], digits[1]) == expected_results[index]

