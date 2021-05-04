import sys; input = sys.stdin.readline
n = int(input())
if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    D = [0 for i in range(n+1)]
    D[1] = 1
    D[2] = 3
    for i in range(3, n+1):
        D[i] = (D[i-1] + 2* D[i-2])%10007
    print(D[n])

