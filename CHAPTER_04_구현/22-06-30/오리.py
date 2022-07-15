string = input()
dp = [0] * len(string)

order = {'u': 'q', 'a': 'u', 'c': 'a', 'k': 'c'}
q_count = 'q'.count(string)

result = 0
pre = ''

while not q_count:
    for idx in range(len(string)):
        now = string[idx]

        if dp[idx] == 1:
            continue

        if pre == '' and now == 'q':
            q_count -= 1
            dp[idx] = 1
            pre = now

        elif pre == order[now]:  # u, a, c, k
            dp[idx] = 1
            pre = now

            if now == 'k':
                pre = ''