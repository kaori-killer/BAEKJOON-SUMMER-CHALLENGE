# 1. 10^N = N + 1개의 M
# 2. 5 x (10^N) = N개의 M뒤에 1개의 K

# 최대값 우선순위: 2 -> 1
# 최솟값 우선순위: 1 -> 2

# 주의 예제: MMM (최대: 111, 최소: 100)

string = input()
count = 0
max_result = ''
min_result = ''

for ch in string:
    if ch == "K":

        max_result += str(5 * 10 ** count)

        if count == 0:
            min_result += '5'
        else:
            min_result += str(10 ** (count - 1)) + '5'
        count = 0
    else:
        count += 1

if count:
    max_result += '1' * count
    min_result += str(10 ** (count - 1))

print(max_result)
print(min_result)