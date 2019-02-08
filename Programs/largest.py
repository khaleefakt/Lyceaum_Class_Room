data=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    data.append(input("Enter element:"))
print(data)
largest=data[0]
for b in data:  
    if b > largest:
        largest = b
print('Largest element is:',largest)
