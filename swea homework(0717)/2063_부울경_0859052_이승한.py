n=int(input())

values=list(map(int,input().split()))
values.sort()
index_number=(n-1)//2
print("{}".format(values[index_number]))