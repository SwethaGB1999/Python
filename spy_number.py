#spy number
#A number is said to be a Spy number if the sum of all the digits is equal to the product of all digits.
#code below:
# print("Enter number from the highest place value to lowest place value:")
# place_val=int(input("Enter the number of digits in the number: "))
# count=0
# sum=0
# product=1
# num_s=''
# while count<place_val:
#     num=int(input("Enter each digit and press enter: "))
#     sum+=num
#     product=product*num
#     num_s=num_s+str(num)
#     count+=1
# if sum==product:
#     print(num_s," is a spy number")
# else:
#     print(num_s," is not a spy number")
#spy number
num=int(input("Enter a number: "))
temp_num=num
pro=1
sum=0
while num>0:
    digit=num%10
    sum+=digit
    pro=pro*digit
    num=num//10
if sum==pro:
    print(temp_num,"is a strong number.")
else:
    print(temp_num, "is not a strong number.")
