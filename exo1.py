name = input("Please enter your name: ")
if name == "VIP" or name =="vip":
    print("Enjoy the show for free !")
else:
    num = int(input("How many tickets would you like to buy? "))
    print(f"The total cost is :{num*15.50}")
    print("Enjoy your tickets!")