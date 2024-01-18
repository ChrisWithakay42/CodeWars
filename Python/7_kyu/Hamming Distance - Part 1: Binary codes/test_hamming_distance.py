from the_hamming_distance import hamming_distance


class TestHammingDistance:

    def test_hamming_distance(self):
        input_1 = '1010'
        input_2 = '0101'
        assert hamming_distance(input_1, input_2) == 4
