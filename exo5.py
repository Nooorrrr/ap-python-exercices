print("Runner 1:")
name1 = input("Name: ")
time1 = int(input("TIme (in seconds): "))

print("Runner 2:")
name2 = input("Name: ")
time2 = int(input("TIme (in seconds): "))

if time1 == time2:
    print(f"{name1} and {name2} have the same time")
elif time1 <time2 :
    print(f"The fastest runner is {name1}")
else:
    print(f"The fastest runner is {name2}")