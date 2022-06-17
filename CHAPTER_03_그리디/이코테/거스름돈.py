def solution(change):
    moneys = [500, 100, 50, 10]  # 단위가 가장 큰 순서대로
    count = 0

    for money in moneys:
        count += change // money
        change %= money

    return count


print(solution(1260))