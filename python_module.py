# from faker import Faker
#
# fake = Faker()
# print("Name:", fake.name())
#
#
# print("Address:", fake.address())
#
#
# print("Email:", fake.email())
#
#
# print("Phone number:", fake.phone_number())
#
#
# print("Company:", fake.company())
#
#
# print("Job Title:", fake.job())
#
#
# print("Date of Birth:", fake.date_of_birth())
#
#
# print("Credit Card Number:", fake.credit_card_number())
# for _ in range(2):
#     profile = fake.simple_profile()
#     print(profile)
# import faker
# fake = faker.Faker()
# count = 0
# names = []
# while count < 7:
#     name = fake.name()
#     if name.endswith('a'):
#         count =count+1
#         print(name.islower())
#         print(name)
fruits=['apple','banana','cherry','date']
print(fruits[1])
fruits[0]='apricot'
fruits.append('elderberry')
print(fruits)
fruits.insert(2,'sitafal')
fruits.remove('banana')
fruits.pop()
print(fruits)
for fruit in fruits:
    print(fruit)
    print(len(fruits))
    if 'cherry' in fruits:
        print('cheery in the list')
        print(fruits[:3])
        fruits_lenght=[len(fruit) for fruit in fruits]
        print(fruits_lenght)








