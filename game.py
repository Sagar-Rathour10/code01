import random


print("*******WELCOME TO THE NUMBER PREDICTION********")
x=int(input("Enter A starting number from which you want to start to chose the number "))
y=int(input("Enter a last number from which you want to end to chose number [including last number ]"))

n=random.randint(x,y)

print("Now you have only [three] chance to predict Number")

for i in range(3):
    k=int(input("enter number "))
    if k==n:
        print("Congratulation")
        break
    else:
        print("Lost")


print(f"Correcct number is {n}")
    

