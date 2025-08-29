# 1
# 1 *
# 1 * 3
# 1 * 3 *
# 1 * 3 * 5



  

n=int(input("Enter the Number of rows:"))
num=int(input("Enter the Number:"))
for i in range(1,n+1):
    sum=1
    for j in range(1, i+1):
        if(j%2==1):
            print(sum, end=" ")
            sum=sum+2
        else:
            print("*", end=" ")
    print()

