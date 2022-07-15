from collections import defaultdict

num = int(input())
dict = defaultdict(int)

for _ in range(num):
    dict[input().split(".")[1]] += 1

order = sorted(dict.items())
for val in order:
    print(val[0], val[1])