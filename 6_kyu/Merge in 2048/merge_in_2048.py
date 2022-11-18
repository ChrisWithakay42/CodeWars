class Merge2048:

    def merge(self, grid_row: list[int]) -> list[int]:
        merged_grid_row = []
        for tile in grid_row:
            if tile == 0:
                merged_grid_row.append(tile)
        return grid_row
