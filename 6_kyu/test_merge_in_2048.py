from merge_in_2048 import


class TestMergeIn2048:

    def test_assert_is_list(self, row):
        print(type(MergeIn2048(row)))
        assert isinstance(MergeIn2048, list)

    def test_is_not_0(self, row):
        return
