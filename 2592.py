import sys; input = sys.stdin.readline
feq_map = dict()
avg = 0
for i in range(10):
    x = int(input())
    avg += x
    if x not in feq_map:
        feq_map[x] = 1
    else:
        feq_map[x] += 1
feq = x
for i in feq_map:
    if feq_map[feq] < feq_map[i]:
        feq = i

print(int(avg/10))
print(feq)