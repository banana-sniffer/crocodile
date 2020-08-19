import random as rand
import string

class Creature():

    def __init__(self,sight=2,health=10,max_stamina=100,symbol="C"):
        self.sight = sight
        self.health = health
        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        self.age = 0
        self.x = 0
        self.y = 0
        self.prev_x = 0
        self.prev_y = 0
        self.symbol = symbol
        self.actions = []
        self.name = self.get_random_name()
        self.env_view = None
        self.status = "A"
        self.knockout_timer = int(max_stamina * 0.25)

    def __repr__(self):
        ret_value = "Name: {}\nPosition: {}\nHealth: {}\nStamina: {}\nStatus: {}\n".format(self.name, [self.x, self.y], self.health, self.stamina, self.status)
        return ret_value

    def __str__(self):
        ret_value = "Name: {}\nPosition: {}\nHealth: {}\nStamina: {}\nStatus: {}\n".format(self.name, [self.x, self.y], self.health, self.stamina, self.status)
        return ret_value

    def get_random_string(self,length=10):
        letters = string.ascii_lowercase
        result_str = ''.join(rand.choice(letters) for i in range(length))
        return result_str

    def get_random_name(self):
        return rand.choice(open("all.txt").read().split())

    def get_sight(self):
        return self.sight

    def set_sight(self, sight):
        self.sight = sight

    def set_env_view(self, env_view):
        self.env_view = env_view

    def get_env_view(self, x=-1, y=-1):
        if x == -1 or y == -1:
            return self.env_view
        return self.env_view[(2*self.sight) - y][x]

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
        moves = []
        if self.get_env_view(self.sight, self.sight + 1) == "#":
            moves.append(1)
        if self.get_env_view(self.sight + 1, self.sight + 1) == "#":
            moves.append(2)    
        if self.get_env_view(self.sight + 1, self.sight) == "#":
            moves.append(3)
        if self.get_env_view(self.sight + 1, self.sight - 1) == "#":
            moves.append(4)
        if self.get_env_view(self.sight, self.sight - 1) == "#":
            moves.append(5)
        if self.get_env_view(self.sight - 1, self.sight - 1) == "#":
            moves.append(6)
        if self.get_env_view(self.sight - 1, self.sight) == "#":
            moves.append(7)
        if self.get_env_view(self.sight - 1, self.sight + 1) == "#":
            moves.append(8)
        return moves

    def action(self):
        if self.status == "KO" and self.stamina < 25:
            self.rest()
        else:
            action = rand.randint(0,100)
            if action < 95:
                move_cmd = rand.choice(self.legal_moves())
                self.move(move_cmd)
            else:
                self.rest()

    def rest(self):
        if self.stamina < self.max_stamina:
            self.stamina += 1
        return "Resting"

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
        return "Moving"

    def health_check(self):
        if self.health < 0:
            self.status = "D"
        elif self.status == "KO" and self.stamina < 25:
            self.status = "KO"
        elif self.stamina < 0:
            self.status = "KO"
        else:
            self.status = "A"
        return self.status












