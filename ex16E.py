from sys import argv
script,filename =argv

print("we are going to erase {filename}")
input("?")

print("opening the file:")
target=open(filename, 'w')

print("truncating the file")
target.truncate()

print("read to the file")
line1 = input("line1:")
line2= input("line2:")

print ("going to write these lines to new file:")
target.write(line1)
target.write(line2)

print("closing")
target.close()



