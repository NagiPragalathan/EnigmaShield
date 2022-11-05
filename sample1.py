# from data.EnCrypt import FileEncrypt,FileDecrypt

# a = FileEncrypt("C:/Users/NagiPragalathan/Downloads/FarmTech-f68306c054698a7ffe2ca003e9c45ca7b0a2da3b/FarmTech-f68306c054698a7ffe2ca003e9c45ca7b0a2da3b/Main/static/chatbot/img/chatbot.jpg","key")

# print(a)

# img = FileDecrypt(a,"key1","C:\\Users\\NagiPragalathan\\Desktop\\NewCrypto\\data\\img1.jpg")

from data import cryptoop as cp

a=cp.Dict({1:2,"23":"hie"},"hi")
a.add("hello","nagi")
print(a.get(23,"hi"))
print(a.to_pyDict("hi"))
b=a.setdefault("hi","hello")
print("set default is : ",b)
print("pop item is : ",a.popitem())
print(a.to_pyDict("hi"))
print(a.items())
print(a.keys("hi"))
print(a.values("hi"))
print(a.from_keys((1,2),"hi",security_key="hi"))



