
print("1、计算成绩等级")
print("2、版本号")
print("3、各地今年中考成绩等级")
choice = input("输入你的选择(1/4):")
if choice =="1":
    score=int(input("请输入成绩"))

if choice =="2":
     print('2.5')
     print("程序运行结束，请重启")

elif  choice =="3":
    import time
    localtime = time.asctime(time.localtime(time.time()))
    import socket
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    print(f"Hostname: {hostname}")
    print(f"IP_Address: {ip_address}")
    print("截止到本地时间为 :", localtime)
    print('中考结束')


elif score >= 130:
    print("A")
elif score >= 90:
    print("B")
elif score >= 60:
    print("C")
elif score < 60:
    print("D")
print("程序运行结束,请重启")



