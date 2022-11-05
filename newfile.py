
from data.EnCrypt import Encrypt,Decrypt

obj = [1,2,3,[1,2,[74,3,{1,2,(1,2)}]],(1,2),{1,2},{1:[1,3]},{2:[1,3]}]

def list_to_dic(Keys,Values):
    res = {}
    for key in Keys:
        for value in Values:
            res[key] = value
            Values.remove(value)
            break
    return res


def iters(obj,key,type=list):
    temp = []
    dictemp = {}
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, list):
                change = iters(i,key,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = iters(list(i),key,tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = iters(list(i),key,set)
                temp.append(change)
            elif isinstance(i, dict):
                change = dict_type(i,key)
                temp.append(change)
            else:
                temp.append(Encrypt(str(i),key)) #................................
    if type is list:
        return temp
    elif type is tuple:
        print("working")
        return tuple(temp)
    elif type is set :
        return set(temp)
    elif type is dict :
        return temp
    


def dict_type(obj,key):
    temp=[]
    temp1=[]
    keys = obj.keys()
    values = obj.values()
    for i in values:
        if isinstance(i, list):
            change = iters(i,key,list)
            temp.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),key,tuple)
            temp.append(change)
        elif isinstance(i, set):
            change = iters(list(i),key,set)
            temp.append(change)
        else:
            temp.append(Encrypt(str(i),key)) #...# this is main line if any changes are make here all values are affected....
    for i in keys:
        if isinstance(i, list):
            change = iters(i,key,list)
            temp1.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),key,tuple)
            temp1.append(change)
        elif isinstance(i, set):
            change = iters(list(i),key,set)
            temp1.append(change)
        else:
            temp1.append(Encrypt(str(i),key)) # impartent..............
    return list_to_dic(temp1,temp)


print(iters(obj,"hello"))

print(Decrypt("&3afecghbd$4cfdhbag_0ifaced+3ifcdea$7figaed&0bchadgife&4iagfhbed","hello1"))