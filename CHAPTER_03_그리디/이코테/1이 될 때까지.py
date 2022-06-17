def solution(n, k, cnt):
    if n == 1:
        return cnt
    elif n % k == 0:
        return solution(n // k, k, cnt + 1)
    else:
        return solution(n - 1, k, cnt + 1)


print(solution(17, 4, 0))

