'''
This is a string handling cheat sheet
'''
# what are the print functions
print(help(print))

# print a thing to the console
print('Printing a thing to the console')

# print a couple of values at once
print("Printing ", "some", "things", "To console")

# print a couple of things to console with a full stop separator
print("Printing ", "some", "things", "To console", "with", "sep=.", sep='.')

# using end parameter print two separate things on one line
print("Printing some things with the ", end='')
print("end=''")

'''
Using .format to apply formatting 
'''
#Passing positional values to the string
person = {"name": "Phil Bridge", "job" : "Development Manager", "company" : "QA"}

print('my name is {0} I am a {1} for {2}'.format(person["name"], person["job"], person["company"]))
#mixing it up
print('my name is {1} I am a {2} for {0}'.format(person["name"], person["job"], person["company"]))
#using F string
print(f'my name is {person["name"]} I am a {person["job"]} for {person["company"]}')

#Treating bits of data at types in a string, the place holders here are positional and one
#represents the data as repr and the other as a str
print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

#Formatting with justification and spaces
#This aligns left and sets 30 character spaces width
print('{:<30}'.format('left aligned'))
#is the width fixed
print('{:<1}'.format('left aligned, is the width fixed'))

#right aligned
print('{:>30}'.format('right aligned'))

#center formatted
print('{:^30}'.format('centered'))

#center formatted with padding character
print('{:*^30}'.format('centered'))

#Printing signs with numeric data

#always show a sign
print('all signs shown \n{:+f}; {:+f}'.format(3.14, -3.14) )

#show a space for a + and - for -
print('show a - sign when negative but only a space for positive \n{: f}; {: f}'.format(3.14, -3.14))

#only show - dont do anything for +
print('Show the - but do nothing with the positive number\n{:-f}; {:-f}'.format(3.14, -3.14))
