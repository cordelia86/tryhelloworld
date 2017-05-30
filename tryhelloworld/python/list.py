list1 = [1, 2, 3]
# extend를 쓰면 +로 merge하는 것 보다 성능이 더 좋다
list1.extend([4, 5, 6])
print(list1)

# 2번째 인덱스에 값 추가
list1.insert(2, 999)
print(list1)

# 뒤에서 두번째 인덱스에 값 추가
list1.insert(-1, -1)
print(list1)

# index에서 벗어난 범위의 인덱스에 추가를 해도 에러 안남. 마지막 인덱스에 값이 추가된다
list1.insert(10000, 10000)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)