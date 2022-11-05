import string
from .EnCrypt import easyEncrypt, easyDectypt
from ctypes import Array
from random import choice

class Tools :
    def __init__(self) -> None:
        self.res = {}
    def list_to_dic(self,Keys,Values):
        for key in Keys:
            for value in Values:
                self.res[key] = value
                Values.remove(value)
                break
        return self.res

    def iters(self,obj,type,Key):
        temp = []
        for i in obj :
            if isinstance(i, list):
                change = self.iters(i,list,Key)
                temp.append(change)
            elif isinstance(i, set):
                change = self.iters(i,set,Key)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(i,tuple,Key)
                temp.append(change)
            else:
                temp.append(easyEncrypt(str(i),Key)) # this is main line if any changes are make here all values are affected....
        if type == list:
            return temp
        elif type == set:
            return set(temp)
        elif type == tuple:
            return tuple(temp)

    def Deiters(self,obj,type,Key):
        temp = []
        for i in obj :
            if isinstance(i, list):
                change = self.Deiters(i,list,Key)
                temp.append(change)
            elif isinstance(i, set):
                change = self.Deiters(i,set,Key)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.Deiters(i,tuple,Key)
                temp.append(change)
            else:
                temp.append(easyDectypt(str(i),Key)) # this is main line if any changes are make here all values are affected....
        if type == list:
            return temp
        elif type == set:
            return set(temp)
        elif type == tuple:
            return tuple(temp)
            
    def Deiters(self,obj,type,Key):
        temp = []
        for i in obj :
            if isinstance(i, list):
                change = self.Deiters(i,list,Key)
                temp.append(change)
            elif isinstance(i, set):
                change = self.Deiters(i,set,Key)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.Deiters(i,tuple,Key)
                temp.append(change)
            else:
                temp.append(easyDectypt(str(i),Key)) # this is main line if any changes are make here all values are affected....
        if type == list:
            return temp
        elif type == set:
            return set(temp)
        elif type == tuple:
            return tuple(temp)
    
    def TwoD_to_string(self,obj):
        temp = list()
        temp_1 = list()
        for i in obj:
            if isinstance(i, list):
                for j in i :
                    temp.append(easyEncrypt(str(j),self.Key))
                temp_1.append(temp)
                temp.append(str(temp_1))
                temp_1 = []

            elif isinstance(i, tuple):
                for j in i :
                    temp.append(easyEncrypt(str(j),self.Key))
                temp_1.append(tuple(temp))
                temp.append(str(temp_1))
                temp_1 = []
            elif isinstance(i, set):
                for j in i :
                    temp.append(easyEncrypt(str(j),self.Key))
                temp_1.append(set(temp))
                temp.append(str(temp_1))
                temp_1 = []
            else:
                temp_1.append(str(i))
        return temp_1

    def to_string(self,obj,type):
        temp = []
        for i in obj :
            if isinstance(i, list):
                change = self.to_string(i,list)
                temp.append(change)
            elif isinstance(i, set):
                change = self.to_string(i,set)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.to_string(i,tuple)
                temp.append(change)
            else:
                temp.append(str(str(i))) # this is main line if any changes are make here all values are affected....
        if type == list:
            return temp
        elif type == set:
            return set(temp)
        elif type == tuple:
            return tuple(temp)

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
            for i in self.obj :
                if isinstance(i, list):
                    obj=Tools()
                    hash=obj.iters(i,list,self.Key)
                    self.Arrays.append(hash)
                if isinstance(i, tuple):
                    obj=Tools()
                    hash=obj.iters(i,tuple,self.Key)
                    self.Arrays.append(hash)
                if isinstance(i, set):
                    obj=Tools()
                    hash=obj.iters(i,set,self.Key)
                    self.Arrays.append(hash)
                else :
                    self.Arrays.append(easyEncrypt(str(i),self.Key))
    

    def add(self,element : object) -> Array :
        if isinstance(element, list):
            obj=Tools()
            hash=obj.iters(element,list,self.Key)
            self.Arrays.append(hash)
        if isinstance(element, tuple):
            obj=Tools()
            hash=obj.iters(element,tuple,self.Key)
            self.Arrays.append(hash)
        if isinstance(element, set):
            obj=Tools()
            hash=obj.iters(element,set,self.Key)
            self.Arrays.append(hash)
        else :
            self.Arrays.append(easyEncrypt(str(element),self.Key))
    
    def to_pyarray(self,Key):
        if Key == self.Key :
            return self.Arrays
        else:
            return None

    def len(self):
        return len(self.Arrays)
    
    def clear(self):
        self.Arrays = []
        return self.Arrays
    
    def copy(self):
        return self.Arrays

    def count(self,Object:object):
        obj=Tools()
        count_is=0
        hash=obj.Deiters(self.Arrays,list,self.Key)
        print(hash,Object)
        if isinstance(Object, int):
            count_is = hash.count(str(Object))
        elif isinstance(Object, list):
            count_is = hash.count(obj.to_string(Object,list))
        elif isinstance(Object, set):
            count_is = hash.count(set(obj.to_string(Object,set)))
        elif isinstance(Object, tuple):
            count_is = hash.count(tuple(obj.to_string(list(Object,tuple))))
        elif isinstance(Object, string):
            count_is = hash.count(Object)
            
        return count_is

    def __str__(self) -> str:
        return str(self.Arrays)

    def __repr__(self) -> str:
        return "CryptoArray"