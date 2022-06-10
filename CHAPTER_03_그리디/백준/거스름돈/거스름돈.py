# 2와 5는 서로소이기 때문에 무작정 가장 큰 수로 나눌 수 없다.
# 현재 금액 - 5가 5 또는 2의 배수면 현재 금액에서 5를 빼도 된다. 아니라면 2를 빼야한다.
# 현재 금액이 음수가 되면 -1를 반환한다.

def solution():
    num = int(input())
    count = 0

    while num:
        if num < 1:
            return -1
        else:
            count += 1
            tmp = num - 5

            if tmp % 5 == 0 or tmp % 2 == 0:
                num -= 5
            else:
                num -= 2
    return count


print(solution())