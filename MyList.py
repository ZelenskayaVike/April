# encoding: utf-8
# module _testcapi
# from C:\Users\Vika\AppData\Local\Programs\Python\Python311\DLLs\_testcapi.pyd
# by generator 1.147
# no doc
# no imports

from .list import list

class MyList(list):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# 1) first
a=3
print(a)
b=4
print(b)
# # 2) Second
z=4
# z=input(a==b)
# print(z)
# 3) third
my=a==b
print(my)
# 4) foth
print("my"+str(b-a))
# 5) fifth
thislist = [a, b, z, my]
# 6 six
print(thislist)
setList=set(thislist)
print(setList)
# 7) seven
myTupl = ("one", "two", "three")
d=("a","b","c")
print(myTupl)
print(d)
# 8) eight
r=myTupl+d
print(r)
# 9) nine
s=list(r)
print(s)
# 10) ten

myFloat=float(2)
MyT1 = ("apple", "banana", "cherry")
MyT2=("one","two","three")
Mydict = {
  "number": 29,
  "electric": "False",
  29: "color",
    True:None,
    True:["one","two", "three"],
    myFloat:{ "electric": "False", 23:24},
    "colors": ["red", "white", "blue"],
    MyT2:MyT1
}
print(Mydict)