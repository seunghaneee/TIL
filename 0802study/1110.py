n = int(input())
n_1 = n
count = 0

while True:
    n_1 = (n_1 % 10) * 10 + (n_1 // 10 + n_1 % 10) % 10
    count +=1
    if (n == n_1):
        break

print(count)

