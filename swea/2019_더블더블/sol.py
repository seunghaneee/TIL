import sys
sys.stdin = open('input.txt')

num = int(input())
num_list = []
result = 1
while num >= 0:
    num_list.append(result)
    result *= 2
    num -= 1

print(*num_list)
