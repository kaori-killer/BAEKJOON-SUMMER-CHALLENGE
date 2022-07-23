n = int(input())
li = list(map(int, input().split()))
dp = [0] + ([1e9] * (n - 1))

for i in range(1, n):
    for j in range(0, i):
        cal = max((i - j) * (1 + abs(li[i] - li[j])), dp[j])  # max(j to i, 0 to j)
        dp[i] = min(dp[i], cal)

print(dp[-1])