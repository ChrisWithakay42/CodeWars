import pytest
from ordered_count_of_characters import ordered_count


class TestOrderedCount:

    def test_input_is_empty(self):
        data = ''
        assert ordered_count(data) == []

    def test_ordered_count(self):
        data = 'abracadabra'
        expected = [
            ('a', 5),
            ('b', 2),
            ('r', 2),
            ('c', 1),
            ('d', 1)
        ]
        assert ordered_count(data) == expected



