list = [1, 2, 3, 5, 7, 2, 5, 237, 55]

for val in list:
    if val % 3 == 0:
        print(val)
        break

print('-'*20)

for i in range(len(list)):
    if i % 2 == 0:
        continue
    print(i)

