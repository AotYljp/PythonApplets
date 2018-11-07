import requests###断开网络
url = "http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1"
params = {
"action": "logout",
"username": "yournumber",
"password": "yourpassword",
"ajax":"1"
    }
r = requests.post(url,data=params)
if(r!=None):
    print("退出成功")