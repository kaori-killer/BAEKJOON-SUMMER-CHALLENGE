n = int(input())
li = list(map(int, input().split()))

set_li = sorted(list(set(li)))
dic = {val: idx for idx, val in enumerate(set_li)}

for val in li:
    print(dic[val], end=" ")
