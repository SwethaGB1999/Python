# 1
# 23
# 456
# 78910

num=int(input("Enter the number of steps: "))
for i in range(num):
    sum=0
    for j in range(1,i+2):
        sum+=j
        print(j," ",end="")
    print()

