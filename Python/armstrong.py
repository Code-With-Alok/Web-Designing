n=int(input())
a=n%10
b=(n//10)%10
c=(n//00)%10
if n==a**3+b**3+c**3:
    print("Armstrong Strong")
else:
    print("Not an Armstrong Strong")