total=int(input("Enter The Total Amount "))
dis=0
paid=0
if total<1000:
    paid=total
    print("Total Amount",total)
    print("Need To be paid ",paid)
elif 1000<=total<=4999:
    dis=(10/100)*total
    paid=total-((10/100)*total) 
    print("Total Amount",total)
    print("Discount",dis)
    print("Need To Be paid",paid)
elif 5000<=total<=9999:
    dis=(20/100)*total
    paid=total-dis
    print("Total Amount",total)
    print("Discount",dis)
    print("Need To Be paid",paid)
elif total>10000:
    dis=(30/100)*total
    paid=total-dis
    print("Total Amount",total)
    print("Discount",dis)
    print("Need To Be paid",paid)
    