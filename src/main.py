from creature import Creature
from tree import Tree
from world import World
import random as rand
import time
import os

c = Creature()
w = World()
t1 = Tree()
t2 = Tree()
t3 = Tree()
t4 = Tree()
t5 = Tree()
w.spawn(c)
w.spawn(t1)
w.spawn(t2)
w.spawn(t3)
w.spawn(t4)
w.spawn(t5)
w.print_grid()
for i in range(500):
    os.system('clear')
    w.tick()
    w.print_grid()
    time.sleep(0.05)
print(w.clock)
print(c)