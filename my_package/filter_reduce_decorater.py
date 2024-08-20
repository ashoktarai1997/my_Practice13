#filter
# li=[10,20,35,45,65,78,81,93]
# var=list(filter(lambda n:n%5==0,li))
# print(var)
# def is_even(num):
#      return num % 2 == 0
#
# numbers = [10,13,16,19,22,25,28,31]
# filtered_number=filter(is_even,numbers)
# filtered_number_list=list(filtered_number)
# print(filtered_number_list)

#map
# li=[20,35,39,43,48,59,55]
# var=list(map(lambda n:n+5,li))
# print(var)
# def square(num):
#     return num**3
# number=[2,3,4,5,6]
# square_num=map(square,number)
# square_num_list=list(square_num)
# print(square_num_list)
#
# numbers1 = [10, 12, 13]
# numbers2 = [14, 15, 16]
# summed_numbers = map(lambda a, b: a * a, numbers1, numbers2)
# summed_numbers_list = list(summed_numbers)
# print(summed_numbers_list)


#reduce
# from functools import reduce
# li=[12,35,63,54,59,71,29,51]
# var=reduce(lambda a,b:a+b,li)
# print(var)
#
# from functools import reduce
# def multiply(x, y):
#     return x * y
# numbers = [1, 2, 3, 4, 5]
# product = reduce(multiply, numbers)
# print(product)
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# product_with_initializer = reduce(lambda x, y: x * y, numbers, 10)
# print(product_with_initializer)

#decorator

# def decore1(cal):
#     def mul(a,b):
#         result = a*b
#         return result,cal(a,b)
#     return mul
#
# def decore(cal):
#     def sub(a,b):
#         result = a-b
#         return result,cal(a,b)
#     return sub
# @decore
# @decore1
# def cal(a,b):
#     add = a+b
#     return add
#
# print(cal(10,20))

'''def decore(string_length_count):
    def reverse_string(st):
        rev = ''
        for i in st:
            rev = i+rev
        return rev,string_length_count(st)

    return reverse_string


@decore
def string_length_count(st):
    var = len(st)
    return var

print(string_length_count('qwerty'))'''
# def decore(div):
#     def mod(a,b):
#         result=a+b
#         return result,div(a,b)
#     return mod
# def cal(div):
#     def mul(a,b):
#         result=a*b
#         return result,div(a,b)
#     return mul
# @decore
# @cal
# def kal(a,b):
#     div=a/b
#     return div
# print(kal(2,50))
def even_odd_decorator(func):
    """Decorator to check if the number is even or odd before calling the function."""
    def wrapper(n):
        if n % 2 == 0:
            print(f"{n} is even")
        else:
            print(f"{n} is odd")
        return func(n)
    return wrapper
@even_odd_decorator
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
num = 9
result = is_prime(num)
print(f"Is {num} a prime number? {'Yes' if result else 'No'}")

