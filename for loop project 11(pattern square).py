# print a square with input number of steps and 5 stars in each line.

num_of_columns=int(input("Enter the number of columns you want."))
num_of_rows=int(input("Enter the number of rows you want."))
for i in range(num_of_rows+1):
    print("* "*num_of_columns)
