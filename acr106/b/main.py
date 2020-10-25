import itertools

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
if (M != 0):
    cd = [list(map(int, input().split())) for _ in range(M)]
else:
    cd = list(list())

groups = list(list())
for i in range(1, N + 1):
    conn_list = [item for item in cd if item[0] == i or item[1] == i]
    if (len(conn_list) == 0):
        conn_list.append([i])
    conn_list = list(set(itertools.chain.from_iterable(conn_list)))
    indexes = [index for index, group in enumerate(
        groups) if not set(conn_list).isdisjoint(set(group))]
    if len(indexes) == 0:
        groups.append([i])
        indexes = [index for index, group in enumerate(
            groups) if not set(conn_list).isdisjoint(set(group))]
    if (len(indexes) > 1):
        for j in range(len(indexes) - 1, 0, -1):
            groups[indexes[0]].extend(groups[indexes[j]])
            groups[indexes[0]] = list(set(groups[indexes[0]]))
            del groups[indexes[j]]
    for item in conn_list:
        groups[indexes[0]].append(item)
        groups[indexes[0]] = list(set(groups[indexes[0]]))

flag = True
for group in groups:
    sum_a = sum([item for index, item in enumerate(a) if index+1 in group])
    sum_b = sum([item for index, item in enumerate(b) if index+1 in group])
    if sum_a != sum_b:
        flag = False
        break

if (flag):
    print('Yes')
else:
    print('No')
