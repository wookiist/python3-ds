# 43162 깊이/너비 우선 탐색(DFS/BFS) > 네트워크

from collections import deque

def solution(n, computers):
    answer = 0
    G = dict()
    for idx, computer in enumerate(computers):
        G[idx] = list()
        for jdx, node in enumerate(computer):
            if node != 0 and jdx != idx:
                G[idx].append(jdx)
    check = [False for _ in range(n)]

    q = deque()
    for i in range(n):
        if not check[i]:
            q.append(i)
            check[i] = True
            answer += 1
            while q:
                nx = q.popleft()
                for k in G[nx]:
                    if not check[k]:
                        q.append(k)
                        check[k] = True
    return answer
