def add():
    a = 10
    b = 20
    c = a + b
    print("the value of c is {}".format(c))
add()

def add(a,b):
    c = a + b
    print("the value of c is {}".format(c))
add(1,4)


def f1(c1,c2,c3):
    print("I need the value from c2 {}".format(c2))
f1(1,2,3)
# or f1(c1=1,c2=2,c3=3)

#kwargs need to pass ** before the parameter for the functions if we dont know number of args passed

def f2(**a1):
    print("second arg is {}".format(a1["second"]))
f2(first = 1,second=2,third=3)

# List as an Argument

def l1(s):
    print(s)
sports = ["cricket","football","Hockey"]
l1(sports)

def l2(s):
    for i in s:
        print(i)
l2(sports)

def table(i):
    while i <= 10:
        j = 5 * i
        print("5 * {} = {}".format(i,j))
        i += 1 
    else:
        print("Wrong function")
table(1)
