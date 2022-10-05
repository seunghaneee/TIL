def f(i, N):
    if i == N:      # 순열 완성
        print(p)
    else:
        for j in range(i, N):   #p[i]에 들어갈 숫자 p[j] 결정
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            p[i], p[j] = p[j], p[i] # 원상복구




p = [1, 2, 3]
f(0, 3) # 0번칸부터 값을 결정하고 총 3개