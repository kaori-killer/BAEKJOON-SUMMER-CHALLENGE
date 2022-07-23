n = int(input())
li = list(map(int, input().split()))
dp = [1e9] * n
dp[0] = 0

for i in range(n):
    for j in range(i + 1, n):
        cal = (j - i) * (1 + abs(li[i] - li[j]))
        if dp[i] <= cal < dp[j]:
            dp[j] = cal

print(dp[-1])