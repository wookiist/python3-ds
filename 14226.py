from collections import deque
S = int(input())
D = [[100_000_000 for _ in range(1001)] for _ in range(1001)]
q = deque([(1, 0)])
D[1][0] = 0
while q:
    nx, nc = q.popleft()
    if nx == S:
        break
    # save
    if nx <= 1000 and D[nx][nx] == 100_000_000:
        q.append((nx, nx))
        D[nx][nx] = D[nx][nc] + 1
    # paste
    if nx+nc <= 1000 and D[nx+nc][nc] == 100_000_000:
        q.append((nx+nc, nc))
        D[nx+nc][nc] = D[nx][nc] + 1
    # 1 delete
    if nx-1 >= 0 and D[nx-1][nc] == 100_000_000:
        q.append((nx-1, nc))
        D[nx-1][nc] = D[nx][nc] + 1

print(min(D[S]))