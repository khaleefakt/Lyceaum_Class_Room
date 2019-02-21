data= []
n=int(input("enter the list of numbers :  "))
for i in range(n):
    data.append(input("enter elements: "))
print (data)
largest = data[0]
smallest= data[0]
for j in data:
    if j > largest:
        largest =j
for k in data:
    if k < smallest:
        smallest =k

print ("largest = {}".format(largest))
print ("smallest = {}".format(smallest))
    
