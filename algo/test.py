n = int(input())
player = []
for i in range(n):
    player.append(input())

possible = []

for i in player:
    p = i[0]
    count = 0
    for j in player:
        p_2 = j[0]
        if p == p_2:
            count += 1
    if count >= 5:
        possible.append(i[0])

possible.sort()
for i in range(1, len(possible)):
    if possible[i] == possible[i-1]:
        possible.pop(i)
print(possible)
# result_list = list(set(possible))
# print(result_list)

if len(result_list):
    result = ''
    for i in result_list:
        result += i

    print(result)
else:
    print('PREDAJA')