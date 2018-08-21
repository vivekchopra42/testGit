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

##################################################################################################################################################################
prec={'+':1, '-':1, '*':2, '/':2}
inp=input("enter expression ")

inp= re.split("([+-/*])",inp)
pfix_l=[]
op=[]

def postfix(x):
        if x.isdigit():
            pfix_l.append(x)
        else:
            while( len(op)!=0 and prec[ op[-1] ] >= prec[x] ):
                pfix_l.append( op.pop() )
            op.append(x)


l=list(map(postfix,inp))

while( len(op)!=0):
    pfix_l.append(op.pop())

print(pfix_l)


##################################################################################################################################################################
num=[]
def sol(x):
    if x.isdigit():
        num.append(x)
    else:
        action = fetcher(x)
        a=int(num.pop())
        b=int(num.pop())
        num.append( str( int(action(b,a) )  ) )
    print(num)

    return
#postfix_exp=['20','10','30','*','-','20','10','/','2','*','-']
l=list(map(sol,pfix_l))
print(*num)
#def