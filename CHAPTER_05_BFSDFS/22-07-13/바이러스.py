from collections import deque

n = int(input())
k = int(input())
graph = [[] * n for _ in range(n + 1)]

check = [0] * (n + 1)
check[1] = 1

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
cnt = 0

while queue:
    ver = queue.popleft()

    for i in sorted(graph[ver]):
        if check[i] == 0:
            check[i] = 1

            queue.append(i)
            cnt += 1
print(cnt)