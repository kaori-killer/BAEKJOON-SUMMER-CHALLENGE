# 0 .식은 ‘0’~‘9’, ‘+’, 그리고 ‘-’
# 1. 가장 처음과 마지막 문자는 숫자이다.
# 2. 연속해서 두 개 이상의 연산자가 나타나지 않는다.
# 3. 5자리보다 많이 연속되는 숫자는 없다.
# 4. 수는 0으로 시작할 수 있다.
# 5. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

# 우선순위 + > -
express = input().split("-")
for idx in range(len(express)):
    tmp = sum(map(int, express[idx].split("+")))

    if idx == 0:
        result = int(tmp)
    else:
        result -= tmp

print(result)