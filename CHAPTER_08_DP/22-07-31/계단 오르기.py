n = int(input())
dp = [1, 3]
count = 1

while dp[0] != n and dp[1] != n:
    for i in [0, 1]:
        tmp = dp[i] + 3
        if tmp <= n:
            dp[i] = tmp
        else:
            dp[i] += 1
    count += 1
print("CY" if count % 2 == 0 else "SK")