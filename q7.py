stock={"laptop":5,"mouse":0,"keyboard":3,"monitor":0}
pro=input("enter the product name :")
pro=pro.lower()
if pro in stock :
    print("available\n")
    if stock[pro]>0:
        print("Stock is also prsent\n")
        print("You Can Also Buy it")
    else:
        print("Sorry Stock is not Available")
else:
    print("This Product Do Not Sale Here")