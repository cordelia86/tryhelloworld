characters = list('abcdef')
print(characters)

print('-' * 20)
words = 'Hello world는 프로그래밍을 배우기에 아주 좋은 사이트 입니다'
words_list = words.split()
print(words_list)

print('-' * 20)
time_str = '10:35:12'
time_list = time_str.split(':')
print(time_list)

print(':'.join(time_list))

print('-' * 20)
# Slice
text = 'Hello World'
# 결과값 ello
print(text[1:5])

print('-' * 20)
list = [0, 1, 2, 3, 4, 5]
# 결과값 [1, 2]
print(list[1:3])
# [2, 3, 4, 5]
print(list[2:len(list)])
# [0, 1]
print(list[:2])
# [2, 3, 4, 5]
print(list[2:])

print('-' * 20)
list1 = [23, 26, 71, 1, 22]
# list1과 list2는 같은 값을 바라봄 -> list1바뀌면 list2도 바뀜
list2 = list1
list1.sort()

print(list1)
print(list2)

print('-' * 20)
# 새로운 리스트로 할당(복사) -> list1 바뀌는것과 별개임
list2 = list1[:]
list1.reverse()
print(list1)
print(list2)

print('-' * 20)


def substring(str, start, end):
    return str[start:end]


str = "Hello world"
between_2_5 = substring(str, 2, 5)
print(between_2_5)
