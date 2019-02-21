data=[]
n=int(input("Enter number of elements:"))
def smallest():    
    for i in range(n):
        data.append(input("Enter element:"))
        print(data)
    smallest=data[0]
    for b in data:  
        if b < smallest:
            smallest = b
return(smallest)

print(smallest)
