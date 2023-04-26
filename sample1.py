from data.cryptoop import array


a = array(['hello', 'hi'], "super_key", Type=3)
a.add("cat")
print(a)


a.add(1)
print(a.to_pyarray("super_key"))
