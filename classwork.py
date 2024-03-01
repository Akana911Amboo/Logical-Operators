x = int(input("Enter your age:"))
y = input("Are you a student or not? Yes/No: ")

if x <=12 and y == "Yes":
    print("You are eligible for the ticket discount")

elif x >= 13 and x <=18 and y == "Yes":
    print("You are eligible for the ticket discount")

else:
    print("You are not eligible for the ticket discount ")