n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

dx = [1, 0]
dy = [0, 1]

for i in range(n):
    for j in range(n):
        if i == n - 1 and j == n - 1:
            print(dp[i][j])
            break

        for k in range(2):
            ai = i + (dx[k] * graph[i][j])
            aj = j + (dy[k] * graph[i][j])
            if ai < n and aj < n:
                dp[ai][aj] += dp[i][j]

#BFS로 하면 안된다.