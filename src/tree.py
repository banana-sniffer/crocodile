import random as rand
import entity

class Tree(entity.Entity):

    def __init__(self):
        super().__init__()
        self.symbol = "T"
        self.x = 0
        self.y = 0
        self.sight = 0
        self.move_status = False
        self.health = 1000
        self.stamina = 1000

    def __str__(self):
        return "Implementing str" 

    def __repr__(self):
        return "Implementing repr"

    def action(self):
        pass


