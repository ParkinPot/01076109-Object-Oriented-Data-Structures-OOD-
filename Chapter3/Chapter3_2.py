class Barbell:
    def  __init__(self):
        self.bar_weight = 20
        self.left = []
        self.right = []
        self.available_plates = [25, 20, 15, 10, 5, 2.5, 1.25]

    def total_weight(self):
        return self.bar_weight + sum(self.left) + sum(self.right) 
    
    def add_plate(self, weight_needed, original_target):
        combo = []
        available = self.available_plates
        visual = False

        for plate in available:
            while plate <= weight_needed and len(combo) < 5:
                combo.append(plate)
                weight_needed -= plate

        if weight_needed != 0:
            if original_target == int(original_target):
                print(f"It's impossible to achieve the weight you want({int(original_target)}).")
            else:
                print(f"It's impossible to achieve the weight you want({original_target}).")
            exit()

        for i in range(min(len(self.left), len(combo))):
            if self.left[i] != combo[i]:
                mismatch_index = i
                break
        else:
            mismatch_index = min(len(self.left), len(combo))

        if len(self.left) > mismatch_index:
            for _ in range(len(self.left) - mismatch_index):
                removed = self.left.pop()
                self.right.pop()
                print(f"PO:{removed}", end=" ")
                visual = True

        for i in range(len(self.left), len(combo)):
            added = combo[i]
            self.left.append(added)
            self.right.append(added)
            print(f"PU:{added}", end=" ")
            visual = True

        if visual:
            print("=> ", end="")

        self.print_bar()

    def set_target_weight(self, target):
        original_target = target
        weight_needed = (target - self.bar_weight)/2
    
        if weight_needed < 0:
            if target == int(target):
                print(f"It's impossible to achieve the weight you want({int(target)}).")
            else:
                print(f"It's impossible to achieve the weight you want({target}).")
            exit()
        elif weight_needed % 1.25 != 0 and weight_needed % 2.5 != 0 and weight_needed % 5 != 0 \
        and weight_needed % 10 != 0 and weight_needed % 15 != 0 and weight_needed % 20 != 0 \
        and weight_needed % 25 != 0:
            if target == int(target):
                print(f"It's impossible to achieve the weight you want({int(target)}).")
            else:
                print(f"It's impossible to achieve the weight you want({target}).")
            exit()
        elif weight_needed > 125:
            if target == int(target):
                print(f"It's impossible to achieve the weight you want({int(target)}).")
            else:
                print(f"It's impossible to achieve the weight you want({target}).")
            exit()
        else:
            self.add_plate(weight_needed, original_target)

    def print_bar(self):
        left_str = ''.join(f"[{p}]" for p in reversed(self.left))
        right_str = ''.join(f"[{p}]" for p in self.right)
        
        plate_count = len(self.left)
        dash_count = max(0, 5 - plate_count)
        dashes = '-' * dash_count

        bar = f"{dashes}{left_str}|======|{right_str}{dashes}"

        weight = self.total_weight()

        has_decimal = any(p % 1 != 0 for p in self.left)

        if has_decimal:
            print(f"{bar} => {weight:.1f} KG.")
        else:
            print(f"{bar} => {int(weight)} KG.")

n = list(map(float, input("Enter needed weight(s): ").split()))
barbell = Barbell()

for target_weight in n:
    barbell.set_target_weight(target_weight)

# คำถามที่เรามักพอบ่อยๆในการไปเข้ายิม หรือฟิตเนสในช่วงแรกๆคือ "อันนี้หนักเท่าไหร่"  "ต้องใส่ข้างละกี่กิโล"  "อีก 20 กิโลมาจากไหน"  ฯลฯ



# แม้จะเป็นเรื่องปกติ แต่หากเราต้องคิดคำนวณในหัวซ้ำๆหลายรอบเพื่อตอบคำถามแต่ละครั้ง ก็คงผลาญพลังงานเกินความจำเป็น ซึ่งทำให้มีผลต่อการยกน้ำหนัก หรือออกแรงในเซสชั่นถัดไป

# เพื่อ Gym bros เหล่านี้ จงคำนวณน้ำหนักของบาร์เบล เพื่อหาว่าจำเป็นต้องถอด/ใส่แผ่นน้ำหนักขนาดต่างๆเท่าไหร่ และอย่างไรเพื่อให้ได้น้ำหนักที่ต้องการ โดยมีรายละเอียดดังนี้



# บาร์เบลเริ่มต้นจะมีน้ำหนัก 20 kg สามารถใส่แผ่นน้ำหนักได้ข้างละ 5 แผ่น และแผ่นน้ำหนักที่จะมีให้ใช้ได้แก่ 1.25 kg, 2.5kg, 5kg, 10kg, 15 kg, 20 kg, 25 kg

# เพื่อความสวยงาม และง่ายต่อการดรอปเซต ลักษณะการใส่แผ่นน้ำหนัก คือ แผ่นที่อยู่ลึกกว่าต้องมีน้ำหนักไม่น้อยกว่าแผ่นที่อยู่นอกกว่า รวมถึงแผ่นน้ำหนักทั้งฝ่ายซ้ายและขวาต้องสมดุลกัน
# หากมีการเปลี่ยนน้ำหนัก สามารถรวบแผ่นน้ำหนักโดยการเอาแผ่นน้ำหนักนอกสุดออกและใส่แผ่นน้ำหนักที่ใหญ่กว่าได้

# Input
# รับค่าน้ำหนักที่ต้องการจะเล่น โดยน้ำหนักที่รับได้มีจำนวน n ค่า (เมื่อ n เป็นจำนวนเต็มบวก) คั่นด้วยช่องว่าง

# Output
# จำนวน n บรรทัด แต่ละบรรทัดจะบอกวิธีการว่าหากต้องการน้ำหนักที่กำหนดพอดี ให้เปลี่ยนแผ่นน้ำหนักอย่างไรบ้าง โดย
# PU:15 หมายถึง การใส่แผ่นน้ำหนัก 15 kg เข้าไปทั้งสองข้างของบาร์เบล 
# PO:20 หมายถึง การถอดแผ่นน้ำหนัก 20 kg ทั้งสองข้างของบาร์เบลออก
# รวมถึง แสดงลักษณะและน้ำหนักโดยรวม ของบาร์เบลในปัจจุบัน

# หากไม่สามารถใส่แผ่นน้ำหนักให้ตรงตามความต้องการได้ให้หยุดการทำงานเพื่อบอกผู้ใข้ทันที

# Enter needed weight(s): 50
# PU:15 => ----[15]|======|[15]---- => 50 KG.

# Enter needed weight(s): 60 100 110 140 295
# PU:20 => ----[20]|======|[20]---- => 60 KG.
# PO:20 PU:25 PU:15 => ---[15][25]|======|[25][15]--- => 100 KG.
# PO:15 PU:20 => ---[20][25]|======|[25][20]--- => 110 KG.
# PO:20 PU:25 PU:10 => --[10][25][25]|======|[25][25][10]-- => 140 KG.
# It's impossible to achieve the weight you want(295).
    


