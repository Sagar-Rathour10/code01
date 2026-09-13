products={"laptop":{"price":50000,"stock":3},
          "phone":{"price":30000,"stock":5},
          "headphones":{"price":2000,"stock":0}}
ask=input("Enter Product Name :")
ask=ask.lower()
q=int(input("Enter Quantity :"))
total=0
if ask in products:
    d=products[ask]
    if d["stock"]>=q:
        total=d["price"]*q
        print("Total amount :",total)
        if total>50000:
            print("total amount after discount :",(total-((10/100)*total)))
        else:
            print("No discount")
    elif q<=0:
        print("You Enter Negative values")
    elif d["stock"]==0:
        print("Today stock Not Available")
    else :
        print("Insufficient Stock")
else :
    print("Not Sale Here")