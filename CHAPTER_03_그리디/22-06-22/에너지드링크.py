num = int(input())
li = list(map(int, input().split()))

for i in range(len(li) - 1):
    if li[i] > li[i + 1]:
        li[i], li[i + 1] = li[i + 1], li[i]

a = li.pop()
b = sum(li) / 2
print(a + b)