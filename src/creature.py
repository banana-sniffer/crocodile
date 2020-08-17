

class Creature():

	def __init__(self,sight=2,health=10,stamina=100,symbol=1):
		self.sight = sight
		self.health = health
		self.stamina = stamina
		self.age = 0
		self.x = 0
		self.y = 0
		self.prev_x = 0
		self.prev_y = 0
		self.symbol = symbol
		self.actions = []

	def __repr__(self):
		return "Implementing"

	def __str__(self):
		return "Implementing"

	def view_world(self, world):
		pass

	def get_symbol(self):
		return self.symbol

	def set_position(self, x, y):
		self.x = x
		self.y = y

	def get_position(self, val):
		if val == 0:
			return self.x
		elif val == 1:
			return self.y
		else:
			return "Invalid value"

	def get_prev_position(self, val):
		if val == 0:
			return self.prev_x
		elif val == 1:
			return self.prev_y
		else:
			return "Invalid value"

	def possible_moves(self):


	def move(self, cmd):
		self.prev_x = self.get_position(0)
		self.prev_y = self.get_position(1)
		if cmd == 1:
			self.y += 1
		elif cmd == 2:
			self.x += 1
			self.y += 1
		elif cmd == 3:
			self.x += 1
		elif cmd == 4:
			self.x += 1
			self.y -= 1
		elif cmd == 5:
			self.y -= 1
		elif cmd == 6:
			self.x -= 1
			self.y -= 1
		elif cmd == 7:
			self.x -= 1
		elif cmd == 8:
			self.x -= 1
			self.y += 1
		else:
			print("Invalid command")
		self.stamina -= 1












