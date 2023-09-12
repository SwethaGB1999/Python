perm_num=int(input("Enter a number: "))
num=int(input("Enter a number from0 to 9: "))
while perm_num>0:
    digit=perm_num%10
    perm_num=perm_num//10
if num==digit:
    print("Yes it is the first number .")
else:
    print("No it is not the first number.")

