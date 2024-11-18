sum1 = 0
sum2 = 0
while True:
    Num = int(input("ใส่ตัวเลข : "))
    if Num > 0:
        sum1+=Num
        print(sum1)
    elif Num < 0:
        sum2+=Num
        print(sum2)
    elif Num == 0:
        print(f"ผลรวมของตัวเลขบวกและตัวเลขลบ คือ : {sum1 + sum2}")
        break