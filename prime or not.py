num=int(input("Enter num:"))
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print(num,"not a prime")
            break
    else:
        print(num,"is prime")
else:
    print("1 is not a prime number")

        