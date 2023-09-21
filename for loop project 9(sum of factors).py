#Find the sum of factors of a number using for loop.

num=int(input("Entere a number: "))
sum=0
for i in range(1,num,1):
    if num%i==0:
        sum+=i
print("The sum of the factors of",num,"is",sum)