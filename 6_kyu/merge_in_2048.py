class Merge2048(list):



def merge(list_of_digits: list) -> list:
    for number in list_of_digits:
        if adjacent_is_not_0(number):
            pass

def adjacent_is_not_0(num):
    non_zero = []


class TestMergeIn2048:

    def test_assert_is_list(self, row):
        print(type(merge(row)))
        assert isinstance(merge(row), list)

    def test_is_not_0(self, row):
        return

