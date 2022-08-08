def floyd():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
floyd()

for _ in range(m):
    a, b, c = map(int, input().split())
    if graph[a-1][b-1] > c:
        print("Stay here")
    else:
        print("Enjoy other party")