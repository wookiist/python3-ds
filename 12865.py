# 12865 - pypy3로만 가능, 백준 코드도 mem : 225712, time: 8776ms
import sys; input = sys.stdin.readline
N, K = map(int, input().split())
W = [0 for _ in range(N+1)]
V = [0 for _ in range(N+1)]
D = [[0 for _ in range(K+1)] for _ in range(N+1)]
for i in range(1, N+1):
    W[i], V[i] = map(int, input().split())
for i in range(1, N+1):
    for k in range(K+1):
        D[i][k] = D[i-1][k]
        if k-W[i] >= 0:
            D[i][k] = max(D[i][k], V[i]+D[i-1][k-W[i]])
print(max(D[N]))

# n,k = map(int,input().split())
# temp = [list(map(int,input().split())) for _ in range(n)]
# w,v = zip(*temp)
# w = [0] + list(w)
# v = [0] + list(v)
# d = [[0] * (k+1) for _ in range(n+1)]
# for i in range(1, n+1):
#     for j in range(1, k+1):
#         d[i][j] = d[i-1][j]
#         if j-w[i] >= 0:
#             d[i][j] = max(d[i][j],d[i-1][j-w[i]]+v[i])
# print(d[n][k])