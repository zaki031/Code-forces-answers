n,s = int(input()),0
for i in range(n):
    t,p = input(),0
    for j in range(5):
        if t[j] == "1": p+=1
    if p>1:s+=1
print(s)
