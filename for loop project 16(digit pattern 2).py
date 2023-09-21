# 2
# 24
# 246
# 2468

# num_of_rows=int(input("Enter number of rows: "))
# for i in range(2,num_of_rows+2,2):
#     for j in range(2,i+1,2):
#         print(j," ",end="")
#     print()

# row=int(input("Enter number of rows: "))
# for i in range (2,(row*2)+1,2):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(j,end="")
#     print("")

# for i in range(2,13,2):
#     for j in range(1,i+1):
#         if j%2==0:
#             print(j,end="")
#     print()

num=int(input("Enter the limit: "))
for i in range(2,(num*2)+1,2):
    for j in range(2,i+1,2):
        print(j," ",end="")
    print()
