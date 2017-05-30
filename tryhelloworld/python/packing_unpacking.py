a, b = 1, 2

print(a, type(a))

c = (3, 4)
# c의 내용을 unpacking
d, e = c
print(d, e)

# d, e의 값을 packing
f = d, e
print(f)

x = 5
y = 10

x, y = y, x
print(x, y)


def tuple_func():
    return 1, 2


q, w = tuple_func()
print(q, w)