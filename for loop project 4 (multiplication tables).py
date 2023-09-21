# Make a multiplication table usinf for loop
digit=int(input("Enter the factor with which you wish to multiply: "))
for i in range(0,11,1):
    print(digit,"x",i,"=",digit*i)

