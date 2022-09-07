import sys
sys.stdin = open('input.txt')

num = int(input())
a_list = []
for i in range(1, num+1):
    if num % i == 0 :
        a_list.append(i)

print(*a_list)