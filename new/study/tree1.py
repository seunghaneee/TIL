'''
정점 번호 V: 1 ~ (E+1)
간선 수
부모-자식 순
4
1 2 1 3 3 4 3 5
'''
def find_root(V):
    for i in range(1, V + 1):
        if par[i] == 0:  # 부모가 없으면 root
            return i
# 전위 순회
def preorder(n):
    if n:       # n != 0
        print(n)    #visit(n)
        preorder(ch1[n])
        preorder(ch2[n])

# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)    # visit(n)
        inorder(ch2[n])

# 후위순회
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)    # visit(n)

E = int(input())    # 간선 개수
arr = list(map(int, input().split()))
V = E + 1   # 정점
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

print("왼쪽 자식", ch1)
print("오른쪽 자식", ch2)
preorder(root)
print('='*30)
inorder(root)
print('='*30)
postorder(root)