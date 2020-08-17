

class Creature():

	def __init__(self,sight=2,health=10,stamina=10,symbol=1):
		self.sight = sight
		self.health = health
		self.stamina = stamina
		self.age = 0
		self.position = [None,None]
		self.symbol = symbol

	def __repr__(self):
		return "Implementing"

	def __str__(self):
		return "Implementing"

	def get_symbol(self):
		return self.symbol

	def set_position(self, row, col):
		self.position = [row,col]

	def get_position(self):
		return self.position