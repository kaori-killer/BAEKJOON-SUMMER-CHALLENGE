num = int(input())
li = list(map(int, input().split()))
result = 0

li.sort()
if len(li) % 2 != 0:
    result = li.pop()

length = len(li)
for i in range(length // 2):
    result = max(result, li[i] + li[length-i-1])

print(result)