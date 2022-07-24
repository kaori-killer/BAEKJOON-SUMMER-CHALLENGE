n, c = map(int, input().split())
wifi = []

for _ in range(n):
    wifi.append(int(input()))
wifi.sort()


def BSearch():
    low = 1
    high = wifi[-1] - wifi[0]

    while low <= high:
        mid = (low + high) // 2

        count, pre = 1, wifi[0]
        for i in range(1, n):
            if mid <= wifi[i] - pre:
                count += 1
                pre = wifi[i]

        if count < c:  # 공유기를 c대보다 적게 설치함
            high = mid - 1

        elif count >= c:  # 공유기를 c대보다 많이 설치함
            result = mid
            low = mid + 1

    return result


print(BSearch())