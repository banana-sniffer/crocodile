from creature import Creature
from tree import Tree
import random as rand
import time
import os

class World():

    def __init__(self,rows=10,cols=10,seed=0,view=10):
        self.rows = rows # is y 
        self.cols = cols # is x 
        self.view = view
        self.world = [["#"] * cols for _ in range(rows)]
        self.clock = 0
        self.entities = []
        self.entities_status = []

    def generate(self,num_trees=10):
        for i in range(num_trees):
            t = Tree()
            spawn(t)

    def print_grid(self):
        for row in self.world:
            stringified_row = ""
            for r in row:
                stringified_row += str(r)
            print(stringified_row)

    def world_put(self, x, y, symbol):
        if self.out_of_bounds(x, y):
            print("Invalid value!")
        else:
            self.world[self.rows - y - 1][x] = symbol

    def world_put_new(self, x, y, entity):
        if self.out_of_bounds(x, y):
            print("Invalid value!")
        else:
            self.world[self.rows - y - 1][x] = entity.symbol
            self.entities.append(entity)
            self.entities_status.append(entity.status)

    def world_get(self, x, y):
        if self.out_of_bounds(x, y):
            print("Invalid value!")
        else:
            return self.world[self.rows - y - 1][x]

    def out_of_bounds(self, x, y):
        if y >= self.rows or y < 0 or x >= self.cols or x < 0:
            return True
        return False

    def update_position(self, entity):
        if entity.move_status:
            self.world_put(entity.get_prev_position(0),entity.get_prev_position(1),"#")
            self.world_put(entity.get_position(0),entity.get_position(1),entity.get_symbol())

    def spawn(self, entity):
        x = rand.randint(0,self.cols-1)
        y = rand.randint(0,self.rows-1)
        while self.world_get(x,y) != "#":
            x = rand.randint(0,self.cols-1)
            y = rand.randint(0,self.rows-1)
        self.world_put(x, y, entity.get_symbol())
        entity.set_position(x, y)
        self.entities.append(entity)
        self.entities_status.append(entity.status)
        self.entity_view()

    def entity_view(self):
        for entity in self.entities:
            if entity.get_sight() != 0:
                size = entity.get_sight() * 2 + 1
                ret_value = [[] * size for _ in range(size)]
                entity_x = entity.get_position(0)
                entity_y = entity.get_position(1)
                up_down = [i - 5 for i in range(size - entity.get_sight(),size + entity.get_sight() + 1)]
                for i in up_down:
                    for j in up_down:
                        if not self.out_of_bounds(entity_x + j, entity_y - i):
                            ret_value[i + entity.get_sight()].append(self.world_get(entity_x + j, entity_y - i))
                        else:
                            ret_value[i + entity.get_sight()].append('')
                entity.set_env_view(ret_value)


    def tick(self):
        for i in range(len(self.entities)-1,-1,-1):
            self.entities[i].action(self)
            self.update_position(self.entities[i])
            self.entity_view()
            # There is no health check right now for the fruit
            self.entities_status[i] = self.entities[i].health_check()
            if self.entities_status[i] == "D":
                self.entities_status.remove(i)
                self.entities.remove(i)
        self.clock += 1

    def all_entity_check(self):
        for e in self.entities:
            print(e)


