import sys

n = int(input())
list_1 = []
result = 0
while n != 0:
    A, B = map(int, sys.stdin.readline().split())
    result = A + B
    list_1.append(result)
    n -=1
    result = 0

for i in list_1:
    print(i)