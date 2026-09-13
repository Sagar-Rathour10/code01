bal=float(input("Enter Balance"))
amt=float(input("Enter Withdrawl Amount"))
if bal>=amt:
    print("After  Withdrawn")
    print("Remainig Balance :",bal-amt)
elif amt<0:
    print("You Entered Negative Number")
else:
    print("Insufficient Balance")