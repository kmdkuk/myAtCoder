A, B, C, D = map(int, input().split())
is_equal = False
for i in range(16):
    sum = 0
    left = 0
    is_a = i & 0b1000
    is_b = i & 0b0100
    is_c = i & 0b0010
    is_d = i & 0b0001
    if (is_a != 0):
        sum += A
    else:
        left += A
    if (is_b != 0):
        sum += B
    else:
        left += B
    if (is_c != 0):
        sum += C
    else:
        left += C
    if (is_d != 0):
        sum += D
    else:
        left += D
    if (sum == left):
        is_equal = True

if (is_equal):
    print("Yes")
else:
    print("No")
