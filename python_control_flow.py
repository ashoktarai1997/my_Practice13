'''how to get input from end user'''
#input
'''var=list(input('enter your name:-'))
print(type(var))'''
                         #dict
# dt={'name':'ashok','age':26,'city':'brahmapur'}
# print(dt['name'])
# var=dt.keys()
# print(var)
# var1=dt.values()
# print(var1)
# var2=dt.items()
# print(var2)
# print(var)
# dt['name']='cs'
# print(dt)
# var4=dt.get('age')
# print('you enter age is:',var4)
'''user_input = eval(input("Enter something: "))
print("You entered:", user_input)
print(type(user_input))'''
# a=1100
# b=2200
# c=3300
# age=int(input('enter the age: '))
# print(type(age))
# if age<15 or age>60:
#     print('not allowed in pub')
# elif age>=15 and age<25:
#     print(f'ticket prrice for those: {a}')
# elif age>=25 and age<45:
#     print(f'ticket price for those:{b}')
# elif age>=45 and age<60:
#     print(f'ticket priice for those:{c}')
# else:
#     print ('old man and child are not allowed')
'''a=int(input('enter a number:='))
if a%2==0:
    print('the number is even')
else:
    print('the number is odd')'''
'''a=input('enter your name:=m')
if a==a[::-1]:
    print('pallindrom')
else:
    print('not pallindrom')'''
# num=int(input('enter a number:='))
# if num%2==0 and  num%3==0:
#     print('T')
# else:
#     print('F')
'''li=[[1,2],[3,4],[5,6],(8,9)]
for i in li:
    for j in li:
        print(j)'''
'''li=[1,2,[3,4]]
for i in li :
    if type(i)==list:
        for j in li :
            print(j)
        else:
            print(i)'''
'''li=[1,2,(89,90),7,8,[91,92]]
for i in li:
    if type(i)==tuple or type(i)==list:
        for j in i:
            print(j)
        else:
            print(i)'''
'''check even or odd number'''
# li = [10,24,31,43,66,87,89,21,26,90]
# even_li=[]
# odd_li=[]
# for i in li:
#     if i%2==0:
#         even_li.append(i)
#     else:
#         odd_li.append(i)
# print('even number:',even_li)
# print('odd number:',odd_li)
'''check pallendram or not'''
'''li=[433,232,563,898,565,221,454,3113,67]
for i in li:
    if str(i)==str(i)[::-1]:
        print(i,'pallendram')
    else:
        print(i,'not pallendram')'''
'''string or not'''
'''li=[10,20,30,90,9+2j,'78','ashok']
for i in li:
    if type(i)==str:
        print(i,'string')
    else:
        print(i,'not string')
for i in li:
    if isinstance(i,int):
        print(i,'int')'''
# li=[[1,2],[3,4],[4,5]]
# for i in li:
#     if type(i)==list:
#         for j in i:
#             print(j)
#         else:
#             print(i)
'''li = [[1,2],[3,4],[5,6],(8,9)]

for i in li:
    for j in i:
        print(j)'''
'''li=[1,2,[3,4]]

for i in li:
    if type(i)==list:
        for j in i:
            print(j)
    else:'''
            # print(i)
# li = [1,2,[3,4]]
#
# for i in li:
#     if type(i)==list:
#         for j in i:
#             print(j)
#     else:
#         print(i)
# li=[1,2,(89,90),7,8,[90,91]]
# for i in li:
#     if type(i)==list or type(i)==list:
#         for j in i:
#             print(j)
#     else:
#         print(i)
# li = [1,2,(89,90),7,8,[90,91]]
#
#
# for i in li:
#     if type(i)==list or type(i)==tuple:
#         for j in i:
#             print(j)
#     else:
#         print(i)
# st='BRAHAMPUR'
# new_st=''
# for i in st:
#     new_st=new_st+i.lower()/new_st=i+new_st
#     print(new_st)
# st = 'King Kong Is GrEat'
# upper = ''
# lower = ''
# for i in st:
#     if i.isupper():
#         upper = upper+i
#     elif i.islower():
#         lower= lower+i
# print(upper)
# print(lower)
# for var in range(2,51,2):
#     print(var)
# for i in range(1,6):
#     print('*')
# for i in range (1,5):
#     print('*',end='')
# for i in range(1,6):
#     print('*'*i)
# for i in range(1,5):
#     print('*'*(i+1))
# for i in range (1,6):
#     print('*'*(6-i))
# num=int(input('enter a number:'))
# for i in range(1,num+1):
#     print('*'*((num+1)-i))
# for i in range(1,10):
#     print('' * (10 - (i + 1)) + '*' * i)
# for i in range(1,7):
#     print('*'*(i))
# for i in range(1,10):
#         print('*'*(i-0)+''*(10-i))
# a,b,c=20,30,40
# print(c)
# li = [
# {'Name':'A','Age':26,'Salary':67000},
# {'Name':'B','Age':27,'Salary':89000},
# {'Name':'C','Age':34,'Salary':81000},
# {'Name':'D','Age':33,'Salary':72000},
# {'Name':'E','Age':33,'Salary':70000},
# {'Name':'F','Age':33,'Salary':72000},
#
# ]
#
# for i in li:
#         if i['Age']>30:
#             print(i['Name'],i['Salary'])
# li = [
# {'Name':'A','Age':26,'Salary':67000},
# {'Name':'B','Age':27,'Salary':89000},
# {'Name':'C','Age':34,'Salary':65000},
# {'Name':'D','Age':33,'Salary':72000},
# {'Name':'E','Age':38,'Salary':60000},
# {'Name':'F','Age':35,'Salary':72000},
# {'Name':'G','Age':31,'Salary':72000},
# {'Name':'G','Age':43,'Salary':70000},
#
# ]
# for i in li:
#         if i['Salary']>60000 and i['Salary']<=70000:
#              print(i['Name'],i['Age'])
# li = [
# {'Name':'A','Age':26,'Salary':67000,'Subjcet':['Python','Java ','C']},
# {'Name':'B','Age':27,'Salary':89000,'Subjcet':['Ruby','Golang ','C']},
# {'Name':'C','Age':34,'Salary':65000,'Subjcet':['.Net','SQL ','Perl']},
# {'Name':'D','Age':33,'Salary':72000,'Subjcet':['Python','Perl ','Ruby']},
# {'Name':'E','Age':38,'Salary':60000,'Subjcet':['SQL','Java ','PLSQL']},
# ]
#
# for i in li:
#     if 'Python' and 'Java ' in i['Subjcet']:
#         print(i['Name'])
# li = [
# {'Name':'A','Age':26,'Salary':67000,'Subjcet':['Python','Java','C']},
# {'Name':'B','Age':27,'Salary':89000,'Subjcet':['Ruby','Golang ','C']},
# {'Name':'C','Age':34,'Salary':65000,'Subjcet':['.Net','SQL ','Perl']},
# {'Name':'D','Age':33,'Salary':72000,'Subjcet':['Python','Perl ','Ruby']},
# {'Name':'E','Age':38,'Salary':60000,'Subjcet':['SQL','Java ','PLSQL']},
# ]
#
# for i in li:
#     if 'Python' and 'Java' in i['Subjcet'] :
#         print(i['Name'])


# di ={
#     "page": 2,
#     "per_page": 6,
#     "total": 12,
#     "total_pages": 2,
#     "data": [
#         {
#             "id": 7,
#             "email": "michael.lawson@reqres.in",
#             "first_name": "Michael",
#             "last_name": "Lawson",
#             "avatar": "https://reqres.in/img/faces/7-image.jpg"
#         },
#         {
#             "id": 8,
#             "email": "lindsay.ferguson@reqres.in",
#             "first_name": "Lindsay",
#             "last_name": "Ferguson",
#             "avatar": "https://reqres.in/img/faces/8-image.jpg"
#         },
#         {
#             "id": 9,
#             "email": "tobias.funke@reqres.in",
#             "first_name": "Tobias",
#             "last_name": "Funke",
#             "avatar": "https://reqres.in/img/faces/9-image.jpg"
#         },
#         {
#             "id": 10,
#             "email": "byron.fields@reqres.in",
#             "first_name": "Byron",
#             "last_name": "Fields",
#             "avatar": "https://reqres.in/img/faces/10-image.jpg"
#         },
#         {
#             "id": 11,
#             "email": "george.edwards@reqres.in",
#             "first_name": "George",
#             "last_name": "Edwards",
#             "avatar": "https://reqres.in/img/faces/11-image.jpg"
#         },
#         {
#             "id": 12,
#             "email": "rachel.howell@reqres.in",
#             "first_name": "Rachel",
#             "last_name": "Howell",
#             "avatar": "https://reqres.in/img/faces/12-image.jpg"
#         }
#     ],
#     "support": {
#         "url": "https://reqres.in/#support-heading",
#         "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
#     }
# }
#
# id_end = int(input('Enter your id number:-'))
#
# for i in di['data']:
#     if i['id']==id_end:
#         print(i['email'])
# num = 1
# num_end = 10
# sum = 0
# while num <= num_end:
#     sum=sum+num
#     num=num+1
# print(sum)
#DICT
# di=[{'name':'ashok','age':26,'salary':56000}
# {'name':'ashok','age':27,'salary':57000},
# {'name':'ashok','age':28,'salary':58000},
# {'name':'ashok','age':29,'salary':59000},
# {'name':'ashok','age':30,'salary':60000}]
# print(di['name'])
# var=['key_name']
# print(di)
# di['name']='cs'
# print(dir(di))
# di.clear()
# print(di)
# var=di.copy()
# print(di)
# print(var)
# var=di.get('name')
# print(var)
# for i in di:
#     print(f"Key: {i}")
#     for values in di.values():
#         print(f'value:{values}')
# di={{'name':'ashok','age':26,'salary':56000},
# {'name':'ashok','age':27,'salary':57000},
# {'name':'ashok','age':28,'salary':58000},
# {'name':'ashok','age':29,'salary':59000},
# [{'name':'ashok','age':30,'salary':60000}]
# }
# for key,value in di:
#     print(f'key:{key}={value}')
# student_grades = {
#     'Math': {'midterm': 85, 'final': 90},
#     'Science': {'midterm': 88, 'final': 92},
#     'English': {'midterm': 78, 'final': 84}
# }
#
# # Iterating over subjects
# for subject in student_grades:
#     print(f"Subject: {subject}")
#
# # Iterating over grades
# for grades in student_grades.values():
#     print(f"Grades: {grades}")
#
# # Iterating over subjects and their grades
# for subject, grades in student_grades.items():
#     print(f"{subject}: Midterm: {grades['midterm']}, Final: {grades['final']}")
# product_details = {
#     'id': 101,
#     'name': 'Laptop',
#     'price': 999.99,
#     'in_stock': True,
#     'tags': ['electronics', 'computer']
# }
#
# # Iterating over keys
# for key in product_details:
#     print(f"Key: {key}")
#
# # Iterating over values
# for value in product_details.values():
#     print(f"Value: {value}")
#
# # Iterating over key-value pairs
# for key, value in product_details.items():
#     print(f"{key}: {value}")
# n=5
# for i in range(n):
#     for j in range(n):
#         print('*',end=' ')
#         print()
# def print_star_square(size):
#     for i in range(size):
#         print('*' * size)
#
# # Example usage
# print_star_square(5)
# n=int(input('enter a number'))
#     for i in range():         # Outer loop for each row
#         for j in range():     # Inner loop for each column in the row
#             print('*', end='')    # Print a star without a newline
#         print()     # Print a newline after each ro
#     n=int(input('enter your number'))
#         for j in range(n):
#             for i in range(n):
#                 print('*',end='')
# n=int(input('enter your number'))
# for i in range(n):
#     for j in  range(n):
#         print('*',end='')
#         print()
# def a (num):
#     digits = 0
#     temp = num
#     while temp > 0:
#         temp //= 10
#         digits =digits+1
#     powers = 0
#     temp = num
#     while temp > 0:
#         digit = temp % 10
#         powers =powers+ digit ** digits
#         temp //= 10
#
#     return num == powers
#
# numbers = [153, 370, 371, 407, 9474, 123]
# for number in numbers:
#     if a (number):
#         print(f"{number} is an Armstrong number.")
#     else:
#         print(f"{number} is not an Armstrong number.")


#Calculator
# def calcu(*args):
#     result=0
#     for i in args:
#         arth=input('enter your opration:-')
#         if arth=='+':
#             result=result+i
#         elif arth=='-':
#             result=result-i
#         elif arth=='*':
#             result=result*i
#         # elif arth=='/':
#         #     result=result//i
#     return result
# print(calcu(15,25,35))
# a = 10
# b = 20

# print("Both are equal" if a == b else "a is greater"
#       if a > b else "b is greater")
# age =int(input("enter your age:"))
# status = "Adult" if age >= 18 else "Minor"

# print(status)
# from faker import Faker
#
# fake = Faker()
#
# print("Name:", fake.name())
#
#
# print("Address:", fake.address())
#
# print("Email:", fake.email())


# print("Phone number:", fake.phone_number())
#
# print("Company:", fake.company())
#
# print("Job Title:", fake.job())

# print("Date of Birth:", fake.date_of_birth())

# print("Credit Card Number:", fake.credit_card_number())

# for i in range(100):
    # profile = fake.simple_profile()
    # print(profile)
def greet(name):
    return f'hello,{name}'
pi=3.14159
class cricle:
    def __int__(self,radius):
        self.radius=radius
    def area(self):
        return pi*(self.radius**2)
    cricle=cricle(5)



