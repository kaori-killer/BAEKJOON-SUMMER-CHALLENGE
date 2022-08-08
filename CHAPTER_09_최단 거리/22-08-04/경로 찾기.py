from collections import deque


# BFS, 인접하지 않은 노드 모두 연결
def BFS(start_node):
    queue = deque([start_node])
    check = [0] * num

    while queue:
        now_node = queue.popleft()

        for next_node in graph[now_node]:
            if check[next_node] == 1:
                continue

            check[next_node] = 1
            result[start_node][next_node] = 1
            queue.append(next_node)


num = int(input())
graph = []
for i in range(num):
    graph.append([])
    input_num = list(map(int, input().split()))
    for j in range(num):
        if input_num[j] == 1:
            graph[i].append(j)

result = [[0] * num for _ in range(num)]

for i in range(num):
    BFS(i)

for li in result:
    print(*li)
