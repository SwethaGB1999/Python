# make an inverted right triangle with astrix symbol using for loop.

num_of_rows=int(input("Enter number of rows you want: "))
for i in range(num_of_rows,0,-1):
    for j in range(i,0,-1):
        print("* ",end="")
    print("")