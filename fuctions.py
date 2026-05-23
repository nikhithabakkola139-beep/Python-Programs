
#alternative sum of numbers
def fun5(*s):
    a1=0
    c=0
    for i in s:
        if c%2==0:
            a1+=i
        c+=1
    print(a1)
fun5(10,15,7,6,8)


