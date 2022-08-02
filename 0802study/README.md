# 백준 단계별 풀기 (반복문) -220802

### 2739 구구단

구구단 출력

```python
n = int(input())

for i in range(1,10):
    print(f'{n} * {i} = {n*i}')
```

- 구구단 하고자 하는 단수 n을 입력 받아 range로 1~9 까지 곱한 값을 f -string을 이용해 출력

---

### 10950 A+B -3

A+B 출력

```py
n = int(input())
while n != 0:
    A, B = map(int, input().split())
    print(A + B)
    n -=1
```

- 이렇게 풀면 두 수를 입력함과 동시에 결과가 출력된다. 이렇게 해도 성공이라고 뜨지만 예제 출력처럼 한번에 뜨게 하고 싶었다 그렇게 하기 위해선 리스트를 사용해서 합을 저장해놓고 마지막에 출력해야 할 것 같다는 생각을 했다.

  ```python
  n = int(input())
  list_1 = []
  result = 0
  while n != 0:
      A, B = map(int, input().split())
      result = A + B
      list_1.append(result)
      n -=1
      result = 0
  
  for i in list_1:
      print(i)
  ```

  결과값을 담을 리스트 list_1과 result를 선언하고 result 값을 list_1에 .append 해준다. 그렇게 하고 난 뒤 n을 감소 시키고 result도 0으로 초기화 해준다. while 반복문이 끝난 뒤 list_1에 담긴 결과값을 for 반복문을 이용해 출력한다.

---

### 8393 1~n 까지 합

```python
n = int(input())
result = 0
while n > 0:
    result += n
    n -=1
print(result)
```

result에 n부터 1씩 줄여나가며 더해준다.

---

### 15552 A + B

```python
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
```

A, B를 input()이 아닌 sys를 이용하여 입력받는다.(이렇게 해야 시간초과 오류가 안난다...)

---

### 2741 N찍기

```python
n = int(input())
for i in range(1, n+1):
    print(i)
```

1부터 N 까지 출력

---

### 2742 기찍 N

```python
n = int(input())
for i in range(n, 0, -1):
    print(i)
```

N부터 1까지 출력

---

### 11021 A+B -7

```python
n = int(input())
list_1 = []
while n > 0:
    A, B = map(int, input().split())
    list_1.append(A + B)
    n -=1
for i in range(len(list_1)):
    print(f'Case #{i+1}: {list_1[i]}')
```

앞선 A+B와 유사하지만 Case #순서 가 들어가야 한다. 따라서 f-string을 사용하여 순서를 출력하고, list_1의 값을 인덱싱을 이용하여 출력한다.

---

### 11022 A+B -8

```python
n = int(input())
list_1 = []
list_2 = []
list_3 = []
while n > 0:
    A, B = map(int, input().split())
    list_1.append(A + B)
    list_2.append(A)
    list_3.append(B)
    n -=1
for i in range(len(list_1)):
    print(f'Case #{i+1}: {list_2[i]} + {list_3[i]} = {list_1[i]}')
```

위 문제에서 A와 B도 리스트에 추가하여 같이 출력해주면 된다.

---

### 2438 별찍기

```python
n = int(input())

for i in range(1, n+1):
    print('*' * i)
```

---

### 2439 별찍기 -2

```python
n = int(input())

for i in range(1, n+1):
    print(' ' * (n-i) + '*' * i)
```

위 문제에서 별 거꾸로 찍기

---

### 10871 X보다 작은 수

```python
N, X = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < X:
        print(i, end=' ') 
```

N은 a의 갯수이며 a를 리스트로 받아 x와 비교하여 x보다 값이 작으면 출력하되, 가로로 출력되도록 end=' '을 이용하였다.

---

### 10952 A+B -5

```python
list_1 = []
while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    list_1.append(A + B)

for i in list_1:
    print(i)
```

A와 B가 둘 다 0이라면 반복문을 종료하고 아니라면 계속 A+B를 list_1에 추가하여 0 0이 입력 될 때 리스트값을 출력

---

### 10951 A+B -4

```python
while True:
    try:
        A, B = map(int, input().split())
    except:
        break
    print(A+B)
```

try-except 구문 사용 try 구문을 이용하여 에러가 발생할 여지가 있는 문장을 작성하고

except 구문에서 에러가 발생 시 실행할 문장을 작성하여 실행한다.

---

### 1110 더하기 사이클

```python
n = int(input())
n_1 = n
count = 0

while True:
    n_1 = (n_1 % 10) * 10 + (n_1 // 10 + n_1 % 10) % 10
    count +=1
    if (n == n_1):
        break

print(count)
```

n_1은 입력받은 숫자와 비교하기 위해 변수 설정을 해주고 n_1은 나머지의 10을 곱해주면 10의자리수가 되고 일의 자리 부분은 각 자리수 합을 10을 나눈 값이다. 이러한 과정을 반복하면 count가 증가하고 만약 반복하다가 입력받은 수와 같아지면 반복문을 나와 count를 출력한다.