# from my_package import my_module,my_module1
# my_module.fun1()
# my_module1.fun2()
# from my_package.hello import say_by,say_hi
# say_hi()
# say_by()
import random
import string
print("Generate a random color hex:")
print("#{:06x}".format(random.randint(0, 0xFFFFFF)))
print("\nGenerate a random alphabetical string:")
max_length = 255
s = ""
for i in range(random.randint(1, max_length)):
    s = s+ random.choice(string.ascii_letters)
print(s)
print("Generate a random value between two integers, inclusive:")
print(random.randint(0, 10))
print(random.randint(-7, 7))
print(random.randint(1, 1))
print("Generate a random multiple of 7 between 0 and 70:")
print(random.randint(0, 10) * 7)
