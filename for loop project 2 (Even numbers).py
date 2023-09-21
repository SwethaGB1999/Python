# For loop to find even numbers.
#Concept of for else.
r=int(input("Enter a range: "))
for i in range(0,r,1):
    if i%2==0:
        print(i)
else:
    print("hi")