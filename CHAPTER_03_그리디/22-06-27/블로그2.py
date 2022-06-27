n = int(input())
string = input()

pre = ""
B_count, R_count = 0, 0

for now in string:
    if now == "B" != pre:
        B_count += 1

    elif now == "R" != pre:
        R_count += 1
    pre = now

if B_count != 0 and R_count != 0:
    print(min(B_count, R_count) + 1)
else:
    print(1)