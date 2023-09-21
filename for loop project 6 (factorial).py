#Find the factorial of a number using for loop
num=int(input("ENter a number: "))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(fact)

#alternate method:
# num=int(input("ENter a number: "))
# fact=1
# for i in range(1,num+1,1):
#     fact=fact*i
# print(fact)