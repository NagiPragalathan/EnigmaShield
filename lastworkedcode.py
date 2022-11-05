from .EnCrypt import Encrypt, Decrypt

def list_to_dic(Keys,Values):
    res = {}
    for key in Keys:
        for value in Values:
            res[key] = value
            Values.remove(value)
            break
    return res


def iters(obj,key,operation="en",type=list):
    temp = []
    dictemp = {}
    for i in obj:
        if isinstance(i, list):
            change = iters(i,key,operation,list)
            temp.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),key,operation,tuple)
            temp.append(change)
        elif isinstance(i, str):
            return Encrypt(i,key)
        elif isinstance(i, set):
            change = iters(list(i),key,operation,set)
            temp.append(change)
        elif isinstance(i, dict):
            change = dict_type(i,key,operation)
            temp.append(change)
        else:
            if ( operation == "en" ) :
                temp.append(Encrypt(str(i),key)) #................................
            elif ( operation == "de" ) :
                temp.append(Decrypt(str(i),key))
            elif ( operation == "str" ) :
                temp.append(str(i))
            elif ( operation == "org" ) :
                if i.isdigit():
                    temp.append(int(i))
                else:
                    temp.append(i)
                    
    if type is list:
        return temp
    elif type is tuple:
        return tuple(temp)
    elif type is set :
        return set(temp)
    elif type is dict :
        return temp


def setiters(obj,key,operation="en",type=set):
    temp = set()
    for i in obj:
        if isinstance(i, tuple):
            change = setiters(i,key,operation,tuple)
            temp.add(change)
        elif isinstance(i, set):
            change = setiters(i,key,operation,set)
            temp.add(change)
        else:
            if ( operation == "en" ) :
                temp.add(i) #................................
            elif ( operation == "de" ) :
                temp.add(Decrypt(str(i),key))
            elif ( operation == "str" ) :
                temp.add(str(i))
            elif ( operation == "org" ) :
                if i.isdigit():
                    temp.add(int(i))
                else:
                    temp.add(i) 
    if type is tuple:
        return tuple(temp)
    elif type is set :
        return set(temp)
    


def dict_type(obj,key,operation="en"):
    temp=[]
    temp1=[]
    keys = obj.keys()
    values = obj.values()
    for i in values:
        if isinstance(i, list):
            change = iters(i,list)
            temp.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),tuple)
            temp.append(change)
        elif isinstance(i, set):
            change = iters(list(i),set)
            temp.append(change)
        else:
            if ( operation == "en" ) :
                temp.append(Encrypt(str(i),key)) #...# this is main line if any changes are make here all values are affected....
            elif ( operation == "de" ) :
                temp.append(Decrypt(str(i),key))
            elif ( operation == "str" ) :
                temp.append(str(i))
            elif ( operation == "org" ) :
                    if i.isdigit():
                        temp.append(int(i))
                    else:
                        temp.append(i)
    for i in keys:
        if isinstance(i, list):
            change = iters(i,list)
            temp1.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),tuple)
            temp1.append(change)
        elif isinstance(i, set):
            change = iters(list(i),set)
            temp1.append(change)
        else:
            if(operation == "en" ):
                temp1.append(Encrypt(str(i),key)) # impartent..............
            elif(operation == "de" ):
                temp1.append(Decrypt(str(i),key))
            elif(operation == "str" ):
                temp1.append(str(i))
            elif ( operation == "org" ) :
                    if i.isdigit():
                        temp1.append(int(i))
                    else:
                        temp1.append(i)
    return list_to_dic(temp1,temp)



class array :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.Arrays = []
        self.Key = Key
        self.obj = object
        temp = []
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            self.Arrays = iters(object,Key)

    def add(self,element : object) :
        if isinstance(element, list):
            self.Arrays.append(iters(element,self.Key))
        elif isinstance(element, int):
            self.Arrays.append(Encrypt(str(element),self.Key))
        elif isinstance(element, str):
            self.Arrays.append(Encrypt(element,self.Key))
        elif isinstance(element,tuple):
            self.Arrays.append(tuple(iters(list(element),self.Key)))
        elif isinstance(element,set):
            self.Arrays.append(set(iters(list(element),self.Key)))
        elif isinstance(element,dict):
            self.Arrays.append(dict_type(element,self.Key))

    def extend(self,iterable):
        for i in iterable:
            self.add(i)
    
    def index(self,object):
        if isinstance(object, list):
            obj_string = iters(object,self.Key,"str")
        elif isinstance(object, int):
            obj_string = str(object)
        elif isinstance(object,tuple):
            obj_string = tuple(iters(list(object),self.Key,"str"))
        elif isinstance(object,set):
            obj_string = set(iters(list(object),self.Key,"str"))
        elif isinstance(object,dict):
            obj_string = dict_type(object,self.Key,"str")
        orginal = iters(self.Arrays,self.Key,"de")
        index_is = orginal.index(obj_string)
        return index_is

    def len(self):
        return len(self.Arrays)

    def clear(self):
        self.Arrays = []
        return self.Arrays
    
    def copy(self):
        return self.Arrays

    def to_pyarray(self,key):
        orginal = iters(self.Arrays,key,"de")
        orginal = iters(orginal,key,"org")
        return orginal

    def insert(self,index,object):
        if isinstance(object, list):
            self.Arrays.insert(index,iters(object,self.Key))
        elif isinstance(object, int):
            self.Arrays.insert(index,Encrypt(str(object),self.Key))
        elif isinstance(object, str):
            self.Arrays.insert(index,Encrypt(object,self.Key))
        elif isinstance(object,tuple):
            self.Arrays.insert(index,tuple(iters(list(object),self.Key)))
        elif isinstance(object,set):
            self.Arrays.insert(index,set(iters(list(object),self.Key)))
        elif isinstance(object,dict):
            self.Arrays.insert(index,dict_type(object,self.Key))

    def count(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = iters(self.Arrays,self.Key,"de")
        count_is = orginal.count(obj_string)
        return count_is
    
    def remove(self,element):
        if isinstance(element, list):
            obj_string = iters(element,self.Key,"str")
        elif isinstance(element, int):
            obj_string = str(element)
        elif isinstance(element,tuple):
            obj_string = tuple(iters(list(element),self.Key,"str"))
        elif isinstance(element,set):
            obj_string = set(iters(list(element),self.Key,"str"))
        elif isinstance(element,dict):
            obj_string = dict_type(element,self.Key,"str")
        orginal = iters(self.Arrays,self.Key,"de")
        orginal.remove(obj_string)
        self.Arrays = iters(orginal,self.Key,"en")
    
    def reverse(self):
        self.Arrays = self.Arrays[::-1]
    
    def sort(self,key=False,reverse=False):
        obj_string = self.to_pyarray(self.Key)
        if key and reverse :
            self.Arrays = obj_string.sort(key,reverse)
        elif reverse:
            self.Arrays = obj_string.sort(reverse)
        elif key:
            self.Arrays = obj_string.sort(key)
        else:
            self.Arrays = obj_string.sort()
    
    def pop(self,index):
        self.Arrays.pop(index)

    def __str__(self) -> str:
        return str(self.Arrays)

    def __repr__(self) -> str:
        return "CryptoArray"


class Dict :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.Dict = dict()
        self.Key = Key
        self.obj = object
        temp = dict()
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            self.Dict = dict_type(object,Key)
    
    def add(self,key,value):
        self.Dict[Encrypt(key,self.Key)] = Encrypt(value, self.Key)
    
    def clear(self):
        self.Dict = dict()
    
    def copy(self):
        return self.Dict
    
    def to_pyDict(self,key):
        orginal_str = dict_type(self.Dict,key,"de") 
        orginal = dict_type(orginal_str,key,"org")
        return orginal

    def get(self,key,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.get(key)
        else:
            return Encrypt(str(orginalDic.get(key)),self.Key)

    def items(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.items()
        else:
            return iters(orginalDic.items(),self.Key)
            
    def keys(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.keys()
        else:
            return iters(orginalDic.keys(),self.Key)
    
    def values(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.values()
        else:
            return iters(orginalDic.values(),self.Key)
    
    def setdefault(self,keyname, value, security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        if security_key and security_key == self.Key:
            return orginalDic.setdefault(keyname,value)
        else:
            return iters(orginalDic.setdefault(keyname,value),self.Key)
    
    def popitem(self,security_key=False):
        orginalDic  = dict_type(self.Dict,self.Key,"de")
        orginalDic = dict_type(orginalDic,self.Key,"org")
        org = list(orginalDic.popitem())
        encry = iters(org,self.Key)
        if security_key and security_key == self.Key:
            return org
        else:
            return encry
    

    def from_keys(self,key,value=False,security_key=False):
        if value:
            fromdic_ = dict.fromkeys(key,value)
        else:
            fromdic_ = dict.fromkeys(security_key)
        returntype = dict_type(fromdic_,security_key)
        return returntype


    def __str__(self) -> str:
        return str(self.Dict)

    def __repr__(self) -> str:
        return "CryptoSet"

