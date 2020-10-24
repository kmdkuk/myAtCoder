N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if (M != 0):
    cd = [list(map(int, input().split())) for _ in range(M)]
else:
    cd = list(list())

i = 0
while i < M:
    diff = b[i] - a[i]
    a[i] += diff
    # cd[0]にiがあるか
    c = [c for c in cd if c[0] == i + 1]
    if (len(c) != 0):
        a[c[0][1]-1] -= diff
    i += 1
if (a == b):
    print('Yes')
else:
    print('No')
