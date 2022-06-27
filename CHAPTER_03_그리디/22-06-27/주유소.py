n = int(input())
costs = list(map(int, input().split()))
nodes = list(map(int, input().split()))

min_node = nodes[0]
result = 0

for i in range(n - 1):
    if nodes[i] <= min_node:
        min_node = nodes[i]
    result += min_node * costs[i]
print(result)