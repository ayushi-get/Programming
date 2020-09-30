n=int(input("Enter the number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
        
if sum==n:
    print("This is a PERFECT number ")
else:
    print("This is a NOT a PERFECT number ")
    
