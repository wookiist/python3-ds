import sys; input = sys.stdin.readline
N = int(input())
A = [int(x) for x in input().split()]
D = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            D[i] = max(D[i], D[j] + 1)
print(max(D)) 