from collections import deque
import sys
input = sys.stdin.readline


def bfs(x, y, knife, value):
    queue = (deque([[x, y]]))
    count[x][y] = value
    knife_xy = [-1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]

            if 0 <= ax < n and 0 <= ay < m and count[ax][ay] == -1:
                if not knife:
                    if graph[ax][ay] == 2:
                        knife_xy = [ax, ay]

                    if graph[ax][ay] == 1:
                        continue

                count[ax][ay] = count[x][y] + 1
                queue.append([ax, ay])

    return [count[n-1][m-1], knife_xy]


n, m, t = map(int, input().split())
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 검X
count = [[-1] * m for _ in range(n)]
result = bfs(0, 0, False, 0)
no_knife_cnt = result[0]
knife_x, knife_y = result[1]
cnt = no_knife_cnt

# 검O
if knife_x != -1 or knife_y != -1:
    val = count[knife_x][knife_y]
    count = [[-1] * m for _ in range(n)]
    knife_cnt = bfs(knife_x, knife_y, True, val)[0]
    cnt = min(no_knife_cnt, knife_cnt)

print("Fail" if cnt == -1 or cnt > t else cnt)

