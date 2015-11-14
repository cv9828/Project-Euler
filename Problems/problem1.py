#!/usr/bin/env python



num = 1000
list = []
total = 0

for i in range (1, num):
    if (i%3 == 0):
        list.append(i)
    elif(i%5 == 0):
        list.append(i)
for j in list:
    total+=j

print (total)
