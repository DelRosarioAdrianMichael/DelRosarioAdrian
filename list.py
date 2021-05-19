list1=["Monday", "Tuesday", "Wednesday"]
print(list1)
print(len(list1))

#add item in list
list1.append("Thursday")
print(list1)
print(len(list1))

#remove item in the list
list1.remove("Tuesday")
print(list1)
print(len(list1))

#insert item in specific position
list1.insert(0, "Sunday")
print(list1)
print(len(list1))

#remove item in specific position
list1.pop(1)
print(list1)
print(len(list1))