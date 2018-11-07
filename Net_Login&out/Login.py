import requests##链接网络
url = "http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1"
params = {
"action": "login",
"ac_id": "1",
"user_ip": "",
"nas_ip": "",
"user_mac": "",
"url": "",
"username": "yournumber",
"password": "yourpasswors",
"save_me": "0"
    }
r = requests.post(url,data=params)
if(r!=None):
    print("登录成功")