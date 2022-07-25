num = int(input())


def BSearch(target):
    low = 1
    high = target

    while low <= high:
        mid = (low + high) // 2
        cal = mid * (mid + 1) // 2
        if cal <= target:
            result = mid
            low = mid + 1

        else:
            high = mid - 1

    return result


print(BSearch(num))