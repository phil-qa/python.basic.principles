cities = ['London', 'Paris', 'Moscow']

# for city in cities:
#     print(city)
#     print(city)
city = None
index = 0

while city != 'Moscow':
    city = cities[index]
    index += 1
    print(city)

choice = None

while choice != 'stop':
    choice = input("Choice please 'stop' stops me")
    print(choice)

