import sys; input = sys.stdin.readline

N = int(input())
D = [0 for i in range(N+1)]
for i in range(2, N+1):
    temp = 99999999
    if i % 3 == 0:
        if temp > D[i//3]:
            temp = D[i//3]
    if i % 2 == 0:
        if temp > D[i//2]:
            temp = D[i//2]
    if temp > D[i-1]:
        temp = D[i-1]
    D[i] = temp + 1
print(D[N])