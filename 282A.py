n,k = int(input()),0
for i in range(n):
    x = input()
    if x == "++X" or x == "X++": k+=1
    if x == "--X" or x == "X--": k-=1
print(k)