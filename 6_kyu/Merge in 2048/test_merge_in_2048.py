from merge_in_2048 import Merge2048


class TestMergeIn2048:
    
    def test_merge_empty_grid_squares(self):
        empty_grid_row = [0, 0, 0, 0]
        assert Merge2048().merge(empty_grid_row) == [0, 0, 0, 0]

