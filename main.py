#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay. 

yname=input("Enter yor name: ")
print("\n Hi ",yname)

num_people=int(input("\n How many people are dinning today?   "))#number of people for dinner

total_price=int(input("\n How much is the total bill?: £ "))#Total bill

cost_pp=total_price / num_people #dividing price per person

print("\n Each person pays £",cost_pp)