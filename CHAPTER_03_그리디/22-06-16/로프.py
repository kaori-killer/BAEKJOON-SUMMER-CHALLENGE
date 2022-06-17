# k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때,
# 각각의 로프에는 모두 고르게 w/k 만큼의 중량

# 3 10 15
# 3*3 10*2 15*1
# 최솟값 * 개수

def solution(n, li):
    li.sort()
    result = 0
    for i in range(n):
        result = max(result, li[i] * (n - i))
    return result


num = int(input())
li = []
for i in range(num):
    li.append(int(input()))
print(solution(num, li))