from sys import argv

script, filename = argv

print (f" We are going to erase {filename}:")
print("If you dont wantm that   hit CTRL-C (^C)>")
print("If you do want that hit RETURN")

input("?")

print ("Opening the file....")
target=open (filename, 'w')

print("Truncating the file Goodbye..!")
target.truncate()

print("Now i am going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("i am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally we clos it")
target.close()
