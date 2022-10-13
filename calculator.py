line = input("Enter an equation: ")
arr=line.split(' ')
while(len(arr)>1 and arr[0]!=0):
    holder = arr[0]
    for i in range(1,len(arr)):
        if(i=='+'):
            holder += arr[i+1]
        elif(i=='-'):
            holder -= arr[i+1]
        elif(i=='*'):
            holder *= arr[i+1]
        elif(i=='/'):
            holder /= arr[i+1]
        else:
            continue
        print("The outcome is "+ holder)
        line = input("Enter an equation")
        arr=line.split(' ')

print("peace")

