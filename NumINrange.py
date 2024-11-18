Num1 = int(input("Enter Num1 : "))
Num2 = int(input("Enter Num2 : "))
for i in range(Num1,Num2+1):
    if i % 3 == 0:
        continue
    print(i)
