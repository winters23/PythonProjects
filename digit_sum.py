n=int(input("enter your digit"))
s=0
while(n>0):
    s=s+n%10
    n//=10
print(s)