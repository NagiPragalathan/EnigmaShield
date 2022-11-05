import string
from .EnCrypt import Encrypt, Decrypt
from ctypes import Array
from random import choice

class Tools :
    def __init__(self) -> None:
        self.res = {}
    def list_to_dic(self,Keys,Values):
        res = {}
        for key in Keys:
            for value in Values:
                res[key] = value
                Values.remove(value)
                break
        return res


    def iters(self,obj,type=list):
        temp = []
        dictemp = {}
        if isinstance(obj, list):
            for i in obj:
                if isinstance(i, list):
                    change = self.iters(i,list)
                    temp.append(change)
                elif isinstance(i, tuple):
                    change = self.iters(list(i),tuple)
                    temp.append(change)
                elif isinstance(i, set):
                    change = self.iters(list(i),set)
                    temp.append(change)
                elif isinstance(i, dict):
                    change = self.dict_type(i)
                    temp.append(change)
                else:
                    temp.append(Encrypt(str(i),"key")) #................................
        if type is list:
            return temp
        elif type is tuple:
            print("working")
            return tuple(temp)
        elif type is set :
            return set(temp)
        elif type is dict :
            return temp
        


    def dict_type(self,obj):
        temp=[]
        temp1=[]
        keys = obj.keys()
        values = obj.values()
        for i in values:
            if isinstance(i, list):
                change = self.iters(i,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i),tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i),set)
                temp.append(change)
            else:
                temp.append(Encrypt(str(i),"key")) #...# this is main line if any changes are make here all values are affected....
        for i in keys:
            if isinstance(i, list):
                change = self.iters(i,list)
                temp1.append(change)
            elif isinstance(i, tuple):
                change = self.iters(list(i),tuple)
                temp1.append(change)
            elif isinstance(i, set):
                change = self.iters(list(i),set)
                temp1.append(change)
            else:
                temp.append(Encrypt(str(i),"key")) # impartent..............
        return self.list_to_dic(temp1,temp)

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
                    self.Arrays.append(Encrypt(str(i),self.Key))
    

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
            self.Arrays.append(Encrypt(str(element),self.Key))
    
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
    
    def to_string(self,obj):
        temp = list()
        temp_1 = list()
        for i in obj:
            if isinstance(i, list):
                for j in i :
                    temp.append(Encrypt(str(j),self.Key))
                temp_1.append(temp)
                temp.append(str(temp_1))
                temp_1 = []

            elif isinstance(i, tuple):
                for j in i :
                    temp.append(Encrypt(str(j),self.Key))
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

    def count(self,Object:object):
        obj=Tools()
        count_is=0
        hash=obj.Deiters(self.Arrays,list,self.Key)
        print(hash,Object)
        if isinstance(Object, int):
            count_is = hash.count(str(Object))
        elif isinstance(Object, list):
            count_is = hash.count(self.to_string(Object))
        elif isinstance(Object, set):
            count_is = hash.count(set(self.to_string(Object)))
        elif isinstance(Object, tuple):
            count_is = hash.count(tuple(self.to_string(list(Object))))
        elif isinstance(Object, string):
            count_is = hash.count(Object)
            
        return count_is

    def __str__(self) -> str:
        return str(self.Arrays)

    def __repr__(self) -> str:
        return "CryptoArray"

class Set :
    def __init__(self,object : object, Key=False, LongCrypt=False, BaseType=False) -> None:
        self.sets = {}
        self.Key = Key
        self.obj = object
        temp = []
        if BaseType :
            pass
        elif LongCrypt:
            pass
        else:
            for i in self.obj :
                if isinstance(i, tuple):
                    obj=Tools()
                    hash=obj.setiters(i,tuple,self.Key)
                    self.sets.add(hash)
                if isinstance(i, set):
                    obj=Tools()
                    hash=obj.setiters(i,set,self.Key)
                    self.sets.add(hash)
                else :
                    self.sets.add(Encrypt(str(i),self.Key))
    def __str__(self) -> str:
        return str(self.sets)

    def __repr__(self) -> str:
        return "CryptoArray"


                 
