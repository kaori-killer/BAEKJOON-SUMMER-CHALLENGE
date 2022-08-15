from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    order = deque([1])
    check[1] = 1

    while order:
        now_node = order.popleft()
        for next_node in graph[now_node]:
            if check[next_node] == 0:
                root_node[next_node] = now_node
                order.append(next_node)
                check[next_node] = 1

    return root_node


num = int(input())
graph = [[] for _ in range(num + 1)]
root_node = [[] for _ in range(num + 1)]
check = [0 for _ in range(num + 1)]

for _ in range(num - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = bfs()
for num in result[2:]:
    print(num)