from collections import deque


def solution(queue):
    while queue:
        now_num, count = queue.popleft()

        if now_num == target:
            return count + 1

        elif now_num < target:
            queue.append([now_num * 2, count + 1])
            queue.append([int(str(now_num) + '1'), count + 1])
    return -1


start_num, target = map(int, input().split())
q = deque([[start_num, 0]])
print(solution(q))