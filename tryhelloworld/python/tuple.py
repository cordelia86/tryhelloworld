# Tuple은 수정할 수 없는 순서있는 값을 저장
tuple1 = (1, 2, 3)
print(tuple1)

type(tuple1)
print(type(tuple1))

list1 = [1, 2, 3]
tuple2 = tuple(list1)
print(tuple2)

"""tuple2[0] = 5
print(tuple2)"""

for index in range(len(tuple2)):
    print(tuple1[index])
