from collections import deque

q = deque([])
u = deque([])
a = deque([])
c = deque([])
k = deque([])

string = input()
for i in range(len(string)):
    if string[i] == 'q':
        q.append(i)

    elif string[i] == 'u':
        u.append(i)

    elif string[i] == 'a':
        a.append(i)

    elif string[i] == 'c':
        c.append(i)

    else:  # k
        k.append(i)


def check(pre, now_li):
    if not now_li:
        return False

    now = now_li.popleft()

    if pre < now:
        return now
    else:
        return False


def solution(count, last):
    for i in range(len(q)):
        pre = q.popleft()
        first = pre

        pre = check(pre, u)
        if not pre:
            return -1

        pre = check(pre, a)
        if not pre:
            return -1

        pre = check(pre, c)
        if not pre:
            return -1

        pre = check(pre, k)
        if not pre:
            return -1

        if i == 0:
            last = pre

        if first < last:
            count += 1

    return count


result = solution(0, 1e9)
if result == 0:
    print(-1)
else:
    print(result)