#!/usr/bin/env python




n = 4000000
list = [1,2]

total = 0
def fib():
    if list[-1] < 4000000:
        k = list[-1]+list[-2]
        list.append(k)
        fib()

fib()
list.pop(-1)

for i in list:
    if i%2 == 0:
        total += i

print total

