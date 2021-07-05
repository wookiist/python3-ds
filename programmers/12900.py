# 2xn 타일링 / 12900.py
def solution(n):
    answer = 0
    D = [0 for _ in range(n+1)]
    D[0] = 1
    D[1] = 1
    for i in range(2,n+1):
        D[i] = (D[i-1] + D[i-2])%1000000007
    return D[n]