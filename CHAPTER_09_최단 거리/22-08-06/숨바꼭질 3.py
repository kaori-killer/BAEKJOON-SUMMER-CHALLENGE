from collections import deque
import heapq


# 메모리 초과 방지2
def isValid(num):
    if not check.get(num, 0):
        check[num] = 1
        return True
    return False


def bfs():
    heap = []
    heapq.heappush(heap, [0, n])  # [count=우선순위, num]
    check[n] = 1

    while heap:
        count, now_num = heapq.heappop(heap)

        left, right, move = [now_num * 2, count], [now_num - 1, count + 1], [now_num + 1, count + 1]

        for next_num, new_count in left, right, move:
            if isValid(next_num):
                if next_num == k:
                    return new_count
                elif -1 < next_num < 100000:  # 메모리 초과 방지1
                    heapq.heappush(heap, [new_count, next_num])


n, k = map(int, input().split())
if n == k:
    print(0)
else:
    check = {}
    print(bfs())

# 우선순위 : 반례) 1 to 2 => 순간이동으로 이동 가능
