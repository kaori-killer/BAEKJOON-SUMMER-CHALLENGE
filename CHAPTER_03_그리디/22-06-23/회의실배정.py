n = int(input())
li = []

for _ in range(n):
    li.append(list(map(int, input().split())))
li.sort(key=lambda x: [x[1], x[0]])

pre_end = li[0][1]
count = 1

for val in li[1:]:
    now_start, now_end = val[0], val[1]
    if pre_end <= now_start:
        pre_end = now_end
        count += 1

print(count)
