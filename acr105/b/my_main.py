N = int(input())
a = list(set(map(int, input().split())))
a.sort()
while (a[0] != a[len(a) - 1]):
    # print(a[0])
    index = len(a) - 1
    max = a[index]
    while (a[index] == max):
        index -= 1
    max2 = a[index]
    a = a[: index + 1]
    if (len(a) == 1):
        break
    index2 = 1
    while (a[index2] - a[0] < a[0]):
        index2 += 1
    for i in range(index2, len(a)):
        diff = a[i] - a[0]
        if (diff % a[0] == 0):
            continue
        a[i] = a[i] - (a[0] * (int(diff/a[0])+1))
    diff = max - max2
    if (a[0] == 1):
        break
    if (diff % a[0] == 0):
        break
    a.append(max - (a[0] * (int(diff/a[0])+1)))
    a.sort()

print(a[0])
