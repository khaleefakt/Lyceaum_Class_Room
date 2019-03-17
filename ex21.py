def add(a,b):
    print(f"adding {a} + {b}")
    return a + b
def subtract(a,b):
    print(f"subtracting {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"multipliying {a} * {b}")
    return a * b

def divide(a,b):
    print(f"dividing {a} / {b}")
    return a / b

print("lets do some with just functions")
age = add(21,3)
height =subtract(200,30)
weight = multiply(20,3)
iq =divide(100,2)

print(f" age:{age}, height:{height}, weitght:{weight}, iq:{iq}")

print("here is a puzzle")

what = add (age, subtract(height, multiply(weight, divide (iq,2))))
print ("that becomes:" , what, "can you do it by hand")
