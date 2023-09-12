#Sum of digits
#code below:
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
if sum_of_digits>10:
    count
     digit_10th_place=int(sum_of_digits/10)
     digit_1_place=sum_of_digits%10
     print(digit_10th_place)
     print(digit_1_place)
     print("Sum of all digits: ",digit_10th_place+digit_1_place)
elif sum_of_digits<10:
     print("Sum of all digits: ", sum_of_digits)
else:
    print("invalid")

