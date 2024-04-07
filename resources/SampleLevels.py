"""
0 = PATH
1 = WALL
2 = ENTANGLED BLOCK 1 -- equates to wall
3 = ENTANGLED BLOCK 2 -- equates to space
4 = ENTANGLED BLOCK TRIGGER
5 = SPAWN POINT
6 = CHECKPOINT 0
7 = CHECKPOINT 1
8 = CHECKPOINT_NEGATIVE
9 = CHECKPOINT_POSITIVE

"""
class Level():
    def __init__(self, grid, winning_cell: int, name: str):
        self.grid = grid
        self.winning_cell = winning_cell
        self.player_coords = (0, 0)
        self.name = name

        # setting player at spawn location
        self.set_player_spawn()

    def set_player_spawn(self):
        for y_coord, row in enumerate(self.grid):
            for x_coord, value in enumerate(row):
                if value == 5:
                    self.player_coords = (x_coord, y_coord)
                    return

    def get_coord_value(self, x, y):
        return self.grid[y][x]
    
    def set_coord_value(self, x, y, cell_type):
        return self.grid[y][x] == cell_type
    
    def getWidth(self, x:int):
        return len(self.grid[x])

    def getHeight(self, y: int):
        return len(self.grid[y])
    
    def get_cell_type(self, x, y):
        return 
    
XGate = Level([
        [1, 1, 1, 0, 1, 1, 1, 1, 8, 1],
        [7, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 0, 6],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 5, 1, 1, 1, 9, 1, 0, 0, 0]
    ], 7, "X Gate"
)

ZGate = Level([
        [1, 0, 1, 0, 1, 0, 0, 0, 8, 1],
        [7, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 9],
        [1, 2, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 1, 2, 1, 1, 1],
        [1, 0, 1, 0, 4, 0, 0, 3, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 1, 1, 1, 0, 6],
        [1, 5, 0, 0, 0, 0, 0, 2, 0, 0]
    ], 7, "Z Gate"
)

HGate = Level([
        [0, 0, 0, 0, 0, 1, 0, 1, 8, 1],
        [7, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 0, 0, 1, 9],
        [1, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 0, 6],
        [1, 5, 1, 1, 1, 0, 1, 1, 1, 0]
    ], 7, "H Gate"
)