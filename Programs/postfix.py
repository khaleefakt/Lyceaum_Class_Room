def evaluate(s):
    a=[] 
    for i in s:
        if i.isdigit():
            a.append(int(i))
        elif i=='+':
            t=a.pop()+a.pop()
            a.append(t)
        elif i=='-':
            t=a.pop()
            t1=a.pop()
            t3=t1-t
            a.append(t3)
        elif i=='*':
            t=a.pop()*a.pop()
            a.append(t)
        elif i=='/':
            t=a.pop()
            t1=a.pop()
            t3=t1/t
            a.append(t3)
    return a.pop()

st="23+4*2/"
print(evaluate(st))
