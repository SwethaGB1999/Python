# 1
# 12
# 123
# 1234
# 123
# 12
# 1

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# if i==4:
#     for i in range(4,0,-1):
#         for j in range(1,i):
#             print(j,end="")
#         print()

num=int(input("Enter a number: "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j," ",end="")
    print()
if i==num:
    for i in range(num,0,-1):
        for j in range(1,i):
            print(j," ",end="")
        print()