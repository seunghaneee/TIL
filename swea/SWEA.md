# SWEA

### [2001_파리퇴치](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PzOCKAigDFAUq&)

```python
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N = 배열 크기, M = 파리채 크기
    N, M = map(int, input().split())
    # 파리 마리수 배열
    array = [list(map(int, input().split())) for _ in range(N)]

    # 합계 중 가장 큰 값을 저장할 result
    result = 0

    # 탐색 범위
    # N = 5, M = 2 일 때 N-M+1번 탐색 해야 한다.
    # -> N-M+1
    for i in range(N-M+1):
        for j in range(N-M+1):

            # 파리채 범위만큼 확인
            total = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    total += array[x][y]
            # print(total)
            if total > result:
                result = total

    print(f'#{tc} {result}')
```



### [1206_View](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&)

```python
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))

    # 조망권이 확보된 총 세대수
    result = 0
    # 현재 위치 기준으로 탐색할 인덱스를 담은 리스트
    search_list = [-2, -1 , 1, 2]
    # 건물 시작 2개와 끝점 2개는 높이가 0이다.
    for i in range(2, N-2):
        # 현재 빌딩 위치를 기준으로 좌우 2개씩 확인
        h_max = 0
        for j in search_list:
            if building[i+j] > h_max:
                h_max = building[i+j]
        
        # 만약 현재 위치의 빌딩 높이가 양옆 2개의 빌딩 중 가장 높은 빌딩보다 높을 때
        # 결과값에 내 높이에서 양 옆 빌딩 중 가장 높은 빌딩의 높이를 뺀 값을 더해준다.
        if building[i] > h_max:
            result += building[i] - h_max
        # 만약 현재 위치의 빌딩 높이가 2칸 이내 빌딩중 최고높이보다 낮다면
        # 조망권을 가진 집이 없다.
        elif building[i] <= h_max:
            result += 0

    print(f'#{tc} {result}')

```

---

### [1208_Flatten](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh)

```python
import sys
sys.stdin = open('input.txt')

T = 11
# 버블 정렬을 활용한 리스트 정렬
def bubble(A):
    for i in range(len(A)-1, 0, -1):
        for j in range(0, i):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]

for tc in range(1, T+1):
    # dump 횟수
    dump = int(input())
    # 박스 높이 리스트
    array = list(map(int, input().split()))

    # 일단 아이디어는 정렬해놓고
    # 제일 높은데에서 제일 낮은데로 옮기기를 dump만큼 반복
    # 다시 정렬하고 반복
    # def 버블정렬 해놓고 쓰자!
    # 덤프 횟수 만큼 반복 혹은 최대 최소값의 차이가 2 미만이면 중지
    # count = 0
    for i in range(dump):
        bubble(array)
        array[-1] -=1
        array[0] += 1
        # count += 1

    bubble(array)
    max_h = array[-1]
    min_h = array[0]

    result = max_h - min_h
    # print(count, dump)
    print(f'#{tc} {result}')
```

---

### [5431_민석이의 과제 체크하기](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWVl3rWKDBYDFAXm)

```python
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 총 수강생수 N / 과제 제출한 사람수 K
    N, K = map(int, input().split())
    # 과제 제출한 사람 번호
    # 모든 수강생 번호는 1~N
    array = list(map(int, input().split()))

    # 과제를 제출하지 않은 사람 번호를 찾고 오름차순 정렬
    C = [0] * (N+1)
    for i in range(1, N+1):
        if i not in array:
            C[i] = i
    list_a = []
    for i in range(len(C)):
        if C[i] != 0:
            list_a.append(i)
    print(f'#{tc}', *list_a)
```

---

### [1970_쉬운 거스름돈](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq)

```python
T = int(input())

for tc in range(1, T+1):
    money = int(input())
    # 돈의 종류가 10, 50, 100, 500, 1000, 5000, 10000, 50000
    # 8개가 있다.
    C = []
    exchange = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for i in exchange:
        if money >= i:
            C.append(money//i)
            money = money % i
        elif money < i:
            C.append(0)
    print(f'#{tc}')
    print(*C)
```

무지성 if문으로 하면 왜 런타임에러가 뜨는지 모르겠다...

---

### [1959_두 개의 숫자열](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpoFaAS4DFAUq&)

```python
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bj = list(map(int, input().split()))


    # 어느 것이 더 길때 조건문을 더 따로 만들지 않기 위해 그냥 bj가 긴걸로 만들기
    if N > M:
        Ai, Bj = Bj, Ai
        N, M = M, N

    result_list = []
    for i in range(M-N+1):
        total = 0
        for j in range(N):
            total += Ai[j] * Bj[i+j]

        result_list.append(total)
    result = result_list[0]
    for i in range(len(result_list)):
        if result_list[i] > result:
            result = result_list[i]

    print(f'#{tc} {result}')
```

---

### [1209_sum](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh)

```python
import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    test_num = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    # 행, 렬, 대각선의 합 중에서 최대값만 출력하기

    # 행 계산
    row_sum_list = []
    for i in range(100):
        total = 0
        for j in range(100):
            total += array[i][j]
        row_sum_list.append(total)
    max_row_sum = row_sum_list[0]
    for i in range(len(row_sum_list)):
        if max_row_sum < row_sum_list[i]:
            max_row_sum = row_sum_list[i]
    # print(max_row_sum)

    # 열 계산
    col_sum_list = []
    for j in range(100):
        total = 0
        for i in range(100):
            total += array[i][j]
        col_sum_list.append(total)
    max_col_sum = col_sum_list[0]
    for i in range(len(col_sum_list)):
        if max_col_sum < col_sum_list[i]:
            max_col_sum = col_sum_list[i]
    # print(max_col_sum)

    # 대각선 계산
    cross_1_list = []
    cross_2_list = []
    total_1, total_2 = 0, 0
    for j in range(100):
        total_1 += array[j][j]
        total_2 += array[j][100-j-1]
    cross_1_list.append(total_1)
    cross_2_list.append(total_2)
    max_cross_1_sum = cross_1_list[0]
    max_cross_2_sum = cross_2_list[0]

    for i in range(len(cross_1_list)):
        if max_cross_1_sum < cross_1_list[i]:
            max_cross_1_sum = cross_1_list[i]

    for i in range(len(cross_2_list)):
        if max_cross_2_sum < cross_2_list[i]:
            max_cross_2_sum = cross_2_list[i]

    result_list = [max_row_sum, max_col_sum, max_cross_1_sum, max_cross_2_sum]

    result = result_list[0]
    for i in range(len(result_list)):
        if result < result_list[i]:
            result = result_list[i]

    print(f'#{test_num} {result}')
```

단순히 최대값의 초기값을 0으로 설정해줬다면 저렇게 리스트 많이 만들고 반복문을 많이 시행할 필요가없지만만약 max값이 음수라면? 그래서 초기값으로 리스트를 만들어 0번째를 지정해주고 각 리스트에서 최대값을 구하였다.

---

### [1210_Ladder1](https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh)

```python
import sys
sys.stdin = open('input.txt')

T = 10
# 좌우상
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for tc in range(1, T+1):
    test_num = int(input())
    array = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    for i in range(100):
        if array[r][i] == 2:
            # 도착 해야 하는 열의 인덱스
            final = i
            break

    # 도착지점에서 시작해서 올라간다.

    # 델타 이용
    idx = 0
    start = array[99][final]
    while r > 0:
        temp_r = r + dx[idx]    # 좌 우 움직임
        temp_c = final + dy[idx]    # 상 하 움직임
        # 범위 밖을 나가지 않게 설정
        if 0 <= temp_r < 100 and 0 <= temp_c < 100:
            if array[temp_r][temp_c] == 1:  # 현재 위치 기준 좌 우 상 확인하여 1이면
                # 내 위치를 1인 위치로 이동시키고
                r = temp_r
                final = temp_c
                # 내가 있던 위치는 숫자를 바꿔줌으로써 무한루프에 들어가지 않게 함
                array[temp_r][temp_c] = -1
        idx = (idx+1) % 4   # 계속 반복

    print(f'#{tc} {final}')

```

사실 좌우상으로만 움직이고 밑으로는 움직이기 않기 때문에 dx, dy를 좌, 우, 상만 설정해줘도 되지만 연습하는 과정이라 그냥 썼다.
델타 배열을 조금 더 공부하자.

---

