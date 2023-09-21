# *
# *+
# *+*
# *+*+
# *+*+*
num=int(input("Enter a number: "))
for i in range (num):
    for j in range (1,i+2):
        if j%2!=0:
            print("* ",end="")
        if j%2==0:
            print("+ ",end="")
    print()
