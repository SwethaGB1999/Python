# a=int(input("Enter lower limit: "))
# b=int(input("Enter upper limit: "))
# while a<=b:
#     if a%2!=0:
#         print(a,"odd")
#
#     else:
#         print(a,"even")
#
#     a += 1

#continue (odd number)
# a=0
# while a<=10:
#     a+=1
#     if a%2==0:
#         continue
#     print(a)


# n=10
# while n>=0:
#     if n==5:
#         break
#     n-=1
#     print(n)


#homework
# #sum of digit until the sum becomes a single number
# print("Enter the number in the order of 1000,100,10 and 1 place values")
# place_val=int(input("ENter the place value: "))
# a=0
# b=0
# while a<=(place_val-1):
#     b=int(input("Enter first number: "))
#     b+=b
#     a+=1
#
# if b>=10:
#     c=int(b/10)
#     print(c)
#     d=b%10
#     print(d)
#
#     print("The sum:",c+d)
# else:
#     print("The final sum is ",b)
#
 # b = str(b)
    # c=int(b[0])
    # d=int(b[1])

# b=int(input("Enter 1000th place: "))
# c=int(input("Enter 1000th place: "))
# d=int(input("Enter 1000th place: "))
# the_num=str(a)+str(b)+str(c)+str(d)
# print("Your number is: ",the_num)
# sum_0=a+b+c+d
# print("The sum of all the numbers is: ",sum_0)
# if sum_0>10:

# #spy number
# lenght=int(input("ENter the number of digits: "))
# a=0
# c=1
# d=0
# while a<=lenght-1:
#     b=int(input("Enter a number: "))
#     c=c*b
#     d=d+b
#     a += 1
# print(c,d)

no_of_digits=int(input("Enter the number of digits: "))
count=0
sum_of_digits=0
string_num=''
while count<(no_of_digits):
    num=int(input("Enter each digit and type enter: "))
    sum_of_digits+=num
    string_num=str(num)+string_num
    count+=1
print(string_num)
print(sum_of_digits)
if 100>sum_of_digits>10:
     digit_10th_place=int(sum_of_digits/10)
     digit_1_place=sum_of_digits%10
     print(digit_10th_place)
     print(digit_1_place)
     print("Sum of all digits: ",digit_10th_place+digit_1_place)
elif sum_of_digits<10:
     print("Sum of all digits: ", sum_of_digits)
else:
    print("invalid")


    










