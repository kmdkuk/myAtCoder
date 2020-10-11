N = int(input())
a = list(map(int, input().split()))
turn = 0
result = [0, 0]
a.sort()
# print(a)
while(len(a) != 0):
    result[turn] += a.pop()
    turn = (turn+1) % 2
print(result[0] - result[1])
