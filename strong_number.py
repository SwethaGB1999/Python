#Strong number is a special number whose sum of the factorial of digits is equal to the original number.
# For Example: 145 is strong number. Since, 1! + 4! + 5!
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
#
num=int(input("Enter the number: "))
new_num=num
factorial=1
fact_sum=0
while num>0:
    digit=num%10
    while digit>0:
        factorial=factorial*digit
        digit-=1
    new_fact=factorial
    fact_sum=fact_sum+new_fact
    num=num//10
    factorial=1
if fact_sum==new_num:
    print(fact_sum,"is a strong number.")
else:
    print(fact_sum,"is not a strong number.")


