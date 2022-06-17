def solution(n, m, k, li):  # n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 연속 가능 횟수
    li.sort(reverse=True)

    repeat = li[0] * k + li[1]
    A = m // (k + 1)
    B = m % (k + 1)

    return (repeat * A) + (li[0] * B)  # (수열 * 반복 횟수) + (최댓값 * 더해야 하는 횟수)


print(solution(5, 8, 3, [2, 4, 5, 4, 6]))

