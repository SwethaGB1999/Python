#Odd numbers using for loop
lower_limit=int(input("Enter the lower limit: "))
upper_limit=int(input("Enter a upper limit: "))
for i in range(lower_limit,upper_limit+1,1):
    if i%2!=0:
        print(i)