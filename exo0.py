n = int(input("How many people need a ride? "))
p = int(input("How many people can fit in a taxi? "))

if n%p != 0 :
    car = n//p +1 
else:
    car = n//p 

print(f"The number of taxis needed is: {car}")