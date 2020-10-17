import math as m

X, Y, A, B = map(int, input().split())

now = X
count = 0
is_c = 0
while now < Y:
    is_b = False
    next_a = now * A
    next_b = now + B
    if next_a >= Y and next_b >= Y:
        break
    if next_a-now <= next_b-now and next_a < Y:
        now = next_a
        count += 1
    elif next_b < Y:
        is_b = True
        sa = Y - now
        kai, mod = divmod(sa, B)
        now += (B * kai)
        count += kai
        if mod == 0:
            is_c = 1
        if kai == 0:
            break

print(count - is_c)
