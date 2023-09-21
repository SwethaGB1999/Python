#Check if a number is perfect or not using for loop.

num=int(input("Enter a number: "))
sum=0
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print(num,"is a perfect number.")
else:
    print(num,"is not a perfect number.")