# from data.EnCrypt import FileEncrypt,FileDecrypt

# a = FileEncrypt("C:/Users/NagiPragalathan/Downloads/FarmTech-f68306c054698a7ffe2ca003e9c45ca7b0a2da3b/FarmTech-f68306c054698a7ffe2ca003e9c45ca7b0a2da3b/Main/static/chatbot/img/chatbot.jpg","key")

# print(a)

# img = FileDecrypt(a,"key1","C:\\Users\\NagiPragalathan\\Desktop\\NewCrypto\\data\\img1.jpg")

from data import cryptoop as cp

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Dictinary>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# a=cp.Dict({1:2,"23":"hie"},"hi")
# a.add("hello","nagi")
# print(a.get(23,"hi"))
# print(a.to_pyDict("hi"))
# b=a.setdefault("hi","hello")
# print("set default is : ",b)
# print("pop item is : ",a.popitem())
# print("pop item is : ",a.pop(1))
# print(a.to_pyDict("hi"))
# print(a.items())
# print(a.keys("hi"))
# print(a.values("hi"))
# print(a.from_keys((1,2),"hi",security_key="hi"))
# print(a.to_pyDict("hi"))
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>Tuple>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
# a = cp.Tuple((1,1,23,3,"hello",(1,2,((1,23),12,3))),"hi")

# print(a)
# print(a.count(1))
# print(a.index(23))
# print(a.to_pytuple("hi"))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.Set.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.


# a = cp.Set({"a", "b", "c"},"hello")
# x = {"a", "b", "c"}
# y = {"f", "e", "d", "c", "b", "a"}
# z = {"f", "g", "c"}
# # a.add((1,2))
# # a.add(7)
# # a.remove(7)
# # a.pop()
# # b={"google", "microsoft", "apple"}
# # print(a.difference_update(b,"hello")) 
# # a.discard("banana")
# # print(a.intersection(y,z,security_key="hello"))
# print(a.isdisjoint(y))
# print(a.to_pyset("hello"))

# print(a)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>String>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
a=cp.String("hello hi hi","hi")
print(a.capitalize("hi"))
print(a.casefold("hi"))
print(a.center(20,security_key="hi"))
print(a.zfill(15,security_key="hi"))
print(a.upper(security_key="hi"))
print(a.lower(security_key="hi"))
print(a.title(security_key="hi"))
print(a.swapcase(security_key="hi"))
print("hia",a.strip(" ",security_key="hi"))
print(a.split(" ",security_key="hi"))
print(a.split(" "))
print(a.istitle(security_key="hi"))
print(a.istitle())
print(a.isalnum(security_key="hi"))
print(a.isalpha(security_key="hi"))
print(a.isascii(security_key="hi"))
print(a.isdecimal(security_key="hi"))
print(a.isdigit(security_key="hi"))
print(a.isidentifier(security_key="hi"))
print(a.islower(security_key="hi"))
print(a.isnumeric(security_key="hi"))
print(a.isprintable(security_key="hi"))
print(a.isspace(security_key="hi"))
print(a.find("h"))





print(a)