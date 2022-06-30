from pyrsistent import discard
import requests
import json
import pandas as pd
import os
import time

# ----cookies部分，可能会过期，需要手动登录后将新的cookies填入------------


url = "https://ehall.ynu.edu.cn/jwapp/sys/wdkb/modules/xskcb/xskcb.do"

payload='XNXQDM=2021-2022-1'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'route=4759ac822f253e4903653c95ba84d98d; _WEU=PH5UD3zezZP8J9t5Wi0NKenx84hgJZl7uydro8CW9rh94RNKbI9CyH6zlXuXUsP2y3OKTKqE0BsFGEXsxA0wOv2tg71pQflwY5Zm0zzTsjU.; JSESSIONID=WESQMvSdDJMo5S0mzKd-MLeFK0MyqPAQ2ME1uUxJ_YtcqJZ49DRC!-1950092067; MOD_AUTH_CAS=MOD_AUTH_ST-15636823-jrRM7enaEfGSHnDCihRO1655981667386-IrJa-ids1; asessionid=527bd696-80c9-44f0-a080-12c6f359393f; route=94238666b3e0150a6c8abca94b06b81c'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# ----------------

# 存储爬到的json数据
file = open("./request.json", "w", encoding="UTF-8")
file.write(response.text)
file.close()

# 打开爬取的文件，分析json数据生成dataframe
f = open("./request.json", "r",encoding = "UTF-8")
info_data = json.load(f)
ls1=[]
ls2=[]
ls3=[]
ls4=[]
ls5=[]
ls6=[]
ls7=[]
for key in range(0,len(info_data['datas']['xskcb']['rows'])):
    st=info_data['datas']['xskcb']['rows'][key]['YPSJDD']
    content=info_data['datas']['xskcb']['rows'][key]['KCM']
    ls=st.split()
    d={ls[1]:(ls[2],content)}
    if '星期一' in d.keys():
       ls1.append(d['星期一'])
    if '星期二' in d.keys():
       ls2.append(d['星期二'])
       ls2=list(set(ls2))
    if '星期三' in d.keys():
       ls3.append(d['星期三'])
       ls3=list(set(ls3))
    if '星期四' in d.keys():
       ls4.append(d['星期四'])
       ls4=list(set(ls4))
    if '星期五' in d.keys():
        if(d['星期五'][0]=='5-8节'):
            ls5.append(('5-6节','形势与政策(4)'))
            ls5.append(('7-8节','形势与政策(4)'))
        else:
            ls5.append(d['星期五'])      
d1=dict(ls1)
d2=dict(ls2)
d3=dict(ls3)
d4=dict(ls4)
d5=dict(ls5)
d6=dict(ls6)
d7=dict(ls7)
dt={'星期一':d1,'星期二':d2,'星期三':d3,'星期四':d4,'星期五':d5, '星期六':d6, '星期日':d7}
df =pd.DataFrame.from_dict(dt,orient='columns')
temp = df.iloc[0, :].copy()
df.iloc[0, :] = df.iloc[1, :].copy()
df.iloc[1, :] = temp.copy()
temp = df.iloc[1, :].copy()
df.iloc[1, :] = df.iloc[2, :].copy()
df.iloc[2, :] = temp.copy()
temp = df.iloc[1, :].copy()
df.iloc[1, :] = df.iloc[3, :].copy()
df.iloc[3, :] = temp.copy()
temp = df.iloc[3, :].copy()
df.iloc[3, :] = df.iloc[4, :].copy()
df.iloc[4, :] = temp.copy()
df.index=['1-2节','3-4节','5-6节','7-8节','9-10节']
print(df)


# 将dataframe类型的课表保存为excel文件
df.to_excel('./request.xlsx')
time.sleep(4)
os.system('powershell .\\opent.ps1')