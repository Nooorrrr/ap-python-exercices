
cities = []
city = input("Enter a city name: ")
if city != "stop":
        cities.append((city,len(city)*1000000))

while city != "stop":
    city = input("Enter a city name (or enter stop if you want to stop): ")
    if city != "stop":
        cities.append((city,len(city)*1000000))

cities.sort(key =lambda x:x [1],reverse =True)

print("the ordered cities")

for city, population in cities:
    print(f"The city {city} has a population of {population}")