Info = {}
Input = int(input("จำนวนคนที่จะป้อน : "))
for i in range(Input):
    NickName = str(input(f"กรุณากรอกคนที่{i+1}\nกรุณากรอกชื่อเล่น : "))
    Info["nickname"] = NickName
    Num = int(input("กรุณากรอกเลขที่ : "))
    Info["stuid"] = Num
    Hob = str(input("กรุณากรอกงานอดิเรก : "))
    Info["hobby"] = Hob
    Color = str(input("กรุณากรอกสีที่ชอบ : "))
    Info["color"] = Color
    print(f"ข้อมูลคนที่ {i+1}")
    print(Info)