n=int(input())
rev=0
for i in range(n):
    digit=n%10
    rev=rev*10+digit
    n=n//10

    if rev==n:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")
    