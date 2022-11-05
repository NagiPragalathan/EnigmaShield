
obj = [1,2,3,[1,2,[74,3,{1,2,(1,2)}]],(1,2),{1,2}]

def iters(obj,type=list):
    temp = []
    if isinstance(obj, list):
        for i in obj:
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
                temp.append(i)
            
    if type is list:
        return temp
    elif type is tuple:
        print("working")
        return tuple(temp)
    elif type is set :
        return set(temp)
print(iters(obj,list))
 








 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
 
from data.EnCrypt import easyEncrypt

obj = [1,2,3,[1,2,[74,3,{1,2,(1,2)}]],(1,2),{1,2},{1:[1,3]},{2:[1,3]}]

def list_to_dic(Keys,Values):
    res = {}
    for key in Keys:
        for value in Values:
            res[key] = value
            Values.remove(value)
            break
    return res


def iters(obj,type=list,key="key"):
    if not key :
        key="key"
    temp = []
    dictemp = {}
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, list):
                change = iters(i,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = iters(list(i),tuple)
                temp.append(change)
            elif isinstance(i, set):
                change = iters(list(i),set)
                temp.append(change)
            elif isinstance(i, dict):
                change = dict_type(i,key)
                temp.append(change)
            else:
                temp.append(easyEncrypt(str(i),key)) #................................
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
            change = iters(i,list)
            temp.append(change)
        elif isinstance(i, tuple):
            change = iters(list(i),tuple)
            temp.append(change)
        elif isinstance(i, set):
            change = iters(list(i),set)
            temp.append(change)
        else:
            temp.append(easyEncrypt(str(i),key)) #...# this is main line if any changes are make here all values are affected....
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
            temp1.append(i) # impartent..............
    return list_to_dic(temp1,temp)


print(iters(obj))
 

 #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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
                if ( operation == "en" ) :
                    temp.append(Encrypt(str(i),key)) #................................
                elif ( operation == "de" ) :
                    temp.append(Decrypt(str(i),key))
    if type is list:
        return temp
    elif type is tuple:
        print("working")
        return tuple(temp)
    elif type is set :
        return set(temp)
    elif type is dict :
        return temp
    


def dict_type(obj,key,operation="en"):
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
            if ( operation == "en" ) :
                temp.append(Encrypt(str(i),key)) #...# this is main line if any changes are make here all values are affected....
            elif ( operation == "de" ) :
                temp.append(Decrypt(str(i),key))
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
            if ( operation == "en" ) :
                temp.append(Encrypt(str(i),key)) #...# this is main line if any changes are make here all values are affected....
            elif ( operation == "de" ) :
                temp.append(Decrypt(str(i),key))
    return list_to_dic(temp1,temp)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, list):
                change = iters(i,key,operation,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = iters(list(i),key,operation,tuple)
                temp.append(change)
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
    if type is list:
        return temp
    elif type is tuple:
        print("working")
        return tuple(temp)
    elif type is set :
        return set(temp)
    elif type is dict :
        return temp
    


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

    return list_to_dic(temp1,temp)

    #?>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def iters(obj,key,operation="en",type=list):
    temp = []
    dictemp = {}
    if isinstance(obj, list):
        for i in obj:
            if isinstance(i, list):
                change = iters(i,key,operation,list)
                temp.append(change)
            elif isinstance(i, tuple):
                change = iters(list(i),key,operation,tuple)
                temp.append(change)
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
    if type is list:
        return temp
    elif type is tuple:
        print("working")
        return tuple(temp)
    elif type is set :
        return set(temp)
    elif type is dict :
        return temp
    


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

    return list_to_dic(temp1,temp)

