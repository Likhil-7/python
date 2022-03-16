'''
a=int(input())
b=int(input())
c=int(input())
max=a
if(b>max):
    max=b
if(c>max):
    max=c

print(max)
'''
a=int(input())
b=int(input())
c=int(input())
if(a>b and a>c):
    print("a is bigger")
elif(b>a and b>c):
    print("b is bigger")
else:
    print("c is bigger")