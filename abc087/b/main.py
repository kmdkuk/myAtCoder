Y500 = int(input())
Y100 = int(input())
Y50 = int(input())
X = int(input())

count = 0
for a in range(Y500+1):
    suma = a * 500
    # print(a)
    if suma > X:
        continue
    for b in range(Y100+1):
        # print(b)
        sumb = suma + b * 100
        if sumb > X:
            continue
        for c in range(Y50+1):
            # print(c)
            sumc = sumb + c * 50
            if sumc > X:
                continue
            if (sumc == X):
                count += 1
print(count)
