import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
graph = [[] for _ in range(n + 1)]
check = [0] * (n + 1)

for _ in range(m):
    A, B = map(int, input().split())
    graph[A].append(B)


def bfs(graph, start, check):
    check[start] = 1
    queue = deque([[start, 0]])
    result = []

    while queue:
        now_node, count = queue.popleft()
        for next_node in graph[now_node]:
            if check[next_node] == 1:
                continue

            check[next_node] = 1
            next_count = count + 1

            queue.append([next_node, next_count])

            if next_count == k:
                result.append(next_node)

            elif next_count > k:
                return result

    return result


result = bfs(graph, x, check)
if len(result) == 0:
    print(-1)
else:
    # 오름차순 출력
    result.sort()
    for node in result:
        print(node)