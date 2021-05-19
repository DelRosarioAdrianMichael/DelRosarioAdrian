amount = input("Enter Amount: ")
quantity = input("Enter Quantity: ")
total = int(amount) * int(quantity)

cashonhand = input("Enter cash on hand: ")
change = int(cashonhand) - int(total)

print("Total Price: " + str(total))
print("Your Change is: " +str(change))