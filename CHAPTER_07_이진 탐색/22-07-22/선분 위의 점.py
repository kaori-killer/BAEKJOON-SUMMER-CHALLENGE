import sys
input = sys.stdin.readline


def BSearch(target):
    low = 0
    high = n - 1
    result = [-1, -1]

    while low <= high:
        mid = (low + high) // 2

        if dot_place[mid] == target:
            return [mid, mid]

        elif dot_place[mid] > target:
            result[0] = mid
            high = mid - 1

        else:
            result[1] = mid
            low = mid + 1

    return result


n, m = map(int, input().split())

dot_place = list(map(int, input().split()))
dot_place.sort()

line_place = []


def soultion(x_idx, y_idx):
    if x_idx == -1 or y_idx == -1:
        return 0
    return y_idx - x_idx + 1


for _ in range(m):
    x, y = map(int, input().split())
    x_idx = BSearch(x)[0]
    y_idx = BSearch(y)[1]

    print(soultion(x_idx, y_idx))
