
import function1

sum1 = 0
sum2 = 0

while True:
    num = int(input('ใส่ค่า: '))
    if num > 0:
        sum1, sum2 = function1.calculate(num, sum1, sum2)
    elif num < 0:
        sum1, sum2 = function1.calculate(num, sum1, sum2)
    else:
        break

print(f'ผลรวม = {sum1 + sum2}')