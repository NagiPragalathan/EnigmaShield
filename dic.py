from data.cryptoop import array, String, Int, Tuple, Dict
from data.EnCrypt import generate_keypair


public_key, private_key = generate_keypair()

print(public_key, private_key)

# c=Int(3444,key=public_key,Type=4)

# print(c.get_int(private_key),"hi")
# b=String("hello1",Key=public_key,Type=4)

# print(b.topystr(private_key),"runned")

# a = array(("ab","cd","ef"), 'hi')
# # a.__add__(78)
# print(len(a))
# b = (1, 2, 3)
# print(len(b))

# dic = Tuple((1,2,3,4,5),public_key,4)
# print(dic.to_pytuple(private_key))

dicte = Dict({"hello":3,"hi":"he",(1,2,3,4,"hi"):5,"ji":[1,2]},public_key,4)
print("dicte",dicte)
print(dicte.to_pyDict(private_key),"output")
