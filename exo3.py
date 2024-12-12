t = int(input("Total amount: "))
n =int(input("Number of items: "))
day = input("Day of the week: ")

if day.lower() in ["monday","tuesday","wednesday","friday","thursday"]:
    if n>5 :
        p=0.85*t
        print(f"The total price after discount is: {p} dinars")
    else:
        p=0.9*t
        print(f"The total price after discount is: {p} dinars")
elif day.lower() in ["saturday","sunday"]:
    if n>5 :
        p=0.75*t
        print(f"The total price after discount is: {p} dinars")
    else:
        p=0.8*t
        print(f"The total price after discount is: {p} dinars")
else:
    print("It seems like you haven't entered a valid day")

