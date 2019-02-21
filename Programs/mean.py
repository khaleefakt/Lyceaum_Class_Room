def mean ():
    data= []
    n = int(input("Enter total number of numbers"))
    for i in range(n):
        data.append(int(input("enter the numbers")))
    sum = 0
    for num in data:
        sum = sum+num
    print("SUM of first ", n, "numbers is: ", sum )
    mean = sum/n
    print("mean = {}".format(mean))

mean()
