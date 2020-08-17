from creature import Creature
import random as rand

rows = 30
cols = 30

world = [["#"] * cols for _ in range(rows)]

def print_grid(grid):
	for row in grid:
		stringified_row = ""
		for r in row:
			stringified_row += str(r)
		print(stringified_row)

def grid_put(row, col, symbol, grid):
	if row > rows or row < 0 or col > cols or col < 0:
		print("Invalid value!")
	else:
		grid[rows - row - 1][col] = symbol

def spawn(creature, grid):
	row_pos = rand.randint(0,rows)
	col_pos = rand.randint(0,cols)
	grid_put(row_pos, col_pos, creature.get_symbol(), world)
	creature.set_position(row_pos, col_pos)




print_grid(world)
c = Creature()
spawn(c,world)
print_grid(world)
