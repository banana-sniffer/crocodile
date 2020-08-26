import random as rand

class Entity():

    def __init__(self):
        self.x = 0
        self.y = 0
        self.status = "A"
        self.internal_clock = 0
        self.name = self.get_random_name()
        self.env_view = None

    def get_random_name(self):
        return rand.choice(open("all.txt").read().split())

    def get_symbol(self):
        return self.symbol

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_sight(self):
        return self.sight

    def set_sight(self, sight):
        self.sight = sight

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

    def set_env_view(self, env_view):
        self.env_view = env_view

    def get_env_view(self, x=-1, y=-1):
        if x == -1 or y == -1:
            return self.env_view
        return self.env_view[(2*self.sight) - y][x]

    def health_check(self):
        if self.health < 0:
            self.status = "D"
        elif self.status == "KO" and self.stamina < 25:
            self.status = "KO"
        elif self.stamina < 0:
            self.status = "KO"
            self.health -= 1
        else:
            self.status = "A"
        return self.status

    def open_spaces(self):
        spaces = []
        if self.get_env_view(self.sight, self.sight + 1) == "#":
            spaces.append(1)
        if self.get_env_view(self.sight + 1, self.sight + 1) == "#":
            spaces.append(2)    
        if self.get_env_view(self.sight + 1, self.sight) == "#":
            spaces.append(3)
        if self.get_env_view(self.sight + 1, self.sight - 1) == "#":
            spaces.append(4)
        if self.get_env_view(self.sight, self.sight - 1) == "#":
            spaces.append(5)
        if self.get_env_view(self.sight - 1, self.sight - 1) == "#":
            spaces.append(6)
        if self.get_env_view(self.sight - 1, self.sight) == "#":
            spaces.append(7)
        if self.get_env_view(self.sight - 1, self.sight + 1) == "#":
            spaces.append(8)
        return spaces