a, b, c = map(int, input().split())
result = 0
if a == b == c:
    result = 10000 + int(a)*1000
    print(result)
elif a == b and a != c:
    result = 1000+int(a)*100
    print(result)
elif a !=b and b == c:
    result = 1000+int(b)*100
    print(result)
elif a == c and b != c:
    result = 1000 + int(a)*100
    print(result)
elif a != b != c:
    if a >= b and a >= c:
        result = a * 100
        print(result)
    elif b >= a and b >= c:
        result = b * 100
        print(result)
    elif c >= a and c >= b:
        result = c * 100
        print(result)
    