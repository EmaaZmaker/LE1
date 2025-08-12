num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
num4=int(input("enter a number"))
numbers=[num1,num2,num3,num4]
even=[]
odd=[]
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("odd numbers are",odd)
print("even numbers are:",even)
    


    