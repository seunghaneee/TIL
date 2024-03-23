import random

random_list = random.sample(range(1, 101), 10)
print(random_list)
# 버블 정렬

for i in range(len(random_list)):
    for j in range(len(random_list) - i - 1):
        if random_list[j] > random_list[j + 1]:
            random_list[j], random_list[j + 1] = random_list[j + 1], random_list[j]

print(random_list)
