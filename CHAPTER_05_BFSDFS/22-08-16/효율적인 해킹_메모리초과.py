import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)


def dfs(start_node):
    check[start_node] = 1

    for next_node in graph[start_node]:
        if check[next_node] == 0:
            dfs(next_node)
            count[start_node] += count[next_node]


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

result = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    count = [1 for _ in range(n + 1)]
    check = [0 for _ in range(n + 1)]
    dfs(i)

    result[i] = count[i]

max_num = max(result)
for i in range(n + 1):
    if result[i] == max_num:
        print(i, end=" ")