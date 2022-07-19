def solution():
    result = 0

    for a in range(5):
        string = input().split()
        for b in range(5):
            count = 0
            result += 1
            a, b = place[string[b]][0], place[string[b]][1]
            check[a][b] = 0

            # 가로 빙고
            for i in range(5):
                if sum(check[i]) == 0:
                    count += 1

                # 세로 빙고
                tmp = 0
                for j in range(5):
                    tmp += check[j][i]
                if tmp == 0:
                    count += 1

            # 대각선 빙고
            tmp_l = 0
            tmp_r = 0

            for i in range(5):
                tmp_l += check[i][i]
                tmp_r += check[i][4 - i]

            if tmp_l == 0:
                count += 1

            if tmp_r == 0:
                count += 1

            if count > 2:
                return result


check = [[1] * 5 for _ in range(5)]
place = {}

for i in range(5):
    string = input().split()
    for j in range(5):
        place[string[j]] = [i, j]

print(solution())