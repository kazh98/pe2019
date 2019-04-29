x = input().split()
a, b, c = int(x[0]), int(x[1]), int(x[2])

count = 0
for i in range(a, b + 1):
    if c % i == 0:
        count += 1
print(count)
