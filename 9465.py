import sys; input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    A = list()
    for i in range(2):
        A.append([0]+list(map(int, input().split())))
    D = [[0 for _ in range(N+1)] for _ in range(2)]
    for j in range(1, N+1):
        for i in range(2):
            if j == 1:
                D[i][j] = A[i][j]
                continue
            D[i][j] = max(D[(i-1)*(-1)][j-1], D[(i-1)*(-1)][j-2]) + A[i][j]
    print(max(D[0][N], D[1][N]))