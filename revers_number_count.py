n = int(input("Enter any number "))
rev = 0
i=0
while(n>0):    
    rem=n%10
    rev=rev*10+rem
    n=n//10
     
print(rev)