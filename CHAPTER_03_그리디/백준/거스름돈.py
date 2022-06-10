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