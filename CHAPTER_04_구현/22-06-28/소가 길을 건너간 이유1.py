num = int(input())
li = [-1] * 11
count = 0

for _ in range(num):
    cow_num, direction = map(int, input().split())
    if li[cow_num] > -1 and li[cow_num] != direction:
        count += 1
    li[cow_num] = direction


print(count)