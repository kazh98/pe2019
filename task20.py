import itertools

while True:
    c = input().split()
    n, x = int(c[0]), int(c[1])
    if n == x == 0:
        break
    count = 0
    for i, j, k in itertools.combinations(range(1, n + 1), 3):
        if i + j + k == x:
            count += 1
    print(count)
