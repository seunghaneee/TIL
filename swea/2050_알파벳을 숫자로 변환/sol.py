import sys
sys.stdin = open('input.txt')

s = input()

for i in s:
    print(ord(i)-64, end=' ')