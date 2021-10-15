from wework.address import Address


class TestAddress:
    def setup(self):
        self.address = Address()
        self.user_id = "MiFa"
        self.name = '米法'
        self.mobile = '+86 13800001234'
        self.department = [2]

    def test_creat_member(self):
        #创建之前删除，确保新创建成功
        self.address.del_member(self.user_id)
        r = self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        #删除无用数据
        #self.address.del_member(self.user_id)

        assert r.get("errmsg", "network error") == 'created'

        r = self.address.get_member(self.user_id)

        assert r.get("name") == self.name

    def test_delet_member(self):
        #删除之前先创建一个用户
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.del_member(self.user_id)
        assert r.get("errmsg", "network error") == 'deleted'

    def test_get_member_infomation(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        r = self.address.get_member(self.user_id)
        assert r.get("errmsg", "network error") == 'ok'

    def test_update_member(self):
        self.address.create_member(self.user_id, self.name, self.mobile, self.department)
        new_name = "塞尔达"
        r = self.address.update_member(self.user_id, new_name)
        assert r.get("errmsg", "network error") == 'updated'



