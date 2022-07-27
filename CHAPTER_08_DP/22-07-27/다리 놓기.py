def recur(i, j):
    if i == j:
        return 1
    elif i == 0:
        return j + 1

    if dp[i][j] != 0:
        return dp[i][j]

    for n in range(j, -1, -1):
        dp[i][n] += recur(i - 1, n - 1)
    print(i, j)
    return sum(dp[-1])

num = int(input())
for _ in range(num):
    i, j = map(int, input().split())
    dp = [[0] * j for _ in range(i)]
    print(recur(i-1, j-1))

