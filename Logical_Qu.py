# Output should be:a,b,c,d

# a="d"
# b=["a","b","c","d","e"]
# i=0
# while i<len(b):
#     c=b[:4]
#     i+=1
# print(c)


# a="d"
# b=["a","b","c","d","e"]
# i=0
# c=[]
# while i<len(b):
#     if b[i]=="d":
#         c.append(b[i])
#         break
#     else:
#         c.append(b[i])
#     i+=1
# print(c)




# i=1
# while i<=20:
#     if i==2:
#         continue
#     elif i==4:
#         pass
#     elif i==8:
#         break
#     i=i+1
# print(i)






# a=[3,5,7,9]
# b=[2,3,9,8]
# i=0
# s=[]
# while i<len(a):
#     j=0
#     sum=0
#     while j<len(b):
#         if len(a)==len(b):
#             sum=a[i]+b[j]
#             s.append(sum)
#         j=j+1
#         i=i+1
# print(s)


# a=[3,5,7,9]
# b=[2,3,9,8]
# i=0
# j=-1
# sum=0
# c=[]
# while i<len(a) and j<len(b):
#     sum=a[i]+b[j]
#     c.append(sum)
#     i=i+1
#     j-=1
# print(c)




# def add(a=4,b=7,c=8):
#     return(a+b+c)
# print(add(2))

# a=int(input("l:-"))
# b=int(input("m:-"))
# x=int(input("x:-"))
# y=int(input("y:-"))
# print(a*b+x*y)



# def my(a):
#     if a==1:
#         print(a*"*")
#     else:
#         print(a*"*")
#         my(a-1)
#         print(a*"*")
# my(3)


# def num(a):
#     if a==0:
#         return 1
#     else:
#         print(a)
#         num(a-1)
# num(10)

# N=int(input())
# i=1
# while i<=N:
#     if N%i==0:
#         print(i)
#     i=i+1

# N=int(input("entre the no:"))
# K=int(input("entre the no:"))
# i=1
# while i<=N:
#     if K in N:
#         print("1")
#     else:
#         print("-1")
#     i=i+1




# N=int(input())
# i=1
# sum=0
# while i<=N:
#     sum=sum+i
#     i=i+1
# print(sum)


# Find all the prime numbers between 1 to 100 whith the use of function....

# def fun(a):
#     i=1
#     while i<=a:
#         j=1
#         c=0
#         while j<=i:
#             if i%j==0:
#                 c=c+1
#             j=j+1
#         if c==2:
#             print(i)
#         i=i+1
# fun(100)


# Check the user input is prime number or not....

# def num(a):
#     i=1
#     c=0
#     while i<=a:
#         if a%i==0:
#             c=c+1
#         i=i+1
#     if c==2:
#         print("prime no")
#     else:
#         print("not prime")
# num(int(input("entre the no:")))
