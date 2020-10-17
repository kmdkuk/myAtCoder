def power(x):
    return pow(x, 2)


N = int(input())
X = list(map(int, input().split()))

abs_x = map(abs, X)
pow_x = map(power, X)

print(sum(abs_x))
print(pow(sum(pow_x), 0.5))
print(max(map(abs, X)))
