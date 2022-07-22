def sym_switch(left_idx, right_idx):
    if left_idx < 1 or n < right_idx or (li[left_idx] != li[right_idx]):
        return

    else:
        val = 0 if li[left_idx] else 1
        li[left_idx], li[right_idx] = val, val
        sym_switch(left_idx-1, right_idx+1)


n = int(input())
li = [None] + list(map(int, input().split()))
m = int(input())

for _ in range(m):
    gender, now_idx = map(int, input().split())

    if gender == 1:  # 남학생
        for idx in range(now_idx, n + 1, now_idx):
            li[idx] = 0 if li[idx] else 1
    else:  # 여학생
        li[now_idx] = 0 if li[now_idx] else 1
        sym_switch(now_idx-1, now_idx+1)

for k in range(n + 1):
    if k == 0:
        continue

    print(li[k], end=" ")
    if k % 20 == 0:
        print()
