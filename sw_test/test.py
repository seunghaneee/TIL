# a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21,22,23,24,25]]

# for i in range(len(a)):
#     for j in range(len(a)):
        # 행 우선 조회
        # print(a[i][j])
        # 열 우선 조회
        # print(a[j][i])

# 지그재그 순회

for x in range(len(a)):
    for y in range(len(a)):
        if x % 2 == 0:
            print(a[x][y])
        elif x % 2 != 0:
            print(a[x][len(a)-1-y])