
n=int(input("Enter n:"))
rev=0
while(n>0):
    k=n%10
    rev=(rev*10)+k
    n=n//10

print(rev)

