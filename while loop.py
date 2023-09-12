#Sum of digits
#code below:
no_of_digits=int(input("Enter the number of digits: "))
count=0
sum_of_digits=0
while count<(no_of_digits):
    num=int(input("Enter each digit and type enter: "))
    sum_of_digits+=num
    count+=1
print(sum_of_digits)
if 100>sum_of_digits>10:
     digit_10th_place=int(sum_of_digits/10)
     digit_1_place=sum_of_digits%10
     print(digit_10th_place)
     print(digit_1_place)
     print("Sum of all digits: ",digit_10th_place+digit_1_place)
elif sum_of_digits<=10:
     print("Sum of all digits: ", sum_of_digits)
else:
    print("invalid")


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
#____________________________________________

#Strong number is a special number whose sum of the factorial of digits is equal to the original number. For Example: 145 is strong number. Since, 1! + 4! + 5!
# first_num=int(input("ENter the number with highest place value: "))
# second_num=int(input("ENter the number with highest place value: "))
# third_num=int(input("ENter the number with highest place value: "))
# count=0
# fact=1
# num=(str(first_num)+str(second_num)+str(third_num))
# print(num)
# while first_num>=1:
#     fact_1=fact*first_num
#     first_num-=1
# while second_num>=1:
#     fact_2=fact*second_num
#     second_num-=1
# while third_num>=1:
#     fact_3=fact*third_num
#     third_num-=1
# sum_of_fact=fact_1+fact_2++fact_3
# if int(num)==sum_of_fact:
#     print(num,"is a strong number. ")
# else:
#     print(num,"is not a strong number.")

#___________________________________________________________________
#Reverse number
# count=int(input("Enter number of digits in the number: "))
# num_of_digit=count
# string_char=''
# while count>0:
#     num=input("Enter each number and press enter: ")
#     string_char=string_char+num
#     count-=1
# string_char=int(string_char)
# print(string_char)
# new_num=0
# count=num_of_digit
# while count>0:
#     num_2=string_char%10
#     string_char=int(string_char/10)
#     num_2=num_2*(10**(count-1))
#     new_num=new_num+num_2
#     count-=1
# print(new_num)













