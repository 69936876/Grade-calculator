import time
import socket

print("1、计算成绩等级")
print("2、版本号")
print("3、各地今年中考成绩等级")
choice = input("输入你的选择(1/3):")

if choice == "1":
    try:
        score = int(input("请输入成绩: "))
        if score >= 130:
            print("A")
        elif score >= 90:
            print("B")
        elif score >= 60:
            print("C")
        else:
            print("D")
    except ValueError:
        print("请输入有效的整数成绩")

elif choice == "2":
    print('2.5')
    print("程序运行结束，请重启")

elif choice == "3":
    localtime = time.asctime(time.localtime(time.time()))
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP_Address: {ip_address}")
    print("截止到本地时间为 :", localtime)
    print('中考结束')

else:
    print("无效的选择，请输入1、2或3")

print("程序运行结束,请重启")



