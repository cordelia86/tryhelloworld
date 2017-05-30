list = [1, 2, 3, 4, 5]
ages = {'Tod': 35, 'Jane': 23, 'Paul': 62}

for i, v in enumerate(list):
    print('{}번째 값 : {}'.format(i, v))

print('-' * 20)

for a in enumerate(list):
    print('{}번째 값 : {}'.format(a[0], a[1]))

print('-' * 20)

# *a -> tuple 'a'를 쪼개라
for a in enumerate(list):
    print('{}번째 값 : {}'.format(*a))

print('-' * 20)

for key, val in ages.items():
    print('{}의 나이는 : {}'.format(key, val))


print('-' * 20)

for a in ages.items():
    print('{}의 나이는 : {}'.format(a[0], a[1]))


print('-' * 20)

for a in ages.items():
    print('{}의 나이는 : {}'.format(*a))