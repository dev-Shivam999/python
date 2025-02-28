
# def suquare(num,how):
#     return num**how

# a=suquare(100000000,3)
# print(a)


# def sum(a,b):
#     return a+b

# print(sum(1,2))

# def multi(a,b):
#     return a*b

# print(multi("2",3))

# def area(ri):
#     area=3.14*ri**2
#     ci=2*3.14*ri
#     return area,ci

# print(area(10))



# def greet(name="lol"):
#     return "Hello "+name

# print(greet('chutiye'))
# print(greet())



# cube=lambda x:x**3
# print(cube(3))



# def sumAll(*args):
#     print(*args)
#     print(args)
    # return sum(args)
    # s=0
    # for i in args:
    #     s+=i
    # return s

# print(sumAll(1,2,3,4,5,6,7,8,9,10))
# sumAll(1,2,3,4)


# def printKwargs(**kwargs):
#     for name,profection in kwargs.items():
#         print(f"{name} is a {profection}")

# printKwargs(name="jony",profection="docter",prfection="fb")


# def generate(num):
#     for i in range(num):
#         yield i


# for i in generate(10):
#     print(i)          


def factorial(num):
    if num==0:
        return 1
    return num*factorial(num-1)

print(factorial(5))