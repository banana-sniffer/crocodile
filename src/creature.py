import random as rand
import string

class Creature():

    def __init__(self,sight=2,health=10,stamina=100,symbol="C"):
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
        self.name = self.get_random_string()
        self.env_view = None

    def __repr__(self):
        ret_value = "Name: {}\nPosition: {}\nHealth: {}\nStamina: {}\n".format(self.name, [self.x, self.y], self.health, self.stamina)
        return ret_value

    def __str__(self):
        ret_value = "Name: {}\nPosition: {}\nHealth: {}\nStamina: {}\n".format(self.name, [self.x, self.y], self.health, self.stamina)
        return ret_value

    def get_random_string(self,length=10):
        letters = string.ascii_lowercase
        result_str = ''.join(rand.choice(letters) for i in range(length))
        return result_str

    def get_sight(self):
        return self.sight

    def set_sight(self, sight):
        self.sight = sight

    def set_env_view(self, env_view):
        self.env_view = env_view

    def get_env_view(self):
        return self.env_view

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

    def legal_moves(self):
        pass

    def action(self):
        move_cmd = rand.randint(1,8)
        self.move(move_cmd)

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












