line = input("Enter an equation")

while(arr.len()>0 and arr[0]==0):
    arr=line.split(' ')
    holder = arr[0]
    for i in range(1,arr.len()):
        if(i=='+'):
            holder += arr[i+1]
        elif(i=='-'):
            holder -= arr[i+1]
        elif(i=='*'):
            holder *= arr[i+1]
        elif(i=='/'):
            holder /= arr[i+1]
        else:
            break
        print("The outcome is "+ holder)
        line = input("Enter an equation")

print("peace")

