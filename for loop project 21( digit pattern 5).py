# 6 5 4 3 2 1
# 6 5 4 3 2
# 6 5 4 3
# 6 5 4
# 6 5
# 6
# 6 5
# 6 5 4
# 6 5 4 3
# 6 5 4 3 2
# 6 5 4 3 2 1


# for i in range (0,6,):
#     for j in range(6,0+i,-1):
#         print(j," ",end="")
#     print()
# if i==5:
#     for i in range(6,0,-1):
#         for j in range(6,i-1,-1):
#             print(j," ",end="")
#         print()


num=int(input("Enter the upper limit: "))
for i in range(num):
    for j in range(num,i,-1):
        print(j," ",end="")
    print()
if i==num-1:
    for i in range(num,0,-1):
        for j in range(num,i-1,-1):
            print(j," ",end="")
        print()

