n = int(input())
cash = []
result = 0

for _ in range(n):
    cash.append(int(input()))
cash.sort(reverse=True)

for i in range(1, n + 1):
    if not i % 3:
        continue
    result += cash[i-1]

print(result)