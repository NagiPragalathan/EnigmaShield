from .EnCrypt import Encrypt, Decrypt, easyEncrypt, easyDectypt, encrypt, decrypt, RSAdecrypt, RSAencrypt



commonKey=False
EncryptType=3


class Keys:
    def __init__(self):
        global commonKey, EncryptType
        self.commonKey = commonKey
        self.encrypt_type=EncryptType
    def getkey(self):
        return self.commonKey
    def setkey(self,key):
        global commonKey
        self.commonKey = key
        commonKey = self.commonKey
    def setType(self,Encrypt_type):
        global EncryptType
        self.encrypt_type=Encrypt_type
        EncryptType = Encrypt_type
    def getType(self):
        return self.encrypt_type
        



class array:
    def __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False) -> None:
        self.Arrays = []
        obj = Keys()
        if Type:
            self.type = Type
        else:
            self.type = obj.getType()
        if Key:
            self.Key = Key
            Key = Key
        else:
            self.Key = obj.getkey()
            Key = obj.getkey()
        self.obj = object
        temp = []
        if BaseType:
            pass
        elif LongCrypt:
            pass
        else:
            self.Arrays = self.iters(object, Key)

    def CryptoType(self, String: str, key: str):
        if self.type == 1:
            return Encrypt(String, key)
        elif self.type == 2:
            return easyEncrypt(String, key)
        elif self.type == 3:
            return encrypt(String, key)
        elif self.type == 4:
            return RSAencrypt(String, key)

    def DeCryptoType(self, String: str, key: str):
        if self.type == 1:
            return Decrypt(String, key)
        elif self.type == 2:
            return easyDectypt(String, key)
        elif self.type == 3:
            return decrypt(String, key)
        elif self.type == 4:
            return RSAdecrypt(String, key)

    def list_to_dic(self, Keys, Values):
        res = {}
        for key in Keys:
            for value in Values:
                res[key] = value
                Values.remove(value)
                break
        return res

    def Diciters(self, obj, key, operation="en", type=list):
        temp = []
        dictemp = {}
        for i in obj:
            if isinstance(i, list):
                change = self.iters(i, key, operation, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), key, operation, tuple)
                temp.append(change)
            elif isinstance(i, str):
                return self.CryptoType(i, key)
            elif isinstance(i, set):
                change = self.iters(list(i), key, operation, set)
                temp.append(change)
            elif isinstance(i, dict):
                change = self.dict_type(i, key, operation)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ................................
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)

        if type is list:
            return temp
        elif type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)
        elif type is dict:
            return temp

    def iters(self, obj, key, operation="en", data_type=list):
        result = []
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, list) and self.type != 4 :
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de" and self.type == 4:
                        result.append(self.DeCryptoType(item, key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, tuple):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, set):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        if data_type is list:
            return result
        elif data_type is tuple:
            return tuple(result)
        elif data_type is set:
            return set(result)
        elif data_type is dict:
            return result

    def setiters(self, obj, key, operation="en", type=set):
        temp = set()
        for i in obj:
            if isinstance(i, tuple):
                change = self.setiters(i, key, operation, tuple)
                temp.add(change)
            elif isinstance(i, set):
                change = self.setiters(i, key, operation, set)
                temp.add(change)
            else:
                if (operation == "en"):
                    temp.add(i)  # ................................
                elif (operation == "de"):
                    temp.add(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.add(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.add(int(i))
                    else:
                        temp.add(i)
        if type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)

    def dict_type(self, obj, key, operation="en"):
        temp = []
        temp1 = []
        keys = obj.keys()
        values = obj.values()
        for i in values:
            if isinstance(i, list):
                change = self.iters(i, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ...# this is main line if any changes are make here all values are affected....
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
        for i in keys:
            if isinstance(i, list):
                change = self.iters(i, list)
                temp1.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), tuple)
                temp1.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp1.append(change)
            else:
                if (operation == "en"):
                    # impartent..............
                    temp1.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp1.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp1.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp1.append(int(i))
                    else:
                        temp1.append(i)
        return self.list_to_dic(temp1, temp)

    def add(self, element: object):
        if isinstance(element, list):
            self.Arrays.append(self.iters(element, self.Key))
        elif isinstance(element, int):
            self.Arrays.append(self.CryptoType(str(element), self.Key))
        elif isinstance(element, str):
            self.Arrays.append(self.CryptoType(element, self.Key))
        elif isinstance(element, tuple):
            self.Arrays.append(tuple(self.iters(list(element), self.Key)))
        elif isinstance(element, set):
            self.Arrays.append(set(self.iters(list(element), self.Key)))
        elif isinstance(element, dict):
            self.Arrays.append(self.dict_type(element, self.Key))

    def extend(self, iterable):
        for i in iterable:
            self.add(i)

    def index(self, object):
        if isinstance(object, list):
            obj_string = self.iters(object, self.Key, "str")
        elif isinstance(object, int):
            obj_string = str(object)
        elif isinstance(object, tuple):
            obj_string = tuple(self.iters(list(object), self.Key, "str"))
        elif isinstance(object, set):
            obj_string = set(self.iters(list(object), self.Key, "str"))
        elif isinstance(object, dict):
            obj_string = self.dict_type(object, self.Key, "str")
        orginal = self.iters(self.Arrays, self.Key, "de")
        index_is = orginal.index(obj_string)
        return index_is

    def len(self):
        return len(self.Arrays)

    def clear(self):
        self.Arrays = []
        return self.Arrays

    def copy(self):
        return self.Arrays

    def to_pyarray(self, key):
        orginal = self.iters(self.Arrays, key, "de")
        orginal = self.iters(orginal, key, "org")
        return orginal

    def insert(self, index, object):
        if isinstance(object, list):
            self.Arrays.insert(index, self.iters(object, self.Key))
        elif isinstance(object, int):
            self.Arrays.insert(index, self.CryptoType(str(object), self.Key))
        elif isinstance(object, str):
            self.Arrays.insert(index, self.CryptoType(object, self.Key))
        elif isinstance(object, tuple):
            self.Arrays.insert(index, tuple(
                self.iters(list(object), self.Key)))
        elif isinstance(object, set):
            self.Arrays.insert(index, set(self.iters(list(object), self.Key)))
        elif isinstance(object, dict):
            self.Arrays.insert(index, self.dict_type(object, self.Key))

    def count(self, element):
        if isinstance(element, list):
            obj_string = self.iters(element, self.Key, "str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, tuple):
            obj_string = tuple(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, set):
            obj_string = set(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, dict):
            obj_string = self.dict_type(element, self.Key, "str")
        orginal = self.iters(self.Arrays, self.Key, "de")
        count_is = orginal.count(obj_string)
        return count_is

    def remove(self, element):
        if isinstance(element, list):
            obj_string = self.iters(element, self.Key, "str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, str):
            obj_string = str(element)
        elif isinstance(element, tuple):
            obj_string = tuple(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, set):
            obj_string = set(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, dict):
            obj_string = self.dict_type(element, self.Key, "str")
        orginal = self.iters(self.Arrays, self.Key, "de")
        orginal.remove(obj_string)
        self.Arrays = self.iters(orginal, self.Key, "en")

    def reverse(self):
        self.Arrays = self.Arrays[::-1]

    def sort(self, key=False, reverse=False):
        obj_string = self.to_pyarray(self.Key)
        if key and reverse:
            self.Arrays = obj_string.sort(key, reverse)
        elif reverse:
            self.Arrays = obj_string.sort(reverse)
        elif key:
            self.Arrays = obj_string.sort(key)
        else:
            self.Arrays = obj_string.sort()

    def pop(self, index):
        self.Arrays.pop(index)

    def __len__(self):
        return self.Arrays.__len__()

    def __str__(self) -> str:
        return str(self.Arrays)

    def __repr__(self) -> str:
        return "CryptoArray"

    def __getitem__(self, index):
        return self.Arrays.__getitem__(index)

    def __setitem__(self, index, value):
        return self.Arrays.__setitem__(index, value)

    def __delitem__(self, index):
        return self.Arrays.__delitem__(index)

    def __contains__(self, value):
        return self.Arrays.__contains__(value)

    def __iter__(self):
        return self.Arrays.__iter__()

    def __reversed__(self):
        return self.Arrays.__reversed__()

    def __add__(self, other):
        if isinstance(other, array):
            return array(self.Arrays.__add__(other))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, array):
            return self.Arrays.__iadd__(other)
        return NotImplemented

    def __mul__(self, count):
        return array(self.Arrays.__mul__(count))

    def __imul__(self, count):
        return self.Arrays.__imul__(count)

    def __eq__(self, other):
        if isinstance(other, array):
            return self.Arrays.__eq__(other)
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    def __lt__(self, other):
        if isinstance(other, array):
            return self.Arrays.__lt__(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, array):
            return self.Arrays.__le__(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, array):
            return self.Arrays.__gt__(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, array):
            return self.Arrays.__ge__(other)
        return NotImplemented

    def __hash__(self):
        return self.Arrays.__hash__()

    def __repr__(self):
        return self.Arrays.__repr__()


class Dict:
    def __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False) -> None:
        self.Dict = dict()
        if Key:
            self.key = Key
            Key = Key
        else:
            obj = Keys()
            self.Key = obj.getkey()
            Key = obj.getkey()
        self.obj = object
        if Type:
            self.type = Type
        else:
            self.type = obj.getType()
        temp = dict()
        if BaseType:
            pass
        elif LongCrypt:
            pass
        else:
            self.Dict = self.dict_type(object, Key)

    def CryptoType(self, String: str, key: str):
        if self.type == 1:
            return Encrypt(String, key)
        elif self.type == 2:
            return easyEncrypt(String, key)
        elif self.type == 3:
            return encrypt(String, key)
        elif self.type == 4:
            return RSAencrypt(String, key)

    def DeCryptoType(self, String: str, key: str):
        if self.type == 1:
            return Decrypt(String, key)
        elif self.type == 2:
            return easyDectypt(String, key)
        elif self.type == 3:
            return decrypt(String, key)
        elif self.type == 4:
            return RSAdecrypt(String, key)

    def list_to_dic(self, Keys, Values):
        res = {}
        for key in Keys:
            for value in Values:
                res[key] = value
                Values.remove(value)
                break
        return res

    def Diciters(self, obj, key, operation="en", type=list):
        temp = []
        dictemp = {}
        for i in obj:
            if isinstance(i, list):
                change = self.iters(i, key, operation, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), key, operation, tuple)
                temp.append(change)
            elif isinstance(i, str):
                return self.CryptoType(i, key)
            elif isinstance(i, set):
                change = self.iters(list(i), key, operation, set)
                temp.append(change)
            elif isinstance(i, dict):
                change = self.dict_type(i, key, operation)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ................................
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)

        if type is list:
            return temp
        elif type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)
        elif type is dict:
            return temp

    def iters(self, obj, key, operation="en", data_type=list):
        result = []
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, list) and self.type != 4 :
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        if self.type == 4:
                            result.append(self.CryptoType(item, key))
                        else:
                            result.append(self.CryptoType(str(item), key))
                    elif operation == "de" and self.type == 4:
                        result.append(self.DeCryptoType(item, key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, tuple):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, set):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        if data_type is list:
            return result
        elif data_type is tuple:
            return tuple(result)
        elif data_type is set:
            return set(result)
        elif data_type is dict:
            return result

    def setiters(self, obj, key, operation="en", type=set):
        temp = set()
        for i in obj:
            if isinstance(i, tuple):
                change = self.setiters(i, key, operation, tuple)
                temp.add(change)
            elif isinstance(i, set):
                change = self.setiters(i, key, operation, set)
                temp.add(change)
            else:
                if (operation == "en"):
                    temp.add(i)  # ................................
                elif (operation == "de"):
                    temp.add(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.add(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.add(int(i))
                    else:
                        temp.add(i)
        if type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)

    def dict_type(self, obj, key, operation="en"):
        temp = []
        temp1 = []
        keys = obj.keys()
        if operation=="de" and operation != "org":
            keys=[ list(i) for i in obj.keys()]
            
        values = obj.values()
        for i in values:
            if isinstance(i, list) and self.type != 4:
                change = self.iters(i, list)
                temp.append(change)
            elif isinstance(i, tuple) and self.type != 4:
                change = self.iters(list(i), tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ...# this is main line if any changes are make here all values are affected....
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    if self.type == 4:
                        temp.append(self.DeCryptoType(i, key))
                    else:
                        temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
        for i in keys:
            if isinstance(i, list) and self.type != 4:
                change = self.iters(i, list)
                temp1.append(change)
            elif isinstance(i, tuple) and self.type != 4:
                change = self.iters(list(i), tuple)
                temp1.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp1.append(change)
            else:
                if (operation == "en"):
                    # impartent..............
                    temp1.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    if self.type == 4:
                        temp1.append(self.DeCryptoType(i, key))
                    else:
                        temp1.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp1.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp1.append(int(i))
                    else:
                        temp1.append(i)
        if self.type == 4:
            keyss = []
            for i in temp1:
                if isinstance(i, list):
                    keyss.append(tuple(i))
                elif isinstance(i, str):
                    keyss.append(i)
            return self.list_to_dic(keyss, temp)
        else:
            return self.list_to_dic(temp1, temp)

    def add(self, key, value):
        self.Dict[self.CryptoType(key, self.Key)] = self.CryptoType(
            value, self.Key)

    def clear(self):
        self.Dict = dict()

    def copy(self):
        return self.Dict

    def to_pyDict(self, key):
        orginal_str = self.dict_type(self.Dict, key, "de")
        
        orginal = self.dict_type(orginal_str, key, "org")
        return orginal

    def get(self, key, security_key=False):
        orginalDic = self.dict_type(self.Dict, self.Key, "de")
        orginalDic = self.dict_type(orginalDic, key, "org")
        if security_key and security_key == self.Key:
            return orginalDic.get(key)
        else:
            return self.CryptoType(str(orginalDic.get(key)), self.Key)

    def items(self, security_key=False):
        orginalDic = self.dict_type(self.Dict, self.Key, "de")
        orginalDic = self.dict_type(orginalDic, self.Key, "org")
        if security_key and security_key == self.Key:
            return orginalDic.items()
        else:
            return self.Diciters(orginalDic.items(), self.Key)

    def keys(self, security_key=False):
        orginalDic = self.dict_type(self.Dict, self.Key, "de")
        orginalDic = self.dict_type(orginalDic, self.Key, "org")
        if security_key and security_key == self.Key:
            return orginalDic.keys()
        else:
            return self.Diciters(orginalDic.keys(), self.Key)

    def values(self, security_key=False):
        orginalDic = self.dict_type(self.Dict, self.Key, "de")
        orginalDic = self.dict_type(orginalDic, self.Key, "org")
        if security_key and security_key == self.Key:
            return orginalDic.values()
        else:
            return self.Diciters(orginalDic.values(), self.Key)

    def setdefault(self, keyname, value, security_key=False):
        orginalDic = self.dict_type(self.Dict, self.Key, "de")
        orginalDic = self.dict_type(orginalDic, self.Key, "org")
        if security_key and security_key == self.Key:
            return orginalDic.setdefault(keyname, value)
        else:
            return self.Diciters(orginalDic.setdefault(keyname, value), self.Key)

    def popitem(self, security_key=False):
        orginalDic = self.dict_type(self.Dict, self.Key, "de")
        orginalDic = self.dict_type(orginalDic, self.Key, "org")
        org = list(orginalDic.popitem())
        self.Dict = self.dict_type(orginalDic, self.Key, "en")
        encry = self.iters(org, self.Key)
        if security_key and security_key == self.Key:
            return org
        else:
            return encry

    def pop(self, key_value):
        orginalDic = self.dict_type(self.Dict, self.Key, "de")
        orginalDic = self.dict_type(orginalDic, self.Key, "org")
        orginalDic.pop(key_value)
        self.Dict = self.dict_type(orginalDic, self.Key, "en")

    def from_keys(self, key, value=False, security_key=False):
        if value:
            fromdic_ = dict.fromkeys(key, value)
        else:
            fromdic_ = dict.fromkeys(security_key)
        returntype = self.dict_type(fromdic_, security_key)
        return returntype

    def __str__(self) -> str:
        return str(self.Dict)

    def __repr__(self) -> str:
        return "CryptoSet"

    def __getitem__(self, key):
        return self.Dict.__getitem__(key)

    def __setitem__(self, key, value):
        return self.Dict.__setitem__(key, value)

    def __delitem__(self, key):
        return self.Dict.__delitem__(key)

    def __contains__(self, key):
        return self.Dict.__contains__(key)

    def __iter__(self):
        return self.Dict.__iter__()

    def __len__(self):
        return self.Dict.__len__()

    def __eq__(self, other):
        if isinstance(other, Dict):
            return self.Dict.__eq__(other)
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    def __repr__(self):
        return self.Dict.__repr__()

    def __str__(self):
        return self.Dict.__str__()

    def keys(self):
        return self.Dict.keys()

    def values(self):
        return self.Dict.values()

    def items(self):
        return self.Dict.items()

    def get(self, key, default=None):
        return self.Dict.get(key, default)

    def pop(self, key, default=None):
        return self.Dict.pop(key, default)

    def popitem(self):
        return self.Dict.popitem()

    def clear(self):
        return self.Dict.clear()

    def update(self, other):
        return self.Dict.update(other)

    def copy(self):
        return Dict(self.Dict.copy())

    def fromkeys(self, cls, iterable, value=None):
        return Dict(self.Dict.fromkeys(iterable, value))


class Tuple:
    def __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False) -> None:
        self.Tuple = tuple()
        if Type:
            self.type = Type
        else:
            self.type = obj.getType()
        if Key:
            self.key = Key
            Key = Key
        else:
            obj = Keys()
            self.Key = obj.getkey()
            Key = obj.getkey()
        self.obj = object
        temp = tuple()
        if BaseType:
            pass
        elif LongCrypt:
            pass
        else:
            if self.type == 4:
                self.Tuple = self.iters(object, Key)
            else:
                self.Tuple = tuple(self.iters(object, Key))

    def CryptoType(self, String: str, key: str):
        if self.type == 1:
            return Encrypt(String, key)
        elif self.type == 2:
            return easyEncrypt(String, key)
        elif self.type == 3:
            return encrypt(String, key)
        elif self.type == 4:
            return RSAencrypt(String, key)

    def DeCryptoType(self, String: str, key: str):
        if self.type == 1:
            return Decrypt(String, key)
        elif self.type == 2:
            return easyDectypt(String, key)
        elif self.type == 3:
            return decrypt(String, key)
        elif self.type == 4:
            return RSAdecrypt(String, key)

    def list_to_dic(self, Keys, Values):
        res = {}
        for key in Keys:
            for value in Values:
                res[key] = value
                Values.remove(value)
                break
        return res

    def Diciters(self, obj, key, operation="en", type=list):
        temp = []
        dictemp = {}
        for i in obj:
            if isinstance(i, list):
                change = self.iters(i, key, operation, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), key, operation, tuple)
                temp.append(change)
            elif isinstance(i, str):
                return self.CryptoType(i, key)
            elif isinstance(i, set):
                change = self.iters(list(i), key, operation, set)
                temp.append(change)
            elif isinstance(i, dict):
                change = self.dict_type(i, key, operation)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ................................
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)

        if type is list:
            return temp
        elif type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)
        elif type is dict:
            return temp

    def iters(self, obj, key, operation="en", data_type=list):
        result = []
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, list) and self.type != 4 :
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de" and self.type == 4:
                        result.append(self.DeCryptoType(item, key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, tuple):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, set):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        if data_type is list:
            return result
        elif data_type is tuple:
            return tuple(result)
        elif data_type is set:
            return set(result)
        elif data_type is dict:
            return result

    def setiters(self, obj, key, operation="en", type=set):
        temp = set()
        for i in obj:
            if isinstance(i, tuple):
                change = self.setiters(i, key, operation, tuple)
                temp.add(change)
            elif isinstance(i, set):
                change = self.setiters(i, key, operation, set)
                temp.add(change)
            else:
                if (operation == "en"):
                    temp.add(i)  # ................................
                elif (operation == "de"):
                    temp.add(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.add(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.add(int(i))
                    else:
                        temp.add(i)
        if type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)

    def dict_type(self, obj, key, operation="en"):
        temp = []
        temp1 = []
        keys = obj.keys()
        if operation=="de" and operation != "org":
            keys=[ list(i) for i in obj.keys()]
            
        values = obj.values()
        for i in values:
            if isinstance(i, list) and self.type != 4:
                change = self.iters(i, list)
                temp.append(change)
            elif isinstance(i, tuple) and self.type != 4:
                change = self.iters(list(i), tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ...# this is main line if any changes are make here all values are affected....
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    if self.type == 4:
                        temp.append(self.DeCryptoType(i, key))
                    else:
                        temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
        for i in keys:
            if isinstance(i, list) and self.type != 4:
                change = self.iters(i, list)
                temp1.append(change)
            elif isinstance(i, tuple) and self.type != 4:
                change = self.iters(list(i), tuple)
                temp1.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp1.append(change)
            else:
                if (operation == "en"):
                    # impartent..............
                    temp1.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    if self.type == 4:
                        temp1.append(self.DeCryptoType(i, key))
                    else:
                        temp1.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp1.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp1.append(int(i))
                    else:
                        temp1.append(i)
        if self.type == 4:
            keyss = []
            for i in temp1:
                if isinstance(i, list):
                    keyss.append(tuple(i))
                elif isinstance(i, str):
                    keyss.append(i)
            return self.list_to_dic(keyss, temp)
        else:
            return self.list_to_dic(temp1, temp)


    def count(self, element):
        if isinstance(element, list):
            obj_string = self.iters(element, self.Key, "str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, tuple):
            obj_string = tuple(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, set):
            obj_string = set(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, dict):
            obj_string = self.dict_type(element, self.Key, "str")
        orginal = self.iters(self.Tuple, self.Key, "de")
        count_is = orginal.count(obj_string)
        return count_is

    def index(self, element):
        if isinstance(element, list):
            obj_string = self.iters(element, self.Key, "str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, str):
            obj_string = element
        elif isinstance(element, tuple):
            obj_string = tuple(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, set):
            obj_string = set(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, dict):
            obj_string = self.dict_type(element, self.Key, "str")
        orginal = self.iters(self.Tuple, self.Key, "de")
        count_is = orginal.index(obj_string)
        return count_is

    def to_pytuple(self, key):
        orginal = self.iters(self.Tuple, key, "de")
        orginal = self.iters(orginal, key, "org")
        return tuple(orginal)

    def __str__(self) -> str:
        return str(self.Tuple)

    def __repr__(self) -> str:
        return "CryptoTuple"

    def __len__(self):
        return self.Tuple.__len__()

    def __getitem__(self, index):
        return self.Tuple.__getitem__(index)

    def __contains__(self, value):
        return self.Tuple.__contains__(value)

    def __eq__(self, other):
        if isinstance(other, Tuple):
            return self.Tuple.__eq__(other)
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    def __lt__(self, other):
        if isinstance(other, Tuple):
            return self.Tuple.__lt__(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Tuple):
            return self.Tuple.__le__(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Tuple):
            return self.Tuple.__gt__(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Tuple):
            return self.Tuple.__ge__(other)
        return NotImplemented

    def __hash__(self):
        return self.Tuple.__hash__()

    def __add__(self, other):
        if isinstance(other, Tuple):
            return Tuple(self.Tuple.__add__(other))
        return NotImplemented

    def __mul__(self, count):
        return Tuple(self.Tuple.__mul__(count))

    def __rmul__(self, count):
        return Tuple(self.Tuple.__rmul__(count))

    def __getnewargs__(self):
        return self.Tuple.__getnewargs__()

    def count(self, value):
        return self.Tuple.count(value)

    def index(self, value, start=0, stop=None):
        return self.Tuple.index(value, start, stop)


class Set:
    def __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False) -> None:
        self.Set = set()
        if Type:
            self.type = Type
        else:
            self.type = obj.getType()
        if Key:
            self.key = Key
            Key = Key
        else:
            obj = Keys()
            self.Key = obj.getkey()
            Key = obj.getkey()
        self.obj = object
        temp = set()
        if BaseType:
            pass
        elif LongCrypt:
            pass
        else:
            self.Set = set(self.iters(object, Key))

    def CryptoType(self, String: str, key: str):
        if self.type == 1:
            return Encrypt(String, key)
        elif self.type == 2:
            return easyEncrypt(String, key)
        elif self.type == 3:
            return encrypt(String, key)
        elif self.type == 4:
            return RSAencrypt(String, key)

    def DeCryptoType(self, String: str, key: str):
        if self.type == 1:
            return Decrypt(String, key)
        elif self.type == 2:
            return easyDectypt(String, key)
        elif self.type == 3:
            return decrypt(String, key)
        elif self.type == 4:
            return RSAdecrypt(String, key)

    def list_to_dic(self, Keys, Values):
        res = {}
        for key in Keys:
            for value in Values:
                res[key] = value
                Values.remove(value)
                break
        return res

    def Diciters(self, obj, key, operation="en", type=list):
        temp = []
        dictemp = {}
        for i in obj:
            if isinstance(i, list):
                change = self.iters(i, key, operation, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), key, operation, tuple)
                temp.append(change)
            elif isinstance(i, str):
                return self.CryptoType(i, key)
            elif isinstance(i, set):
                change = self.iters(list(i), key, operation, set)
                temp.append(change)
            elif isinstance(i, dict):
                change = self.dict_type(i, key, operation)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ................................
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)

        if type is list:
            return temp
        elif type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)
        elif type is dict:
            return temp

    def iters(self, obj, key, operation="en", data_type=list):
        result = []
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, list) and self.type != 4 :
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de" and self.type == 4:
                        result.append(self.DeCryptoType(item, key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, tuple):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, set):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        if data_type is list:
            return result
        elif data_type is tuple:
            return tuple(result)
        elif data_type is set:
            return set(result)
        elif data_type is dict:
            return result

    def setiters(self, obj, key, operation="en", type=set):
        temp = set()
        for i in obj:
            if isinstance(i, tuple):
                change = self.setiters(i, key, operation, tuple)
                temp.add(change)
            elif isinstance(i, set):
                change = self.setiters(i, key, operation, set)
                temp.add(change)
            else:
                if (operation == "en"):
                    temp.add(i)  # ................................
                elif (operation == "de"):
                    temp.add(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.add(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.add(int(i))
                    else:
                        temp.add(i)
        if type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)

    def dict_type(self, obj, key, operation="en"):
        temp = []
        temp1 = []
        keys = obj.keys()
        values = obj.values()
        for i in values:
            if isinstance(i, list) and self.type != 4:
                change = self.iters(i, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ...# this is main line if any changes are make here all values are affected....
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
        for i in keys:
            if isinstance(i, list):
                change = self.iters(i, list)
                temp1.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), tuple)
                temp1.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp1.append(change)
            else:
                if (operation == "en"):
                    # impartent..............
                    temp1.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp1.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp1.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp1.append(int(i))
                    else:
                        temp1.append(i)
        return self.list_to_dic(temp1, temp)

    def copy(self):
        return self.Set

    def add(self, element: object):
        if isinstance(element, list):
            self.Set.add(self.iters(element, self.Key))
        elif isinstance(element, int):
            self.Set.add(self.CryptoType(str(element), self.Key))
        elif isinstance(element, str):
            self.Set.add(self.CryptoType(element, self.Key))
        elif isinstance(element, tuple):
            self.Set.add(tuple(self.iters(list(element), self.Key)))
        elif isinstance(element, set):
            self.Set.add(set(self.iters(list(element), self.Key)))
        elif isinstance(element, dict):
            self.Set.add(self.dict_type(element, self.Key))

    def to_pyset(self, key):
        orginal = self.iters(self.Set, key, "de")
        orginal = self.iters(orginal, key, "org")
        return set(orginal)

    def clear(self):
        self.Set = set()
        return self.Set

    def remove(self, element):
        if isinstance(element, list):
            obj_string = self.iters(element, self.Key, "str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, str):
            obj_string = str(element)
        elif isinstance(element, tuple):
            obj_string = tuple(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, set):
            obj_string = set(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, dict):
            obj_string = self.cleardict_type(element, self.Key, "str")
        orginal = self.iters(self.Set, self.Key, "de")
        orginal.remove(obj_string)
        self.Set = self.iters(orginal, self.Key, "en")

    def discard(self, element):
        if isinstance(element, list):
            obj_string = self.iters(element, self.Key, "str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element, str):
            obj_string = str(element)
        elif isinstance(element, tuple):
            obj_string = tuple(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, set):
            obj_string = set(self.iters(list(element), self.Key, "str"))
        elif isinstance(element, dict):
            obj_string = self.cleardict_type(element, self.Key, "str")
        orginal = set(self.iters(self.Set, self.Key, "de"))
        orginal.discard(obj_string)
        self.Set = self.iters(orginal, self.Key, "en")

    def difference(self, sets, security_key=False):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        if security_key and security_key == self.Key:
            return orginal.difference(sets)
        else:
            return set(self.iters(orginal.difference(sets), self.Key))

    def symmetric_difference(self, sets, security_key=False):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        if security_key and security_key == self.Key:
            return orginal.symmetric_difference(sets)
        else:
            return set(self.iters(orginal.symmetric_difference(sets), self.Key))

    def issuperset(self, sets, security_key=False):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        if security_key and security_key == self.Key:
            return orginal.issuperset(sets)
        else:
            return self.iters(orginal.issuperset(sets), self.Key)

    def issubset(self, sets, security_key=False):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        if security_key and security_key == self.Key:
            return orginal.issubset(sets)
        else:
            return self.iters(orginal.issubset(sets), self.Key)

    def isdisjoint(self, sets, security_key=False):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        if security_key and security_key == self.Key:
            return orginal.isdisjoint(sets)
        else:
            return self.iters(orginal.isdisjoint(sets), self.Key)

    def intersection(self, *argv, security_key=False):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        if security_key and security_key == self.Key:
            return orginal.intersection(argv)
        else:
            return set(self.iters(orginal.intersection(argv), self.Key))

    def difference_update(self, sets):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        orginal.difference_update(sets)
        self.Set = set(self.iters(orginal, self.Key))

    def update(self, sets):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        orginal.update(sets)
        self.Set = set(self.iters(orginal, self.Key))

    def symmetric_difference_update(self, sets):
        orginal = self.iters(self.Set, self.Key, "de")
        orginal = set(self.iters(orginal, self.Key, "org"))
        orginal.symmetric_difference_update(sets)
        self.Set = set(self.iters(orginal, self.Key))

    def pop(self):
        return self.Set.pop()

    def __len__(self):
        return self.Set.__len__()

    def __str__(self) -> str:
        return str(self.Set)

    def __repr__(self) -> str:
        return "CryptoSet"

    def __contains__(self, value):
        return self.Set.__contains__(value)

    def __iter__(self):
        return self.Set.__iter__()

    def __len__(self):
        return self.Set.__len__()

    def __eq__(self, other):
        if isinstance(other, Set):
            return self.Set.__eq__(other)
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    def __le__(self, other):
        if isinstance(other, Set):
            return self.Set.__le__(other)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Set):
            return self.Set.__lt__(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Set):
            return self.Set.__ge__(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Set):
            return self.Set.__gt__(other)
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, Set):
            return Set(self.Set.__and__(other))
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, Set):
            return Set(self.Set.__or__(other))
        return NotImplemented

    def __xor__(self, other):
        if isinstance(other, Set):
            return Set(self.Set.__xor__(other))
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Set):
            return Set(self.Set.__sub__(other))
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, Set):
            return Set(self.Set.__rsub__(other))
        return NotImplemented

    def add(self, elem):
        return self.Set.add(elem)

    def clear(self):
        return self.Set.clear()

    def copy(self):
        return Set(self.Set.copy())

    def difference(self, other):
        if isinstance(other, Set):
            return Set(self.Set.difference(other))
        return NotImplemented

    def difference_update(self, other):
        if isinstance(other, Set):
            return self.Set.difference_update(other)
        return NotImplemented

    def discard(self, elem):
        return self.Set.discard(elem)

    def intersection(self, other):
        if isinstance(other, Set):
            return Set(self.Set.intersection(other))
        return NotImplemented

    def intersection_update(self, other):
        if isinstance(other, Set):
            return self.Set.intersection_update(other)
        return NotImplemented

    def isdisjoint(self, other):
        if isinstance(other, Set):
            return self.Set.isdisjoint(other)
        return NotImplemented

    def issubset(self, other):
        if isinstance(other, Set):
            return self.Set.issubset(other)
        return NotImplemented

    def issuperset(self, other):
        if isinstance(other, Set):
            return self.Set.issuperset(other)
        return NotImplemented

    def pop(self):
        return self.Set.pop()

    def remove(self, elem):
        return self.Set.remove(elem)

    def symmetric_difference(self, other):
        if isinstance(other, Set):
            return Set(self.Set.symmetric_difference(other))
        return NotImplemented

    def symmetric_difference_update(self, other):
        if isinstance(other, Set):
            return self.Set.symmetric_difference_update(other)
        return NotImplemented


class String:
    def __init__(self, object: object, Key=False, Type=3, LongCrypt=False, BaseType=False) -> None:
        self.String = str()
        if Key:
            self.Key = Key
            Key = Key
        else:
            obj = Keys()
            self.Key = obj.getkey()
            Key = obj.getkey()
        self.obj = object
        if Type:
            self.type = Type
        else:
            self.type = obj.getType()
        temp = str()
        if BaseType:
            pass
        elif LongCrypt:
            pass
        else:
            self.String = self.CryptoType(object, Key)

    def CryptoType(self, String: str, key: str):
        if self.type == 1:
            return Encrypt(String, key)
        elif self.type == 2:
            return easyEncrypt(String, key)
        elif self.type == 3:
            return encrypt(String, key)
        elif self.type == 4:
            return RSAencrypt(String, key)

    def DeCryptoType(self, String: str, key: str):
        if self.type == 1:
            return Decrypt(String, key)
        elif self.type == 2:
            return easyDectypt(String, key)
        elif self.type == 3:
            return decrypt(String, key)
        elif self.type == 4:
            return RSAdecrypt(String, key)

    def list_to_dic(self, Keys, Values):
        res = {}
        for key in Keys:
            for value in Values:
                res[key] = value
                Values.remove(value)
                break
        return res

    def Diciters(self, obj, key, operation="en", type=list):
        temp = []
        dictemp = {}
        for i in obj:
            if isinstance(i, list):
                change = self.iters(i, key, operation, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), key, operation, tuple)
                temp.append(change)
            elif isinstance(i, str):
                return self.CryptoType(i, key)
            elif isinstance(i, set):
                change = self.iters(list(i), key, operation, set)
                temp.append(change)
            elif isinstance(i, dict):
                change = self.dict_type(i, key, operation)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ................................
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)

        if type is list:
            return temp
        elif type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)
        elif type is dict:
            return temp

    def iters(self, obj, key, operation="en", data_type=list):
        result = []
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, list) and self.type != 4 :
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de" and self.type == 4:
                        result.append(self.DeCryptoType(item, key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, tuple):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        elif isinstance(obj, set):
            for item in obj:
                if isinstance(item, list):
                    change = self.iters(item, key, operation, list)
                    result.append(change)
                elif isinstance(item, tuple):
                    change = self.iters(list(item), key, operation, tuple)
                    result.append(change)
                elif isinstance(item, set):
                    change = self.iters(list(item), key, operation, set)
                    result.append(change)
                elif isinstance(item, dict):
                    change = self.dict_type(item, key, operation)
                    result.append(change)
                else:
                    if operation == "en":
                        result.append(self.CryptoType(str(item), key))
                    elif operation == "de":
                        result.append(self.DeCryptoType(str(item), key))
                    elif operation == "str":
                        result.append(str(item))
                    elif operation == "org":
                        if item.isdigit():
                            result.append(int(item))
                        else:
                            result.append(item)

        if data_type is list:
            return result
        elif data_type is tuple:
            return tuple(result)
        elif data_type is set:
            return set(result)
        elif data_type is dict:
            return result

    def setiters(self, obj, key, operation="en", type=set):
        temp = set()
        for i in obj:
            if isinstance(i, tuple):
                change = self.setiters(i, key, operation, tuple)
                temp.add(change)
            elif isinstance(i, set):
                change = self.setiters(i, key, operation, set)
                temp.add(change)
            else:
                if (operation == "en"):
                    temp.add(i)  # ................................
                elif (operation == "de"):
                    temp.add(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.add(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.add(int(i))
                    else:
                        temp.add(i)
        if type is tuple:
            return tuple(temp)
        elif type is set:
            return set(temp)

    def dict_type(self, obj, key, operation="en"):
        temp = []
        temp1 = []
        keys = obj.keys()
        values = obj.values()
        for i in values:
            if isinstance(i, list):
                change = self.iters(i, list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp.append(change)
            else:
                if (operation == "en"):
                    # ...# this is main line if any changes are make here all values are affected....
                    temp.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
        for i in keys:
            if isinstance(i, list):
                change = self.iters(i, list)
                temp1.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i), tuple)
                temp1.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i), set)
                temp1.append(change)
            else:
                if (operation == "en"):
                    # impartent..............
                    temp1.append(self.CryptoType(str(i), key))
                elif (operation == "de"):
                    temp1.append(self.DeCryptoType(str(i), key))
                elif (operation == "str"):
                    temp1.append(str(i))
                elif (operation == "org"):
                    if i.isdigit():
                        temp1.append(int(i))
                    else:
                        temp1.append(i)
        return self.list_to_dic(temp1, temp)

    def capitalize(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).capitalize()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def upper(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).upper()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def lower(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).lower()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def swapcase(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).swapcase()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def title(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).title()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def casefold(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).casefold()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def istitle(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).istitle()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def zfill(self, len, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).zfill(len)
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def strip(self, character, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).strip(character)
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def center(self, length, character=False, security_key=False):
        if character == True:
            String = self.DeCryptoType(
                self.String, self.Key).center(length, character)
        else:
            String = self.DeCryptoType(self.String, self.Key).center(length)
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(String, self.Key)

    def split(self, separator, maxsplit=False, security_key=False):
        if maxsplit == True:
            String = self.DeCryptoType(
                self.String, self.Key).split(separator, maxsplit)
        else:
            String = self.DeCryptoType(self.String, self.Key).split(separator)
        if security_key and security_key == self.Key:
            return String
        else:
            return self.iters(String, self.Key)

    def isalnum(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isalnum()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isalpha(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isalpha()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isascii(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isascii()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isdecimal(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isdecimal()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isdigit(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isdigit()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isidentifier(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isidentifier()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def islower(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).islower()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isnumeric(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isnumeric()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isprintable(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isprintable()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def isspace(self, security_key=False):
        String = self.DeCryptoType(self.String, self.Key).isspace()
        if security_key and security_key == self.Key:
            return String
        else:
            return self.CryptoType(str(String), self.Key)

    def find(self, value, start=False, end=False):
        if start == False and end == False:
            String = self.DeCryptoType(self.String, self.Key).find(value)
        elif end == False:
            String = self.DeCryptoType(
                self.String, self.Key).find(value, start)
        if start == False and end == False:
            String = self.DeCryptoType(
                self.String, self.Key).find(value, start, end)
        return String

    def topystr(self, key) -> str:
        if key == self.Key:
            return self.DeCryptoType(self.String, self.Key)
        elif self.type == 4:
            return self.DeCryptoType(self.String, key)
        else:
            return self.String

    def __str__(self) -> str:
        return str(self.String)

    def __repr__(self) -> str:
        return "CryptoString"

    def __getitem__(self, index):
        return self.String.__getitem__(index)

    def __contains__(self, value):
        return self.String.__contains__(value)

    def __iter__(self):
        return self.String.__iter__()

    def __len__(self):
        return self.String.__len__()

    def __add__(self, other):
        if isinstance(other, String):
            return String(self.String.__add__(other))
        return NotImplemented

    def __mul__(self, count):
        return String(self.String.__mul__(count))

    def __rmul__(self, count):
        return String(self.String.__rmul__(count))

    def __eq__(self, other):
        if isinstance(other, String):
            return self.String.__eq__(other)
        return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        return not result

    def __lt__(self, other):
        if isinstance(other, String):
            return self.String.__lt__(other)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, String):
            return self.String.__le__(other)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, String):
            return self.String.__gt__(other)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, String):
            return self.String.__ge__(other)
        return NotImplemented

    def __hash__(self):
        return self.String.__hash__()

    def capitalize(self):
        return String(self.String.capitalize())

    def casefold(self):
        return String(self.String.casefold())

    def center(self, width, fillchar=' '):
        return String(self.String.center(width, fillchar))

    def count(self, sub, start=0, end=None):
        return self.String.count(sub, start, end)

    def encode(self, encoding='utf-8', errors='strict'):
        return self.String.encode(encoding, errors)

    def endswith(self, suffix, start=0, end=None):
        return self.String.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return String(self.String.expandtabs(tabsize))

    def find(self, sub, start=0, end=None):
        return self.String.find(sub, start, end)

    def format(self, *args, **kwargs):
        return String(self.String.format(*args, **kwargs))

    def format_map(self, mapping):
        return String(self.String.format_map(mapping))

    def index(self, sub, start=0, end=None):
        return self.String.index(sub, start, end)

    def isalnum(self):
        return self.String.isalnum()

    def isalpha(self):
        return self.String.isalpha()

    def isdecimal(self):
        return self.String.isdecimal()

    def isdigit(self):
        return self.String.isdigit()

    def isidentifier(self):
        return self.String.isidentifier()

    def islower(self):
        return self.String.islower()

    def isnumeric(self):
        return self.String.isnumeric()

    def isprintable(self):
        return self.String.isprintable()

    def isspace(self):
        return self.String.isspace()

    def istitle(self):
        return self.String.istitle()

    def isupper(self):
        return self.String.isupper()

    def join(self, iterable):
        return String(self.String.join(iterable))


class Int:
    def __init__(self, value, key=False, Type=3):
        if Type:
            self.type = Type
        else:
            self.type = obj.getType()
        if key:
            self.key = key
            self.Key = self.key
            key = self.key
            Key = self.key
        else:
            obj = Keys()
            self.Key = obj.getkey()
            self.key = obj.getkey()
            Key = obj.getkey()
            Key = obj.getkey()
        if self.type==4:
            self.value = self.CryptoType(str(value), key)
        else:
            self.value = self.CryptoType(value, key)

    def CryptoType(self, String: str, key: str):
        if self.type == 1:
            return Encrypt(String, key)
        elif self.type == 2:
            return easyEncrypt(String, key)
        elif self.type == 3:
            return encrypt(String, key)
        elif self.type == 4:
            return RSAencrypt(String, key)

    def DeCryptoType(self, String: str, key: str):
        if self.type == 1:
            return Decrypt(String, key)
        elif self.type == 2:
            return easyDectypt(String, key)
        elif self.type == 3:
            return decrypt(String, key)
        elif self.type == 4:
            return RSAdecrypt(String, key)

    def get_int(self, key):
        if key == self.key:
            return self.DeCryptoType(self.value, self.Key)
        elif self.type == 4:
            return self.DeCryptoType(self.value, key)

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
