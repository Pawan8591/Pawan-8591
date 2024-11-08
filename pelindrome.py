n = int(input("Enter any number "))
n1=n
rev = 0
while(n>0):    
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(n1==rev):
    {
        print(" the number is pelindrome number",rev)
     }
else :
    {
        print(" the number is not pelindrome number",rev)
     }