n,v,r = input().lower(),['a', 'e', 'i', 'o', 'u', 'y'],""
for i in n:
    voy = False
    for j in v:
        if j == i: voy= True
    if voy == False:r+='.'+i
print(r)


