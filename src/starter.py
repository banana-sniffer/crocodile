from creature import Creature
import random as rand

rows = 10
cols = 10

world = [["#"] * cols for _ in range(rows)]

def print_grid(grid):
	for row in grid:
		stringified_row = ""
		for r in row:
			stringified_row += str(r)
		print(stringified_row)

def grid_put(x, y, symbol, grid):
	if y >= rows or y < 0 or x >= cols or x < 0:
		print("Invalid value!")
	else:
		grid[rows - y - 1][x] = symbol

def update_position(creature):
	grid_put(creature.get_prev_position(0),creature.get_prev_position(1),"#",world)
	grid_put(creature.get_position(0),creature.get_position(1),creature.get_symbol(),world)

def spawn(creature, grid):
	x = rand.randint(0,rows-1)
	y = rand.randint(0,cols-1)
	grid_put(x, y, creature.get_symbol(), world)
	creature.set_position(x, y)

c = Creature()
spawn(c,world)
print(c.get_position(0),c.get_position(1))
print_grid(world)
for i in range(1,9):
	c.move(i)
	update_position(c)
	print_grid(world)
	print(c.get_position(0),c.get_position(1))