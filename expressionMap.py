import re



def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b


def fetcher(args):
    ops={
        '+':add,
        '-':sub,
        '*':mul,
        '/':div
    }

    foo=ops.get(args, lambda: "Invalid op")
    return foo
############################################################################################################################
precedences = {'+' : 1, '-' : 0, '*' : 2, '/' : 3}
itr = {'+' : 0, '-' : 0, '*' : 0, '/' : 0}

def fnc(x):
    i = op_l.index(x)
    a = num_l.pop(i)
    b = num_l.pop(i)
    ff = fetcher(x)
    ans = ff(a, b)
    num_l.insert(i, ans)
    itr[x] -= 1
    op_l.pop(i)
def itr_count(x):
    itr[x] = 1 + itr[x]
    return

def func(x):
    if( x == '/' and itr[x] !=0 ):
        fnc(x)
    elif(x == '*' and itr['/']==0 and itr[x]!=0 ) :
        fnc(x)
    elif(x == '+' and itr['*'] == 0 and itr['/'] ==0 and itr[x]!=0):
       fnc(x)
    elif (x == '-' and itr['+']==0 and itr['*'] == 0 and itr['/'] == 0 and itr[x] != 0):
       fnc(x)
    #print(num_l)
    return

inp=input("enter expression ")

inp= re.split("([+-/*])",inp)

n=list( filter(lambda x: x.isdigit(),inp ))
o= [ pp for pp in inp if pp not in n  ]
n=list(map( lambda x: int(x),n))
num_l=[20,10,30,20,10,2]
op_l=['-','*','-','/','*']
emptu_l=list( map(itr_count,o))
print(itr)
num_l=n
op_l=o
while(len(num_l)!=1):
    ll=list(map(func,op_l))

#print(ll)
print(*num_l)
#print(n)
#print(o)