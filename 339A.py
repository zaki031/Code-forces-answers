sum = input().split("+")
hh = []
for i in range(len(sum)):
    hh.append(int(sum[i]))
print('+'.join(map(str,sorted(hh))))