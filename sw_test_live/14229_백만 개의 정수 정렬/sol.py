import sys
sys.stdin = open('input.txt')

numbers = list(map(int, input().split()))

numbers.sort()
print(numbers[500000])