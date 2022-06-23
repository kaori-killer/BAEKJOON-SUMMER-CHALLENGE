def BSearch(li, target):
    low = 0
    high = len(li) - 1

    result = -1

    while low <= high:
        mid = (low + high) // 2

        if li[mid] <= target:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


n, k = map(int, input().split())
li = []
count = 0

for _ in range(n):
    li.append(int(input()))

idx = BSearch(li, k)

while k:
    for i in range(idx, -1, -1):
        count += k // li[i]
        k = k % li[i]

print(count)