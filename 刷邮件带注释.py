import time
import requests


cookie = {"JSESSIONID": "2941D8F4605C97CF650525348CC71876"}  # 登录之后f12找cookie
login_data = {'username': '20YG3002', 'password': ''}  # 设置账号和密码

# 设置其他请求的URL和参数
mail_url = 'http://10.3.240.109:8088/vouching2/message/message_personadd'
login_url = 'http://10.3.240.109:8088/vouching2/Login.action'
logout_url = 'http://10.3.240.109:8088/vouching2/login.jsp?from=logout'
advertise_url = 'http://10.3.240.109:8088/vouching2/home/advertise/Advertisement1.action?method=add'
mail_data = {'outline': '【自动发送】江南皮革厂倒闭了！', 'receiver': '20YG3007', 'content': '王八蛋黄鹤老板，吃喝嫖赌，欠下3.5个亿，带上小姨子跑路了！我们没有办法，只能拿钱包抵工资，原价200、300块的钱包现在统统20块！20块！！', 'B1': '发送'}
advertise_data = {'type': '出售', 'subject': '笑死', 'content': '11111'}


def post_email():
    # 发送POST请求
    response = requests.post(mail_url, data=mail_data, cookies=cookie)

    # 输出响应结果
    print(response.text)


def mail_main(loop):
    for i in range(loop):
        post_email()
        print(i+1, '次')
        time.sleep(1)


def login():
    # 发送POST请求
    response = requests.post(login_url, data=login_data)
    # 输出响应结果
    print(response.text)

    # 发送GET请求
    response = requests.get(logout_url)
    # 输出响应结果
    print(response.text)


def login_main(loop):
    for i in range(loop):
        login()
        print(i+1, '次')
        time.sleep(1)


def advertise():
    # 发送POST请求
    response = requests.post(advertise_url, data=advertise_data, cookies=cookie)

    # 输出响应结果
    print(response.text)


def advertise_main(loop):
    for i in range(loop):
        advertise()
        print(i+1, '次')
        time.sleep(1)


#mail_main(25)  # 发邮件 25次
login_main(25)  # 登录 25次
#advertise_main(40)  # 发广告 40次
