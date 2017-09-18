# coding:utf-8

import json
import requests

print("请输入姓名：")
name=input()
print("请输入身份证号码：")
sfz=input()
print("请输入考试类型（四级：1， 六级：2）：")
type=input()

url = "http://app.cet.edu.cn:7066/baas/app/setuser.do?method=UserVerify";
ks_data = {
"ks_xm": name,
"ks_sfz": sfz,
"jb": type
}

user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
post_json=json.dumps(ks_data)
postdata = {
"action": "",
"params": post_json
}

print(post_json)
print(" ")
r=requests.post(url, data=postdata)
res=r.content
res=bytes.decode(res)
print("准考证号码： " + json.loads(res)["ks_bh"])

