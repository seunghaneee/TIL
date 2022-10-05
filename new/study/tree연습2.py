'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
'''
4
1 2 1 3 3 4 3 5
'''
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i
# 전위 순회
def preorder(n):
    global cnt
    if n:       # n != 0
        print(n, end = ' ')    #visit(n)
        # cnt += 1
        cnt = n
        preorder(ch1[n])
        preorder(ch2[n])

# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n, end = ' ')    # visit(n)
        inorder(ch2[n])

# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n, end = ' ')    # visit(n)

def f(n):           # global cnt 없이 순회한 정점 수를 리턴하는 함수
    if n == 0:      # 서브트리가 비어 있으면 (자식이 없으면)
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1

E = int(input())
arr = list(map(int, input().split()))
V = E + 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)
# 자식을 인덱스로 부모 번호 저장
par = [0] * (V + 1)
for i in range(E):
    # 부모, 자식
    p, c = arr[i*2], arr[i*2+1]
    if ch1[p] == 0:     # 아직 자식이 없으면
        ch1[p] = c      # 자식 1로 저장 (부모 인덱스로)

    else:
        ch2[p] = c
    par[c] = p
root = find_root(V)
# print(root)

# print(ch1)
# print(ch2)
# print("전위순회")
# preorder(root)
# print()
# print('='*30)
# print("중위순회")
# inorder(root)
# print()
# print('='*30)
# print("후위순회")
# postorder(root)
# print()

# 3을 루트로 하는 서브트리에 속한 정점의 개수는?
# cnt = 0
# preorder(3)
# print(cnt)

# 주어진 트리를 root부터 전위/중위/후위 순회하는 경우 각각 마지막 정점은?

# 정점의 개수
print(f(3))