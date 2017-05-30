wintable = {
    '가위': '보',
    '바위': '가위',
    '보': '바위'
}


def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'


messages = {
    'draw': '비겼네..까비',
    'win': '이겼다!!!!^0^',
    'lose': '졌다-_ㅠ 저주받은 손가락'
}

result = messages[rsp('가위', '보')]
print(result)

list = [1, 2, 3, 4, 5]
dict = {
    'one': 1,
    'two': 2
}

list.append(6)
"""del list[0]"""
''' pop을 하게 되면 삭제되는 값을 return'''
print(list.pop(0))
print(list)

dict['three'] = 3
dict['four'] = 4
del (dict['one'])
print(dict)

# dictionary는 저장 순서 상관없이 출력함
# 순서가 중요한 경우 List 사용하기
ages = {'Tod': 35, 'Jane': 23, 'Paul': 62}

for key, value in ages.items():
    print('{}의 나이는 {} 입니다'.format(key, value))
