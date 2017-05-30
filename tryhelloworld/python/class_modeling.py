class Human:
    '''인간'''


def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight

    return person


Human.create = create_human
man = Human.create('Joy', 60.5)


def eat(person):
    person.weight += 0.1
    print('{}가 먹어서 {}kg이 되었습니다.'.format(person.name, person.weight))


def walk(person):
    person.weight -= 0.1
    print('{}가 걸어서 {}kg이 되었습니다.'.format(person.name, person.weight))


Human.eat = eat
Human.walk = walk

man.walk()
man.eat()
man.walk()
