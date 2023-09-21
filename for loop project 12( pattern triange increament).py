# make a right angled triange with astrix using for loop.

num_of_rows=int(input("Enter the number of rows you want: "))
for i in range(num_of_rows):
    for j in range (i+1):
        print("*",end="")
    print()