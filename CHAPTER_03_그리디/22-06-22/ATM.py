num = int(input())
li = list(map(int, input().split()))
li.sort()
result = li[0]

for i in range(1, len(li)):
    li[i] += li[i - 1]
    result += li[i]

print(result)