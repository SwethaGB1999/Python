# 2 4 6 8 10 12 14
# 2 4 6 8 10 12
# 2 4 6 8 10
# 2 4 6 8
# 2 4 6
# 2 4
# 2

num=int(input("Enter the number of steps:"))
for i in range(num*2,0,-2):
    for j in range(2,i+1):
        if j%2==0:
            print(j," ",end="")
    print()