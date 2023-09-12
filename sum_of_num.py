# num=int(input("ENter a number: "))
# digit=num
# count=0
# while num>0:
#     d=num%10
#     count=count+d
#     num=num//10
#     if count > 9:
#         num=count
#         count=0
# print(count)

# num=int(input("Enter a number: "))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
#     if num==0 and sum>9:
#         num=sum
#         sum=0
# print(sum)
#Sum of numbers
num=int(input("Enter a number: "))
sum=0
while num>0:
    digit=num%10
    sum=sum+digit
    num=num//10
    if sum>9 and num==0:
        num=sum
        sum=0
print(sum)