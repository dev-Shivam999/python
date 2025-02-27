number =[1,-2,1,3,-5,6,-7,-3]
count=0
# for i in number:
#     # print(i)
#     count+=1 

for i in range(10):
    if i==5-1:
        continue
    # print((i+1)*3)

str="lol opi oooyyyye"

# dic={}

# for i in str:
#      dic[i]=dic.get(i,0)+1
 

# for i,j in dic.items():
#     print(i,j)
#     if j==1:
#      print(i)
#      break

# i=0
# num=3
# fac=1
# while num>i:
#     fac=fac*(num-i)
#     i+=1

# print(fac)

# while True:

#  a=input("enter number between 0 and 9")
#  if a.isdigit() and 0 <= int(a) <= 9:
#      print("you have entered correct number")
#      break

number=29

isPrime=True

if number >1:
    for i in range(2,number):
        if number%i==0:
            isPrime=False
            break

