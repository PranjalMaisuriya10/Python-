n=int(input("ENter the number :- "))

for i in range(1,n+1):
    for k in range(n-i):
            print(" " ,end=" ")
    for j in range(1,i+1):
        print("*", end=" ")   
    print()