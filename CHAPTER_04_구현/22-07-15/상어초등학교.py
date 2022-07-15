num = int(input())
graph = [[0] * (num + 1) for _ in range(num + 1)]
infos = []

for _ in range(num**2):
    infos.append(list(map(int, input().split())))

for info in infos:
    num = info[0]

