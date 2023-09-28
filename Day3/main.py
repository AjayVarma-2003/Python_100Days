print("Welcome to the roller coaster ride")

height = int(input("What is yout height in cm : "))

bill = 0

if height >=120:
    age = int(input("What is your age : "))
    print("You can ride...")
    if (age >= 18):
        bill = 12
        print("Pay $12")
    else:
        bill = 7
        print("Pay $7")
        
    photo = str(input("Do you want your ride photos (y/N): "))
    if photo == "y" :
        print("Pay extra $2")
        bill = bill +2
        print(f"pay ${bill}")
    if photo == "N" :
        print(f"Your final bill is ${bill}")
        
else :
    print("You can't ride...")