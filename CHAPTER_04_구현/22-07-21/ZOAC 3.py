left_li = [['q', 'w', 'e', 'r', 't'], ['a', 's', 'd', 'f', 'g'], ['z', 'x', 'c', 'v']]
right_li = [['y', 'u', 'i', 'o', 'p'], ['h', 'j', 'k', 'l'], ['b', 'n', 'm']]
only_left = ['q', 'w', 'e', 'r', 't', 'a', 's', 'd', 'f', 'g', 'z', 'x', 'c', 'v']
place = {}

for i in range(3):
    j = 0
    for li in left_li[i], right_li[i]:
        for ch in li:
            place[ch] = [i, j]
            j += 1

result = 0
data = input().split()
left_pre, right_pre = place[data[0]], place[data[1]]

for ch in input():
    if ch in only_left:
        result += abs(left_pre[0] - place[ch][0]) + abs(left_pre[1] - place[ch][1])
        left_pre = place[ch]
    else:
        result += abs(right_pre[0] - place[ch][0]) + abs(right_pre[1] - place[ch][1])
        right_pre = place[ch]
    result += 1

print(result)