t = int(input())

for _ in range(t):
    n = int(input())
    li = []
    for _ in range(2):
        li.append(list(map(int, input().split())))

    dp = [[0] * n for _ in range(2)]
    dp[0][0] = li[0][0]
    dp[1][0] = li[1][0]

    for j in range(1, n):
        for i in range(2):
            if i == 0:
                val = dp[i+1][j-1]
            else:
                val = dp[i-1][j-1]

            dp[i][j] = max(dp[i][j - 1] - li[i][j - 1], val) + li[i][j]
    print(max(dp[0] + dp[1]))


# 현재 dp = 왼쪽(왼쪽값 제외) vs 대각선 값