## Inputs we need form the user.
#Total rent
#Total food ordered for snacking
#Electricity units spend
#Charge per unit
#persons living in room/flat

## Output 

#Total amount you've to pay is 



rent = int(input("Enter Your hostel/Flat rent: "))
food = int(input("Enter the amount of food ordered: "))
Electricity_spend = int(input("Enter the total of electricity spend: "))
Charge_per_unit = int(input("Enter the charge per unit: "))
persons = int(input("Enter the number of perons living in room/flat: "))


total_bill = Electricity_spend * Charge_per_unit 

output = (food + rent + total_bill)//persons

print("Each person will pay: ",output)


