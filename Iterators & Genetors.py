#Iterator
from operator import index

'''
class A:
    def __init__(self,s,e):
        self.s=s
        self.e=e
    def __iter__(self):
        return self
    def __next__(self):
        if self.s>self.e:
            raise StopIteration
        n=self.s
        self.s+=1
        return n
obj=A(1,8)
for i in obj:
    print(i)

'''
#2.iterator
#Q:even number from list

class EvenIterator:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.lst):
            raise StopIteration

        value = self.lst[self.index]
        self.index += 1

        if value % 2 == 0:
            return value
        return self.__next__()
numbers = EvenIterator([1, 2, 3, 4, 5, 6])

for i in numbers:
    print(i)

#3.Reverse of a string
class Rever:
    def __init__(self, a):
        self.a = a
        self.index = len(a) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        rev = self.a[self.index]
        self.index -= 1
        return rev

r = "python"
obj = Rever(r)

for i in obj:
    print(i)

#4.Write an iterator that yields element of list with their index
class Index:
    def __init__(self,x):
        self.x=x
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.x):
            raise StopIteration
        res=(self.index,self.x[self.index])
        self.index+=1
        return res
h=Index(["n","i","k","h","i","t","h","a"])
for i in h:
    print(i)

#5.Write a generator that yields digits from an integer one by one.

def fun():
    for i in s:
        yield(i)
s=[1,2,3,4,5]
g=fun()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

#6.Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6




