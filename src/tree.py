from fruit import Fruit
import random as rand
import entity

class Tree(entity.Entity):

    def __init__(self):
        super().__init__()
        self.symbol = "T"
        self.x = 0
        self.y = 0
        self.sight = 1
        self.move_status = False
        self.health = 1000
        self.stamina = 1000
        self.fruits = []

    def __repr__(self):
        ret_value = "Name: {}\nPosition: {}\nStatus: {}\nSymbol: {}\n".format(self.name, [self.x, self.y], self.status, self.symbol)
        return ret_value

    def __str__(self):
        ret_value = "Name: {}\nPosition: {}\nStatus: {}\nSymbol: {}\n".format(self.name, [self.x, self.y], self.status, self.symbol)
        return ret_value

    def health_check(self):
        pass

    def action(self, world):
        # pass
        random_action = rand.uniform(0,1)
        print(self.fruits)
        for f in self.fruits:
            f.grow()
            if f.ripeness >= 5 and not f.dropped:
                f.drop()
                open_spaces = self.open_spaces()
                print(open_spaces)
                random_open_space = rand.choice(open_spaces)
                print(random_open_space)
                drop_cords = self.get_drop_coordinate(random_open_space)
                world.world_put_new(drop_cords[0], drop_cords[1], f)
        if len(self.fruits) < 1 and random_action > 0.25:
            new_fruit = Fruit()
            self.fruits.append(new_fruit)

    def get_drop_coordinate(self, cmd):
        drop_cords_x = self.x
        drop_cords_y = self.y
        if cmd == 1:
            drop_cords_y += 1
        elif cmd == 2:
            drop_cords_x += 1
            drop_cords_y += 1
        elif cmd == 3:
            drop_cords_x += 1
        elif cmd == 4:
            drop_cords_x += 1
            drop_cords_y -= 1
        elif cmd == 5:
            drop_cords_y -= 1
        elif cmd == 6:
            drop_cords_x -= 1
            drop_cords_y -= 1
        elif cmd == 7:
            drop_cords_x -= 1
        elif cmd == 8:
            drop_cords_x -= 1
            drop_cords_y += 1
        else:
            print("Invalid Tree command")
        return [drop_cords_x, drop_cords_y]

    def drop(self):
        pass



