import requests

from wework.base import Base


class Address(Base):


    def get_member(self,userid):
        # 获取id是Linke的成员信息
        get_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get'
        parmas = {
            "userid" : userid
        }
        r = self.s.get(url=get_member_url, params=parmas)
        return r.json()

    def create_member(self, userid, name, mobile, department):
        # 创建一个名为MiFa的成员
        create_member_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create'
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }

        r = self.s.post(url=create_member_url, json=data)

        return r.json()

    def del_member(self, userid):
        # 删除一个名为MiFa的成员
        del_member_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {"userid": userid}
        r = self.s.get(url=del_member_url, params=params)
        # print(r.json())
        return r.json()

    def update_member(self, userid, name):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid" : userid,
            "name" : name
        }

        r = self.s.post(url=update_url,json=data)
        return r.json()