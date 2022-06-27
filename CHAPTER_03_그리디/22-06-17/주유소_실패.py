n = int(input())
w = list(map(int, input().split()))
v = list(map(int, input().split()))

w.reverse()
v.reverse()

tmp = 0
result = 0
for i in range(n):
    if v[i] == min(v[i:]):
        result += v[i] * tmp
        tmp = 0
    if i < n - 1:
        tmp += w[i]

print(result)