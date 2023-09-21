# create fibonacci series by inputing a limit using for loop.
num=int(input("Enter an upper limit for the series: "))
a=0
b=1

for i in range(0,num,1):
    print(a)
    c=a
    a=b
    b=b+c

#c=a+b
#print(c)
# a=b
# b=c

#a,b=b,a+b