# reverse of a number
num=int(input("Enter a number. "))
temp_num=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print("The reverse of",temp_num,"=",rev)





