import heapq


def solution():
    dic = {'q': [], 'u': [], 'a': [], 'c': [], 'k': []}

    string = input()
    result = 0

    for i in range(len(string)):
        heapq.heappush(dic[string[i]], i)

    for key in dic:
        if key == 'q':
            pre = heapq.heappop(dic[key])

        check = True
        now = heapq.heappop(dic[key])
        while pre < now:
            now = heapq.heappop(dic[key])

            if not dic[key]:
                check = False
                return result

        if check:
            if key == 'k':
                result += 1
            pre = now