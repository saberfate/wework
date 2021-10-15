import requests

class Base:
    def __init__(self):
        self.token = self.get_token()
        self.s = requests.Session()
        self.s.params = {"access_token": self.token}

    def get_token(self):
        r = requests.get(
            url='https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww100240802e0773ff&corpsecret=ZPIQz1cHZeVS_QU2MzppQ2cKxsdfDWBrIqgCKSgIne8')
        token = r.json()['access_token']
        # print(r.json()['access_token'])
        return token