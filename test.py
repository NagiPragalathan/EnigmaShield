# from data import CryptoOperation as cp

# a = cp.array([1,2,3,1,(1,2),(1,2),(1,5),8],"key")
# a.add("hel1lo")
# a.add("nagi")
# a.add([1,2,3])
# a.add([1,2,3])


# print(a)
# print(type(a))
# print(type(str()))

# print(a.count((1,2)),"count")

# print(isinstance([], list))

# b=[[1,2],[1,2],(1,2),(1,2)]

# print(b.count((1,2)))

arr=[]
temp=[]
obj = [[1,2],[1,[2,[1,2]],[1,2,[1,2],2]],[1],{1,3},(1,2),{1:"2","2":4,3:"5",'b':[1,2,3],"h":{1,2}}]

# # for i in obj :
#     if isinstance(i, list):
#         for j in i :
#             temp.append(j)
#         arr.append(temp)
#         temp=[]
def list_to_dic(Keys,Values):
    res = {}
    for key in Keys:
        for value in Values:
            res[key] = value
            Values.remove(value)
            break
    return res

def iters(obj,type):
    temp = []
    dickey = []
    dicvalue = []
    new=[]
    for i in obj :
        if isinstance(i, list):
            change = iters(i,list)
            temp.append(change)
        elif isinstance(i, set):
            change = iters(i,set)
            temp.append(change)
        elif isinstance(i, tuple):
            change = iters(i,tuple)
            temp.append(change)
        elif isinstance(i, dict):
            keys = i.keys()
            value = i.values()
            for i in keys:
                if isinstance(i, list):
                    change = iters(i,list)
                    dickey.append(change)
                elif isinstance(i, set):
                    change = iters(i,set)
                    dickey.append(change)
                elif isinstance(i, tuple):
                    change = iters(i,tuple)
                    dickey.append(change)
                elif isinstance(i, dict):
                    change = iters(i,dict)
                    temp.append(change)
                else:
                    dickey.append(i) #.....main
            for i in value:
                if isinstance(i, list):
                    change = iters(i,list)
                    dicvalue.append(change)
                elif isinstance(i, set):
                    change = iters(i,set)
                    dicvalue.append(change)
                elif isinstance(i, tuple):
                    change = iters(i,tuple)
                    dicvalue.append(change)
                elif isinstance(i, dict):
                    print("yes")
                    change = iters(i,dict)
                    temp.append(change)
                else:
                    dicvalue.append(i) #.....main
            print(dicvalue,dickey)
            new = list_to_dic(list(dickey),list(dicvalue))
            change = iters(i,dict)
            temp.append(new)
        else:
            temp.append(chr(i)) # this is main line if any changes are make here all values are affected....

    
    if type == list:
        return temp
    elif type == set:
        return set(temp)
    elif type == tuple:
        return tuple(temp)
    elif type == dict:
        return temp


print(iters(obj,list))
