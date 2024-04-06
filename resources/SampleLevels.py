"""
0 = PATH
1 = WALL
2 = ENTANGLED BLOCK 1
3 = ENTANGLED BLOCK 2
4 = ENTANGLED BLOCK TRIGGER
5 = SPAWN POINT
6 = CHECKPOINT 01
7 = CHECKPOINT 10
8 = CHECKPOINT 11

"""
class Level():
    def __init__(self, grid, winning_cell: int):
        self.grid = grid
        self.winning_cell = winning_cell
        self.player_coord = (0, 0)

        # setting player at spawn location
        self.set_player_spawn()

    def set_player_spawn(self):
        for y_coord, row in enumerate(self.grid):
            for x_coord, value in enumerate(row):
                if value == 5:
                    self.player_coord = (x_coord, y_coord)
                    return

    def get_coord_value(self, x, y):
        return self.grid[y][x]

XGate = Level([
        [1, 1, 1, 1, 1, 1, 1, 1, 8, 1],
        [7, 0, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 6],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 5, 1, 1, 1, 1, 1, 1, 1, 1]
    ], 7
)

ZGate = Level([
        [1, 0, 1, 0, 1, 0, 1, 1, 8, 1],
        [7, 0, 1, 1, 0, 1, 1, 0, 1, 0],
        [0, 0, 0, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 0, 1, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1, 1, 1, 6],
        [1, 5, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 5, 0, 0, 0, 1, 0, 0, 1, 0],
        [1, 5, 0, 0, 0, 1, 0, 0, 1, 0]
    ], 7
)

HGate = Level([
        [0, 0, 0, 0, 0, 1, 0, 1, 8, 1],
        [7, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 6],
        [1, 5, 1, 1, 1, 0, 1, 1, 1, 0],
        [1, 5, 1, 1, 1, 0, 1, 1, 1, 0],
        [1, 5, 1, 1, 1, 0, 1, 1, 1, 0]
    ], 7
)