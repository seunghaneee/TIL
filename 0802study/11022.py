n = int(input())
list_1 = []
list_2 = []
list_3 = []
while n > 0:
    A, B = map(int, input().split())
    list_1.append(A + B)
    list_2.append(A)
    list_3.append(B)
    n -=1
for i in range(len(list_1)):
    print(f'Case #{i+1}: {list_2[i]} + {list_3[i]} = {list_1[i]}')