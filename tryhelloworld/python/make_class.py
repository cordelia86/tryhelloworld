class Human():
    print('나는 사람이다')


person1 = Human()
person2 = Human()

person1.language = '한국어'
person2.language = 'English'

person1.name = '이보람'
person2.name = 'Catherine'


def speak(person):
    print('{}이 {}로 말을 합니다.'.format(person.name, person.language))


Human.speak = speak

person1.speak()
person2.speak()
