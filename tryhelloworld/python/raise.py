def rsp(mine, yours):
    allowed = ['가위', '바위', '보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError


try:
    rsp('가위', '바')
except ValueError:
    print('잘못된 값을 넣은것 같습니다')

school = {'1반': [172, 185, 198, 177, 165, 199], '2반': [165, 177, 167, 180, 191]}

try:
    for class_number, students in school.items():
        for student in students:
            if student > 190:
                # Exception 발생시킴으로 모든 for문 종료
                raise StopIteration
except StopIteration:
    print('{}에 190을 넘는 학생이 있습니다'.format(class_number))

shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

try:
    for shop, products in shops.items():
        for product, price in products.items():
            if product == '풀':
                raise StopIteration
except StopIteration:
    print("{}: {}원".format(shop, price))
