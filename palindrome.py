#palindrome
num=int(input("Enter a number:"))
original_number=num
rev=0
while num!=0:
    d=num%10
    rev=(rev*10)+d
    num=num//10
print(rev)
if original_number==rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome.")