n = int(input())
a = input().split()

for i in range(n):
    print(a[n - i - 1], end="")
    if i < n - 1:
        print(" ", end="")
print()
