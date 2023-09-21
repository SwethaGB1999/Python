#     *
#    **
#   ***
#  ****
# *****

num_of_rows=int(input("Enter number of rows: "))
for i in range(1,num_of_rows+1):
    print("  "*(num_of_rows-i)+"* "*i)
