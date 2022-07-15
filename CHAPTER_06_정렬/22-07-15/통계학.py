from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
li = []

for _ in range(n):
    li.append(int(input()))

# 1
# round는 반올림이 아니다.
tmp = float('%.1f' % (sum(li) / n))
if tmp < 0:
    print(int(tmp - 0.5))

else:
    print(int(tmp + 0.5))


# 2
li.sort()
print(li[n // 2])

# 3
tmp = Counter(li).most_common()
if n > 1 and tmp[0][1] == tmp[1][1]:
    print(tmp[1][0])
else:
    print(tmp[0][0])

# 4
print(li[-1] - li[0])