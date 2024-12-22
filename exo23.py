numbers =[]

while True:
    n = int(input("Enter a number (0 to stop ): "))
    if n == 0:
        if len(numbers) == 0:
            print("The list is empty")
            break
        else:
            for i in range(len(numbers)):
                print(numbers[i])
        break
    
    if n<0 or type(n) != int:
        print("The number is negativeor is not an integer")
    else:
        numbers.append(n)
    
    