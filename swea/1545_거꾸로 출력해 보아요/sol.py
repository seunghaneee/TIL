import sys
sys.stdin = open('SampleInput.txt')

num = int(input())

for i in range(num, -1, -1):
    print(i, end=' ')