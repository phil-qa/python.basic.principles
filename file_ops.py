class Client:
    def __init__(self, line):
        self.first_name = line[0]
        self.last_name = line[1]
        self.city = line[4]

    def __str__(self):
        return f"The clients name is {self.first_name} {self.last_name} and they live in {self.city}"

    def get_client(self):
        return(f"The clients name is {self.first_name} {self.last_name} and they live in {self.city}")






# open a csv
import csv

clients = []

# read a csv
with open("uk-500.csv",newline='') as csvfile:
    read_data = csv.reader(csvfile, delimiter = ',')
    next(read_data)
    for row in read_data:
        # print(row[0])
        #print(', '.join(row))
        clients.append(Client(row))

print(clients[0])
print(clients[10])
print(clients[1].first_name)
print(clients[5].get_client())