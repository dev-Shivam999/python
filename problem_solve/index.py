a=input(str("enter the  age"))
age=int(a)
op=10
if age>13 and age<19:
    
    print("teenager")
elif age>20 and age<59:
    print("adult")
elif age>60:
    print('senior')    
else:
    print("child")    


print(op)