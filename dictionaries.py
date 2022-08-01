# print admin
def console(message):
    print(message)

def separator():
    print("*****************")

#A dictionary is a store of keys and values for the keys, the keys must be distinct
console("The dictionary is initialised either with data or with an empty consturct {}")
basic_dict = {}

console(basic_dict)

console("Or with data, in a key : value ")

basic_dict = {"name": "phil", "employee_number": 12441, "role": "team lead"}

console(basic_dict)
separator()
console("Can address the value any of the elements dict[key]")
console(basic_dict['name'])

console("Can iterate through the dictionary, first by iterating the keys")
for k in basic_dict:
    console(basic_dict[k])

console("Can look at the values by calling the .items() method, note that this is in a list as a return")
console(basic_dict.items())

console("Also can iterate through that, note that the responses are tuples")
for item in basic_dict.items():
    console(item)

console("Can also separate these into key value through the items() method")
for ke, value in basic_dict.items():
    console(f"{ke} -> {value}")

#adding things to the dict can be done by adding a key with a value
console("Can add to the dictionary with a key reference and a value dict[key]=value")
basic_dict["service"] = 10
console(basic_dict)

#additionally use the update() method in list
basic_dict.update({"drinks": "coffee"})
console(basic_dict)
separator()

