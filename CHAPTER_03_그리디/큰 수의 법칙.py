def solution(n, m, k, li):  # n: 배열의 크기, m: 숫자가 더해지는 횟수, k: 연속 가능 횟수
    li.sort(reverse=True)
    count = 0
    answer = 0

    while count != m:
        for _ in range(k):
            answer += li[0]
            count += 1

            if count == m:
                return answer

        answer += li[1]
        count += 1
    return answer


print(solution(5, 8, 3, [2, 4, 5, 4, 6]))