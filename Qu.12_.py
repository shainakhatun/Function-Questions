# Q12.Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105

def num(a,b,c,d):
    i=0
    b=[]
    c=[]
    while i<len(a):
        if a[i]!=0:
            b.append(a[i])
        else:
            c.append(a[i])
        i=i+1
num([1450,960000,1050,-1050])
??

