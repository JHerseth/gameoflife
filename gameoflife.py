"""
Made by Jonas Herseth
Python implementation of Game of Life
v0.0.0.1
"""


class GameOfLife(object):
    """
    My implementation of Conways Game of Life

    Takes 3 params:
    gridheight: int - height of matrix
    gridwidth: int - width of matrix
    seed: list of touples [(1,2), (3,4), (5,6)] startseed
    """

    def __init__(self, gridheight, gridwidth, seed):
        self.grid = [[0 for x in range(gridwidth)] for y in range(gridheight)]
        self.seed = seed

    def neighbours(self, i, j):
        """
        Given coords i and j, returns number of living adjacent cells
        """
        ncells = sum([self.grid[i-1][j-1], self.grid[i-1][j], self.grid[i-1][j+1], \
                    self.grid[i][j-1], self.grid[i][j+1], \
                    self.grid[i+1][j-1], self.grid[i+1][j], self.grid[i+1][j+1]])
        return ncells

    def flip_cell(self, i, j):
        """
        Flips the cell state between alive and dead
        """
        self.grid[i][j] = 0 if self.grid[i][j] == 1 else 1


    def draw_game(self):
        """
        Draws the game
        """
        for row in self.grid:
            for elem in row:
                print(elem, end=' ')
            print('\n')



def main():
    """
    Game of life main function
    """
    game = GameOfLife(16, 32, 4)
    game.flip_cell(2, 2)
    game.draw_game()

if __name__ == "__main__":
    main()
