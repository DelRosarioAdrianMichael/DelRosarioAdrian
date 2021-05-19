my_name = input("Enter Name: ")
print("Welcome " +my_name)

my_age = input("Enter your Age: ")
my_age = int(my_age)

if my_age >= 18:
    print("You are eligible to vote")
else: 
    print("You are not eligible to vote")