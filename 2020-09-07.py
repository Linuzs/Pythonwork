ll = [i for i in range(10) if i % 3 == 0 or i % 5 == 0]
print(ll)

print(sum([i for i in range(10) if i % 3 == 0 or i % 5 == 0]))

print(sum([i for i in range(1,1000) if i % 3 == 0 or i % 5 == 0]))


# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:31:29 2020

@author: tute
"""

world = [['#','#','#','#','#','#'],['#','#','#','#','#','#'],['#','#','#','#','#','#']]

up_down = 0
left_right = 0

while True:        
    world[up_down][left_right] = "*"
    print("Your are here:")
    print("".join(world[0]))
    print("".join(world[1]))
    print("".join(world[2]))
    user_input = input("wads:")
    
    if user_input == "w":
        world[up_down][left_right] = "#"
        up_down -= 1
    elif user_input == "a":
        world[up_down][left_right] = "#"
        left_right -= 1
    elif user_input == "s":
        world[up_down][left_right] = "#"
        up_down += 1
    elif user_input == "d":
        world[up_down][left_right] = "#"
        left_right += 1    

        
        
        
        
        
        
        
        
f = open("KMSWHS.txt")
ff = f.read()
fff = ff.split()
d = {}
for i in fff:
    if i in d:
        d[i] += 1
    else:
        d[i] =1
print(d)
f.close()
