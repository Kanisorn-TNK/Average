def UsoSigma(Num1,Num2):
    CanDiv3 = []
    for i in range(Num1,Num2+1):
        if i % 3 == 0:
            continue
        CanDiv3.append(i)
    return CanDiv3

def calculate(num, sum1, sum2):
    if num > 0:
        sum1 += num
        print(f'ผลบวกจากบวก = {sum1}')
        return sum1, sum2
    elif num < 0:
        sum2 += num
        print(f'ผลบวกจากลบ = {sum2}')
        return sum1, sum2