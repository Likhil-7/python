l=int(input("enter low:"))
h=int(input("enter high:"))
for num in range(l,h+1):
    if(num>1):
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num) 