#make a pyramid with astrix using for loop:
num=int(input("Enter a number: "))
for i in range(num):
    print("."*i+"*"*(num-(i+1))+"*"+"*"*(num-(i+1)))