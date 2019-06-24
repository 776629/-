import requests
import base64,os
from db import db_join,db_delete,db_search
from form import form_one

api_key= '2zph3UZGTXj1t8v1IBWpLyXt'
api_secret= 'ryAsQEuRDxyt9epnDbtPkmDjieth5WPs'

def api_to_access_token(api_key,api_secret):
    url='https://aip.baidubce.com/oauth/2.0/token'
    data={'grant_type':'client_credentials','client_id':api_key,'client_secret':api_secret}
    access_token=requests.post(url,data=data).json()['access_token']
    return access_token

access_token=api_to_access_token(api_key,api_secret)

def base64_encode(image_name):
    opener = open(image_name, 'rb')
    changer = base64.b64encode(opener.read())
    opener.close()
    image_base6_4 = changer
    return image_base6_4

def get_key(img_name):  #识别图片中的关键
    url='https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token={}'.format(access_token)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    image_base64=base64_encode(img_name)
    data={'image':image_base64}
    try:
        result=requests.post(url,headers=headers,data=data).json()
        b = len(result['result'])
        key = ''
        for i in range(b):
            c = result['result'][i]['keyword']
            key = key + c + ','
        #print(key)
        return key
    except:
        pass

def img_finder(): #得到路经
    path = 'picture'
    list=[]
    for root, dirs, files in os.walk(path):
        for file in files:
            img_path=os.path.join(root, file)
            img_path = img_path.replace('\\', "/")
            #print (img_path)
            list.append(img_path)
   # print (list[0])
    return list

def add_data(): #加入数据
    path=img_finder()
    f=len(img_finder())
    for i in range(0,f):
        form_one(i, f)
        img_name=img_finder()[i]
        w=get_key(img_name)
        if w== None:
            pass
        else:
            db_join(w,img_name)
            #print(w,img_name)
    print ('successful,the pictures are added to the db')

#add_data()
#db_delete('data')
#print(db_search('狗'))






