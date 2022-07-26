import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, k = map(int, input().split())
after_li = [0] + list(input().split())
d = [0] + list(map(int, input().split()))


def card_mix(after, cnt):
    if cnt == 0:
        return after

    tmp = [0] * (n + 1)
    for i in range(1, n + 1):
        tmp[d[i]] = after[i]

    return card_mix(tmp, cnt-1)


print(" ".join(card_mix(after_li, k)[1:]))