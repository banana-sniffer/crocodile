import random as rand
import entity

class Creature(entity.Entity):

    def __init__(self,sight=2,health=10,max_stamina=100,max_hunger=100,symbol="C"):
        super().__init__()
        self.sight = sight
        self.health = health
        self.max_stamina = max_stamina
        self.stamina = self.max_stamina
        self.max_hunger = max_hunger
        self.hunger = self.max_hunger
        self.age = 0
        self.prev_x = 0
        self.prev_y = 0
        self.symbol = symbol
        self.actions = []
        self.env_view = None
        self.knockout_timer = int(max_stamina * 0.25)
        self.inventory = None
        self.move_status = True

    def __repr__(self):
        ret_value = "Name: {}\nPosition: {}\nHealth: {}\nStamina: {}\nStatus: {}\n".format(self.name, [self.x, self.y], self.health, self.stamina, self.status)
        return ret_value

    def __str__(self):
        ret_value = "Name: {}\nPosition: {}\nHealth: {}\nStamina: {}\nStatus: {}\n".format(self.name, [self.x, self.y], self.health, self.stamina, self.status)
        return ret_value

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
            self.health -= 1
        else:
            self.status = "A"
        return self.status












