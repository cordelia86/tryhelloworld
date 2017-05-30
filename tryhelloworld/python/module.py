import math as math
import random
import my_module

r = 10
print(2 * math.pi * r)

candidates = ['Rock', 'Scissors', 'Paper']
selected = random.choice(candidates)
print(selected)

selected = my_module.random_rsp()
print(selected)
print('가위 ? ', my_module.SCISSOR == selected)

