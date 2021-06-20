import sys; input = sys.stdin.readline
n = int(input())
A = [0] + [int(x) for x in input().split()]
D = [0 for _ in range(n+1)]
for i in range(1, n+1):
    if D[i-1] + A[i] > A[i]:
        D[i] = D[i-1] + A[i]
    else:
        D[i] = A[i]
print(max(D[1:]))
 