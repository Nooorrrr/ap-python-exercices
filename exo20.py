
list =[]

while True:
    v = int(input("Enter a value (enter 0 to quit): "))
    if v == 0:
        if len(list) == 0:
            print("The list is empty")
            break
        else:
            print("The list is: ", list)
            print("The sorted list is: ", sorted(list))
            print("The median is: ", sorted(list)[len(list)//2])
            print("The mean is : ", sum(list)/len(list))
            print("----------goodbye----------")
        break
    else:
        list.append(v)
        print("The value has been added to the list")
        print("The list is: ", list)
        print("THe sorted list is : ", sorted(list))
        print("-------------------------")
    
