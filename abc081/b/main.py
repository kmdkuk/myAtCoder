def checkEven(arr=[]):
    for i in arr:
        if (i % 2 != 0):
            return False
    return True


n = int(input())
a = list(map(int, input().split()))
count = 0

while (checkEven(a)):
    for i in range(len(a)):
        a[i] = int(a[i] / 2)
    count += 1
print(count)
