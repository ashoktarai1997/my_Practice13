# a=200
# b=300
# c=a+b
# print(id(c),c)
# '''DATA TPYES'''
# #string slicing
# a='CHATRAPURA'
# print(a[0:4:1])
# b='CHATRAPUR'
# print(b[1:12:3])
# ba='ASHOK KUMAR TARAI'
# print(ba[0:15:3])
# c='ashok kumar tarai'
# print(c)
# d='ashok kumar tarai'
# print(d[::-1])
# name='ashok kumar tarai'
# dob='17/02/1997'
# password=name[0:4]+dob[-4:]
# print(password)
# da='ahok'
# print(da*5)
# #string methon
# a='ashok'
# print(a.capitalize())
# b='ASHOK'
# print(b.swapcase())
# c='ashok'
# print(c.upper())
# d='ASHOK'
# print(d.lower())
# e='tarai, ashok'
# print(e.startswith('o'))
# f='tarai ashok'
# print(e.endswith('h'))
# g='ashok kumar,akshya kumar,akankshya kumari,arusha kumar'
# print(g.count('kumari'))
# h='akankshya'
# print(h.find('h'))
# i='akshya kumar'
# print(i.index('a'))
# j=' ashokkumar '
# print(j.replace('kumar','tarai'))
# print(j.isalnum())
# print(j.isalpha())
# print(j.isdigit())
# print(j.islower())
# print(j.isupper())
# k=' ashokkmar'
# print(k.strip())
# l='ashok kumar akshya kumar'
# print(l.split())
# m=['ashok', 'kumar','akshaya','kumar']
# var=' '.join(m)
# print(var)
# n=10
# nn=20
# nnn=n+nn
# print(f'print the number:{nnn}')
#
# #list and tuple

# selenium
from selenium import webdriver
driver=webdriver.chrome
driver=webdriver.Firefox
# driver.get("https://www.google.com"/)
driver.get("https://www.google.com")
