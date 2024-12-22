numbers = [1,2,3,4,5]

def menu():
    print("--------MENU--------")
    print("1. Append an element")
    print("2. Insert an element at a specific position")
    print("3. Pop an element")
    print("4. Remove an element")
    print("5. Sort the list")
    print("6. Reverse the list")
    print("7. Search for an element")
    print("8. Save the list to a file")
    print("9. Load the list from a file")
    print("10. Quit")

def append():
    v = int(input("Enter a value: "))
    numbers.append(v)
    print(numbers)
    print("--------------------")
    

def insert():
    v = int(input("Enter a value: "))
    i = int(input("Enter an index: "))
    numbers.insert(i,v)
    print(numbers)
    print("--------------------")
    

def pop():
    i = int(input("Enter an index: "))
    numbers.pop(i)
    print(numbers)
    print("--------------------")
    

def remove():
    v = int(input("Enter a value: "))
    numbers.remove(v)
    print(numbers)
    print("--------------------")
    

def sort():
    numbers.sort()
    print(numbers)
    print("--------------------")
    

def reverse():
    numbers.reverse()
    print(numbers)
    print("--------------------")
    

def search():
    v = int(input("Enter a value: "))
    if v in numbers:
        print("The value is in the list")
    else:
        print("The value is not in the list")
    print("--------------------")
    

def save():
    f = open("numbers.txt", "w")
    for i in numbers:
        f.write(str(i) + "\n")
    f.close()
    print("The list has been saved to numbers.txt")
    print("--------------------")
    

def load():
    f = open("numbers.txt", "r")
    numbers.clear()
    for i in f:
        numbers.append(int(i))
    f.close()
    print("The list has been loaded from numbers.txt")
    print(numbers)
    print("--------------------")
    

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        append()
    elif choice == '2':
        insert()
    elif choice == '3':
        pop()
    elif choice == '4':
        remove()
    elif choice == '5':
        sort()
    elif choice == '6':
        reverse()
    elif choice == '7':
        search()
    elif choice == '8':
        save()
    elif choice == '9':
        numbers = load()
        if numbers:
            print("List loaded from file:", numbers)
    elif choice == '10':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice, please try again.")
