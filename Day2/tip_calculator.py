print("Welcome to the tip calculator!!")

bill = float(input("What was the total bill ? "))

tip_percent = int(input("What percentage tip would you like to give? 10,12 or 15 : "))

split_bill = int(input("How many people to split the bill ? "))

tip = round ((float(bill) / int(split_bill)) * (int(tip_percent)/100) , 2)

print("Tip should be given by each person is : ",tip)