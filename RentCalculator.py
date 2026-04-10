## Input from the user
# Total rent
# Total food expenses
# Total electricity bill
#Charge per unit of electricity
#Persons living in room/flat

##Output
# Total amount you've to pay is


rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter your food expenses = "))
electricity = int(input("Enter your electricity bill = "))
charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number of persons living in the room/flat = "))

total_bill = electricity * charge_per_unit

output = (rent + food + total_bill) // persons
print("each person will pay =", output)

