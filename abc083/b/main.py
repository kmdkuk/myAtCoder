def sum_digits(number=""):
    sum = 0
    for i in range(len(number)):
        sum += int(number[i])
    return sum


N, A, B = input().split()

sum = 0
for i in range(1, int(N) + 1):
    result = sum_digits(str(i))
    if (int(A) <= result and result <= int(B)):
        sum += i

print(sum)
