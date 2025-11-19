def process_input(data):
    initial, actions = data.split('/')
    stack = [hp for hp in map(int, initial.strip().split()) if hp > 0]
    actions = actions.split(',')

    print("\nstart")
    print(stack)

    for action in actions:
        if stack == [] and not action.startswith("spawn"):
            break
        cmd, val = action.strip().split()
        val = int(val)

        if cmd == "spawn" and val > 0:
            print(f"\nspawn an enemy of {val} HP")
            stack.append(val)
            print(stack)

        elif cmd == "dmg" and val > 0:
            dmg = val
            kill_count = 0
            while stack and dmg > 0:
                if dmg >= stack[-1]:
                    dmg -= stack.pop()
                    kill_count += 1
                else:
                    stack[-1] -= dmg
                    dmg = 0
            print(f"\ndeal {val} damage, killed {kill_count} enemy")
            print(stack)
            if stack == []:
                print("")  
                print(">>>> Player Wins <<<<")
                break
        elif cmd == "dmg" and val == 0:
            print("\nInvalid number")
            break
            

input_str = input("Enter Input : ")
process_input(input_str)

# Stack Fighting
#     ในเกมนี้ผู้กล้าจะต้องกำจัดศัตรู โดยศัตรูจะเกิดเรียงกันในรูปแบบ stack และผู้กล้าจะต้องทำดาเมจกับศัตรูที่ละตัว
# แต่ถ้าหากดาเมจของผู้กล้ามากกว่า HP ของศัตรู ดาเมจที่เกินมาจะโดนศัตรูตัวถัดไปเรื่อย ๆ

#     การรับ input จะรับเป็น HP ของศัตรูแต่ละตัว / action ต่าง ๆ ที่เกิดขึ้นในเกม เช่น
#             spawn 30 = spawn ศัตรูที่มี HP 30
#             dmg 37 = ทำดาเมจ 37 กับศัตรู
#         ตัวอย่าง Enter Input : 10 40 30 20 60 30/spawn 10,spawn 10,dmg 24

# เมื่อศัตรูถูกกำจัดหมดเกมจะจบลงและไม่สามารถเล่นต่อได้
# ใน action แต่ละครั้งจะแสดง stack ของศัตรูที่เหลืออยู่ และถ้าเป็นการทำดาเมจ จะแสดงจำนวนศัตรูที่ฆ่าด้วย
# ไม่สามารถทำดาเมจ 0 หรือ spawn ศัตรูที่ HP 0 ได้