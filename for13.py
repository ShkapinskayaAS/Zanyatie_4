N = int(input())

total = 0

for i in range(1, N):
    if i % 2 != 0:
        total += 1 + i / 10
    else:
        total -= 1 + i / 10
    print(1 + i / 10, total)

print(total)