Number = []
Input = int(input("ต้องการป้อนทั้งหมดกี่ตัว : "))
for i in range(Input):
    num = int(input(f"ใส่ตัวที่ {i+1}: "))
    Number.append(num)
Ans = sum(Number) / i
print(f"ค่าเฉลี่ยของ {Number} = {Ans}")