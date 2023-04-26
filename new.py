from data.EnCrypt import Encrypt, Decrypt, easyEncrypt, easyDectypt, encrypt, decrypt


class Int:
    def __init__(self, value, key, Type=3):
        self.type = Type
        self.Key = key
        self.value = self.CryptoType(value, key)

    def CryptoType(self, String: str, key: str):
        if self.type == 1:
            return Encrypt(String, key)
        elif self.type == 2:
            return easyEncrypt(String, key)
        elif self.type == 3:
            return encrypt(String, key)

    def DeCryptoType(self, String: str, key: str):
        if self.type == 1:
            return Decrypt(String, key)
        elif self.type == 2:
            return easyDectypt(String, key)
        elif self.type == 3:
            return decrypt(String, key)

    def get_int(self, key):
        if key == self.Key:
            return self.DeCryptoType(self.value, self.Key)

    def __int__(self):
        return int(self.value)

    def __str__(self):
        return str(self.value)

    def get_repr(self, key):
        if self.Key == key:
            return f"Int({self.DeCryptoType(self.value, self.Key)})"
        else:
            return f"Int({self.value})"

    def __repr__(self):
        return f"Int({self.value})"

    def __float__(self):
        return float(self.value)

    def get_float(self, key):
        if self.Key == key:
            return float(self.DeCryptoType(self.value, self.Key))
        else:
            return float(self.value)

    def __bool__(self):
        return bool(self.DeCryptoType(self.value, self.Key))

    def __eq__(self, other):
        if isinstance(other, Int):
            return int(self.DeCryptoType(self.value, self.Key)) == other.value
        elif isinstance(other, (int, float)):
            return int(self.DeCryptoType(self.value, self.Key)) == other
        return False

    def __lt__(self, other):
        if isinstance(other, Int):
            return int(self.DeCryptoType(self.value, self.Key)) < other.value
        elif isinstance(other, (int, float)):
            return int(self.DeCryptoType(self.value, self.Key)) < other
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Int):
            return int(self.DeCryptoType(self.value, self.Key)) <= other.value
        elif isinstance(other, (int, float)):
            return int(self.DeCryptoType(self.value, self.Key)) <= other
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Int):
            return int(self.DeCryptoType(self.value, self.Key)) > other.value
        elif isinstance(other, (int, float)):
            return int(self.DeCryptoType(self.value, self.Key)) > other
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Int):
            return int(self.DeCryptoType(self.value, self.Key)) >= other.value
        elif isinstance(other, (int, float)):
            return int(self.DeCryptoType(self.value, self.Key)) >= other
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Int):
            return Int(self.DeCryptoType(self.value, self.Key) + other.value, self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) + other, self.Key)
        return NotImplemented

    def add(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) + int(self.DeCryptoType(other, self.Key)), self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) + other, self.Key)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) - other.value, self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) - other, self.Key)
        return NotImplemented

    def sub(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) - int(self.DeCryptoType(other, self.Key)), self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) - other, self.Key)
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Int(other - int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def rsub(self, other):
        if isinstance(other, (int, float)):
            return Int(other - int(self.DeCryptoType(self.value, self.Key)), self.Key)
        else:
            return Int(int(self.DeCryptoType(other, self.Key)) - int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) * other.value, self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) * other, self.Key)
        return NotImplemented

    def mul(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) * int(self.DeCryptoType(other, self.Key)), self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) * other, self.Key)
        return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def rmul(self, other):
        if isinstance(other, Int):
            return self.__mul__(int(self.DeCryptoType(other, self.Key)))
        else:
            return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) / other.value, self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) / other, self.Key)
        return NotImplemented

    def truediv(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) / int(self.DeCryptoType(other, self.Key)), self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) / other, self.Key)
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Int(other // int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def rtruediv(self, other):
        if isinstance(other, (int, float)):
            return Int(other // int(self.DeCryptoType(self.value, self.Key)), self.Key)
        else:
            return Int(int(self.DeCryptoType(other, self.Key)) // int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) // other.value, self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) // other, self.Key)
        return NotImplemented

    def floordiv(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) // int(self.DeCryptoType(other, self.Key)), self.Key)
        elif isinstance(other, (int, float)):
            return Int(other // int(self.DeCryptoType(other, self.Key)), self.Key)
        return NotImplemented

    def __rfloordiv__(self, other):
        if isinstance(other, (int, float)):
            return Int(other // int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def rfloordiv(self, other):
        if isinstance(other, (int, float)):
            return Int(other // int(self.DeCryptoType(self.value, self.Key)), self.Key)
        else:
            return Int(int(self.DeCryptoType(other, self.Key)) // int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) % other.value, self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) % other, self.Key)
        return NotImplemented

    def mod(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) % int(self.DeCryptoType(other, self.Key)), self.Key)
        elif isinstance(other, (int, float)):
            return other % int(self.DeCryptoType(other, self.Key))
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) ** other.value, self.Key)
        elif isinstance(other, (int, float)):
            return Int(int(self.DeCryptoType(self.value, self.Key)) ** other, self.Key)
        return NotImplemented

    def pow(self, other):
        if isinstance(other, Int):
            return Int(int(self.DeCryptoType(self.value, self.Key)) ** int(self.DeCryptoType(other, self.Key)), self.Key)
        elif isinstance(other, (int, float)):
            return Int(other ** int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def __rpow__(self, other):
        if isinstance(other, (int, float)):
            return Int(other ** int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented

    def rpow(self, other):
        if isinstance(other, (int, float)):
            return Int(other ** int(self.DeCryptoType(self.value, self.Key)), self.Key)
        else:
            return Int(int(self.DeCryptoType(other, self.Key)) ** int(self.DeCryptoType(self.value, self.Key)), self.Key)
        return NotImplemented


a = Int(4, 'hjfvu')
c = a % 6
d = a.mul(c).add(4).add(c).pow(4)
print('d', d.get_int('hjfvu'))
print(c, a)
print(decrypt(a, 'hjfvu'))
print(a.get_int('hjfvu'), c.get_int('hjfvu'))
