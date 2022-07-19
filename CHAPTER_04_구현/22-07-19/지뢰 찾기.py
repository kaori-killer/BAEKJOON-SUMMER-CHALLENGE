n = int(input())
place = []
stars = []
count = [[0] * n for _ in range(n)]
result = [["."] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(n):
    place.append([])
    string = input()

    for j in range(n):
        place[i].append(string[j])
        if string[j] == "*":
            stars.append([i, j])

for data in stars:
    x, y = data[0], data[1]

    for i in range(8):
        ax = x + dx[i]
        ay = y + dy[i]

        if 0 <= ax < n and 0 <= ay < n:
            count[ax][ay] += 1

check = False
for i in range(n):
    string = input()

    for j in range(n):
        if string[j] == "x":
            result[i][j] = count[i][j]

            if place[i][j] == "*":
                check = True
        result[i][j] = str(result[i][j])

# 지뢰가 있는 칸이 열림
if check:
    for li in stars:
        x, y = li[0], li[1]
        result[x][y] = "*"

for li in result:
    print("".join(li))
print()