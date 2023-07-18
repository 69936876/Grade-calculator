print("选择模式")
print("1、计算成绩等级")
print("2、关于本程序")
choice = input("输入你的选择(1/2):")
if choice =="1":
   score=int(input("请输入成绩"))
elif choice =="2":
     print('0.1BATA版本')
     print("程序运行结束，请重启")
elif  choice =="3":
    print("非法操作,（后续会开放选项）")
elif  choice =="4":
    print("非法操作,（后续会开放选项）")
if score>=90:
          print("A")
elif score>=75:
          print("B")
elif score>=60:
          print("C")
elif score<60:
          print("D")
print("程序运行结束,请重启")

