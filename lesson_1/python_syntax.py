
a = 1
b = "string"
print(f"fsf {a}")

_intiger = 1
_bool = True or False
_string = "String"
_float = 10.5

_list = [1, 2, "three", 4.5]
_list[0] = "one"

_tuple = (1, "two", 3.0, False)

_dict = {
    "key": "value",
    "key2": "value1",
}
_dict2 = dict(
    one = "value",
    two = 12
    )

_dict["key"]

if ("condition"):
    print("inside condition")

if (1 == 2):
    print("error")

if 1 == 2 or 2 == 3 and 3 == 4:
    print("error")

if (((1 == 2) or 2 == 3) and 3 == 4):
    print("error")

if (True):
    pass
else:
    pass

if (True):
    pass
elif(False):
    pass
else:
    pass

if (1):
    pass
else:
    a = 2

for i in range(1,9):
    print(i)

while True:
    print("asdad")
    if 1 == 2:
        break
    else:
        continue

_list = [1, 2, 3, 4]
for item in _list:
    print(item)


_dict = {
    "key": "value",
    "key2": "value1",
}

for key in _dict.keys():
    print(key)
    print(_dict[key])

for key, value in _dict.items():
    print(key)
    print(value)

def my_function():
    pass

my_function()

def my_function(arg):
    print(arg)

my_function(1)
# my_function(1, 2)

def my_function(value: int, value2: int) -> int:
    return value + 1

my_function(1, 2)
# my_function(1)

def my_function(value, value2 = None):
    return value + 1

my_function(1, 2)
my_function(value2 = 1, value = 2)
my_function(1)

def my_function(*args):
    pass

my_function(1, 2, 3, 4)

def my_function(**kwargs):
    pass

my_function(key="value", key1="value2")


def my_difficult_function(arg1, arg2, *args, **kwargs):
    pass


class MyClass:

    pass

class OtherClass(MyClass):

    pass


class AnotherClass(OtherClass, dict):

    class Meta:
        abstract = True

class Animal:

    name = None    

    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello {self.name}")

    def __str__(self) -> str:
        return self.name

animal = Animal("kuku")    

animal.hello()


my_list = [1, 2, 3, 4]
my_list[1:3]
my_list[1:1:1]
my_list[:1]
my_list[1:]
my_list[::-1]
my_list[:-3]


