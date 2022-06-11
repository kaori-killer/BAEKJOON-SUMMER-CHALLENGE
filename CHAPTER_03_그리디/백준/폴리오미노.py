# 첫째 줄에 사전순으로 가장 앞서는 답을 출력한다,
# 만약 덮을 수 없으면 -1을 출력한다.

def solution():
    string = input().split(".")

    for idx, board in enumerate(string):
        tmp = ''
        length = len(board)

        while length:
            if length < 0:
                return -1

            elif length % 4 == 0:
                tmp += "AAAA" * (length // 4)
                length = 0
            else:
                tmp += "BB"
                length -= 2

        string[idx] = tmp[::-1]

    result = ".".join(string)
    return result


print(solution())