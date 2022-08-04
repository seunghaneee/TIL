n = int(input())
list_1 = []
while n > 0:
    A, B = map(int, input().split())
    list_1.append(A + B)
    n -=1
for i in range(len(list_1)):
    print(f'Case #{i+1}: {list_1[i]}')