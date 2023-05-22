from data.cryptoop import array
from data.EnCrypt import generate_keypair
from data.cryptoop import Keys

a={(1,23,3):[2,3]}

message = "Hello, RSA!"
public_key, private_key = generate_keypair()

# setCommonKey(public_key)
obj = Keys()
obj.setkey(public_key)


a = array(object=['hello', 'hi',3],Type=4)
a.add("cat")
print(a)

# a.add(1)
print(a.to_pyarray(private_key))
