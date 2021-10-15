import requests

def get_token():
    r = requests.get(url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww100240802e0773ff&corpsecret=ZPIQz1cHZeVS_QU2MzppQ2cKxsdfDWBrIqgCKSgIne8')
    token = r.json()['access_token']
    #print(r.json()['access_token'])
    return token

def test_get_member():
    #获取id是Linke的成员信息
    get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={get_token()}&userid=Linke'
    r =requests.get(url = get_member_url)
    print(r.json())

def test_create_member():
    #创建一个名为MiFa的成员
    create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={get_token()}'
    data = {
        "userid": "MiFa",
        "name": "米法",
        "mobile": "+86 13800001234",
        "department": [2]
    }

    r = requests.post(url=create_member_url, json=data)

    print(r.json())

def test_del_member():
    #删除一个名为MiFa的成员
    del_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={get_token()}&userid=MiFa"


    r = requests.get(url=del_member_url)
    print(r.json())

