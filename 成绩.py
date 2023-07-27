print("选择模式")
print("1、计算成绩等级")
print("2、版本号")
print("3、各地今年中考成绩等级")
print("4、软件说明")
choice = input("输入你的选择(1/4):")
if choice =="1":
    score=int(input("请输入成绩"))

if choice =="2":
     print('1.1')
     print("程序运行结束，请重启")

elif  choice =="3":
    print('（截止到目前正在搜集各市等级计算方法）')

elif  choice =="4":
 print("本软件是用来计算各地中考等级学科等级，有一部份地区中考采用的是主科和体育算入总分，副科算等级")
 print("每个地方计算方法各不相同，详细可以咨询各市的教育局网站")

elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
elif score < 60:
    print("D")
print("程序运行结束,请重启")

