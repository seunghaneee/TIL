list_1 = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    list_1.append(A + B)

for i in list_1:
    print(i)