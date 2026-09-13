x=int(input("enter  lenght side "))
y=int(input("enter second side"))
z=int(input("enter third side"))
if x+y>z and y+z>x and z+x>y:
    if x==y==z:
        print("Equilateral Triangle")
    elif x==y or y==z or z==x :
        print("Isosceles Triangle")
    else:
        print("scalene Triangle3")
else:
    print("Not a Valid Triangle")23


