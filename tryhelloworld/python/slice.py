""" slice_step """

list1 = list(range(20))
print(list1)

# 0 ~ 끝까지 2 차이
print(list1[::2])
print(list1[5:15])
# 5 인덱스부터 15인덱스까지 3차이
print(list1[5:15:3])
# 15 인덱스부터 5인덱스까지 -1차이
print(list1[15:5:-1])
print(list1[::-3])

print('--' * 10)
# slice_list_modify

numbers = list(range(10))
print('Original numbers : ', numbers)
del numbers[:5]
print('del numbers[:5] : ', numbers)

print('numbers[1:3] : ', numbers[1:3])
numbers[1:3] = 66, 77
print('numbers[1:3] = 66, 77 : ', numbers)
numbers[1:3] = 66, 77, 88
print('numbers[1:3] = 66, 77, 88 : ', numbers)
numbers[1:4] = [0]
print('numbers[1:4] = [0] : ',numbers)
