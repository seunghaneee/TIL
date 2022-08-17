# N = int(input())
# A = set(map(int, input().split())) #set형으로 중복값은 제거하여 찾는데 시간 줄임
# M = int(input())
# numbers = list(map(int, input().split()))
#
# for i in numbers:
#     if i in A:
#         print("1")
#     else:
#         print("0")

# 이진 탐색을 이용한 풀이
def binary_search(array, target, start, end):

    if start > end:
        return '0'

    mid = (start + end) // 2
    if array[mid] == target:   #여기서 key는 B집합에서 하나씩 가져와야 한다.
        return '1'
    elif array[mid] > target:  # 찾고자 하는 값이 중앙값보다 작으면
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    print(binary_search(A, i, 0, N-1))
