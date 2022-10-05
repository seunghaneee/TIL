a = 0
b = 1
n = 20

for _ in range(n-1):
    a, b = b, a + b

print(b)