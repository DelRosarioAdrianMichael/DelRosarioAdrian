my_name = input("Enter Name: ")
print("Welcome " +my_name)

my_grade = input("Enter your Grade: ")
my_grade = int(my_grade)

if my_grade >= 98 and my_grade <= 100:
    print(my_name + " Your grade is 1.00 ")
elif my_grade >= 96 and my_grade <= 97: 
    print(my_name + " Your grade is 1.25")
else:
    print("Invalid")