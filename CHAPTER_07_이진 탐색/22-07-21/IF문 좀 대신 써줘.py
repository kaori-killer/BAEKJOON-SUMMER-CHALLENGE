import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
li = []


# 큰 값 중에 최솟값
def BSearch(target):
    low = 0
    high = len(li) - 1
    result = None

    while low <= high:
        mid = (low + high) // 2

        if target <= li[mid]:
            result = li[mid]
            high = mid - 1

        else:
            low = mid + 1

    return result


for _ in range(n):
    data = input().split()
    key, val = int(data[1]), data[0]

    if key in dic:
        continue

    dic[key] = val
    li.append(key)

li.sort()

for _ in range(m):
    print(dic[BSearch(int(input()))])