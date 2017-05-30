numbers1 = list(range(10))
print(numbers1)

characters = list('hello')
print(characters)

print(isinstance(characters, list))

print(type(numbers1) == type(characters))
print(numbers1 is numbers1)

list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list1:
    print("당연히 list1과 list1은 같은 인스턴스입니다.")

if list1 == list2:
    print("list1과 list2의 값은 같습니다.")
    if list1 is list2:
        print("그리고 list1과 list2는 같은 인스턴스입니다.")
    else:
        print("하지만 list1과 list2는 다른 인스턴스입니다.")

# 당연히 list1과 list1은 같은 인스턴스입니다.
# list1과 list2의 값은 같습니다.
# 하지만 list1과 list2는 다른 인스턴스입니다.
# 'is'는 인스턴스 비교, '=='은 값 비교

if isinstance(list1, list) and isinstance(list2, list):
    print("list1과 list2는 둘 다 list 클래스 입니다.")

# list1과 list2는 둘 다 list 클래스 입니다.
