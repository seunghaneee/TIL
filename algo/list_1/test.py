'''
9
7 4 2 0 0 6 0 7 0
3
2 3 1
'''

N = int(input())
arr = list(map(int, input().split()))

# 가장 큰 수를 찾을 수 있는가
maxV = arr[0]   # 첫번째값을 가장 큰값이라 가정하고 시작
for i in range(1, N):   # 나머지 모든 원소에 대해
    if arr[i] > maxV:
        maxV = arr[i]
print(maxV)
# print(max(arr))

# 각 원소에 대해 오른쪽에 있는 더 작은 원소의 개수 구하기
'''
6
6 3 2 5 3 4
'''
a = int(input())
arr_1 = list(map(int, input().split()))

result = []
for i in range(a):
    count = 0
    for j in range(i+1, a):
        if arr_1[i] > arr_1[j]:
            count += 1
    result.append(count)

print(result)
