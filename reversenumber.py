#Reverse number
count=int(input("Enter number of digits in the number: "))
num_of_digit=count
print(str(count))
new_num=0
# string_char=''
# while count>0:
#     num=input("Enter each number and press enter: ")
#     string_char=string_char+num
#     count-=1
# string_char=int(string_char)
# print(string_char)
# new_num=0
# count=num_of_digit
# reverse of a number
num=int(input("Enter a number. "))
temp_num=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("The reverse of",temp_num,"=",rev)
