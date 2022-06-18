# TIp = 원래 주려고 생각했던 돈 - (받은 등수 - 1)

import heapq

heap = []
n = int(input())
result = 0

for _ in range(n):
    num = int(input())
    heapq.heappush(heap, (-num, num))

for k in range(n):
    tmp = heapq.heappop(heap)[1] - k
    result += 0 if tmp < 0 else tmp

print(result)