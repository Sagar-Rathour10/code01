#1sept2026
#finding a and b ,then we find E


k=int(input("enter number of x values"))

#x valuse 
lstx=[]
for i in  range(k):
    x=float(input("enter values of x"))
    lstx.append(x)
print(lstx)



lsty=[]
for i in  range(k):
    y=float(input("enter values of y"))
    lsty.append(y)
print(lsty)
#

#FOR Sum of squares of x and y values

def sq(lst):
    y=0
    for i in lst:
        y+=i*i
    return y
   

def cross(lst1,lst2):
    z=0
    for i in range(len(lst1)):
        z+=lst1[i]*lst2[i]
    return z


#PRINTING THE VALUES OF a and b


a=((k*cross(lstx,lsty))-(sum(lstx)*sum(lsty)))/(k*sq(lstx)-sum(lstx)**2)
print("The value of a is: ",a)
b=((sum(lsty))-(a*(sum(lstx))))/k
print("The value of b is: ",b)

E=(sq(lsty))-(a*cross(lstx,lsty))-(b*sum(lsty))
print("The value of E is: ",E)