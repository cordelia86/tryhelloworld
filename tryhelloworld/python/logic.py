def return_false():
    print('함수 return_false')
    return False


def return_true():
    print('함수 return_true')
    return True


print('test1')
a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)

print('-' * 20)
print('test2')

if return_false() and return_true():
    print(True)
else:
    print(False)


print('-' * 20)
dic = {"key2": "value2"}

if "key1" in dic and dic["key1"] == "value2":
    print("key1도 있고 그 값은 value2이군")
else:
    print("실패닷")
