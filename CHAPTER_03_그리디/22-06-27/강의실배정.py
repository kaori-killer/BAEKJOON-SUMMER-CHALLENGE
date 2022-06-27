import sys
import heapq

input = sys.stdin.readline

heap = []
times = []

num = int(input())
for _ in range(num):
    start, end = map(int, input().split())
    times.append([end, start])
times.sort(key=lambda x: [x[1], x[0]])
# 예) 3 4 / 3 5 / 4 7 / 5 6 (O) : start 기준 정렬
# 예) 3 4 / 3 5 / 5 6 / 4 7 (X) : end 기준 정렬

heapq.heappush(heap, (times[0][0], times[0][1]))

for now_end, now_start in times[1:]:
    pre_end, pre_start = heapq.heappop(heap)

    if now_start < pre_end:
        heapq.heappush(heap, (pre_end, pre_start))
    heapq.heappush(heap, (now_end, now_start))


print(heap)
print(len(heap))