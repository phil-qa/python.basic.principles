#Open a file using the open function the modes for it can be
# r - read
# a - append
# w - write
# x - create exclusive

#open and read a file

# file_object = open("uk-500.csv", 'r')
# print(file_object.read())
#
#
# #
# # #Oh no I cant do that twice
# file_object.seek(0)
# #
# # read a couple of lines
#
# for line in file_object:
#    print(line)
#
# file_object.close()
#

# #create a file
# my_file = open('myTextFile.txt','w')
# my_file.write("Adding a line to this")
# my_file.close()
#
# my_file = open('myTextFile.txt','a')
# my_file.write("Another line is here")
# my_file.close()

#
# # class Address:
# #     def __init__(self, line):
# #         self.
#
#
# # open a csv
import csv
#
# # read a csv
with open("uk-500.csv",newline='') as csvfile:
     read_data = csv.reader(csvfile, delimiter = ',')
     next(read_data)
     for row in read_data:
        #print(row[0])
        print(', '.join(row))



