p=0
while p<=3:
    p+=1
    password=int(input("Enter the Password"))
    if password==123456:
        print("Correct Password, login successful")
        break
    elif p==3:
        print("Limit Exceeded")
        break
    else:
        print("Wrong Password")