numbers = [1, 2, 3, 4, 5]


while True:
    i = int(input("Enter an index (enter -1 to quit): "))
    if i == -1:
        break
    if i <= 0 or i > len(numbers):
        print("Invalid index")
    else:
        value = int(input("Enter a value: "))
        numbers.insert(i, value)
        print("THe new updated list: ",numbers)








