import sys
input = sys.stdin.readline


def Bsearch(stack, s):
    low = 0
    high = len(stack) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2
        if stack[mid] <= s:
            result = mid
            low = mid + 1
        else:
            high = mid - 1

    return result


n = int(input())
time = []

for _ in range(n):
    time.append(list(map(int, input().split())))

time.sort()
s, e = time.pop(0)
stack = [e]

for s, e in time:
    stack.sort()
    idx = Bsearch(stack, s)
    if idx == -1:
        stack.append(e)
    else:
        stack[idx] = e

print(len(stack))