#1
# dicto={}
# name=input("enter the name")
# while name!='no':
#     salary = input("enter the salary")
#     dicto[name]=salary
#     name = input("enter the name")
# print(dicto)

#2
# numbers=[]
#
# for i in range(10):
#     newNum=int(input("enter the number"))
#     numbers.append(newNum)
#     if len(numbers)==1:
#         maxo=numbers[0]
#     else:
#         if maxo<newNum:
#             maxo=newNum
# print(maxo)
# # print(numbers)
# #3
# cel=float(input('enter the temperature'))
# print((9/5)*cel+32)
# #4
# numo=int(input("enter number"))
# for i in range(1,11):
#     print(f'{i}*{numo} = {i*numo}')
#
# #5
x= int(input("Enter a number of repetitions"))
# Write your decorator here
def annouce(f):
    def wrapper():
        for i in range(x):
            f()
    return wrapper
@annouce
def hello():
       print('Hello')

hello()
