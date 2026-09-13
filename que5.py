unit=int(input("enter number of   bill unit"))

if unit<=100:
    bill=unit*2
    print(f"your current bill is :{bill}")
elif unit <=200:
    bill=100*2+((unit-100)*3)
    print("Your Current Electricity Bill is ",bill)
else:
    bill=100*2+100*3+((unit-200)*5)
    print(f"Your current bil is :{bill}")