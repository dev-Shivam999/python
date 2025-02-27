list=[1,2,3,4,5]
list.append(0)    

for ok in list:
    print(ok,end="-> ")

print('\n')
if 1 in list:
    print("yes")
else:
    print("no")

print("count of 1",list.count(1))
    