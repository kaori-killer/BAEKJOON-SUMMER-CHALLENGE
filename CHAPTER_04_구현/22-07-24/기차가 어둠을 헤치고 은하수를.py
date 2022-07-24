from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
train = [deque([0] * 20) for _ in range(n)]

for _ in range(m):
    order = list(map(int, input().split()))
    train_num = order[1] - 1

    if order[0] == 1:
        x = order[2] - 1
        train[train_num][x] = 1

    elif order[0] == 2:
        x = order[2] - 1
        train[train_num][x] = 0

    elif order[0] == 3:
        train[train_num][19] = 0
        train[train_num].rotate()

    else:
        train[train_num][0] = 0
        train[train_num].rotate(-1)


count = 0
pass_train = []
for now_train in train:
    if now_train in pass_train:
        continue
    count += 1
    pass_train.append(now_train)

print(count)