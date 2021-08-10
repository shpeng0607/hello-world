# coding:utf-8
'''
login test case
'''
import unittest
from app import app
import json

class TestLogin(unittest.TestCase):
    """定義測試案例"""

    def setUp(self):
        app.testing = True  
        self.client = app.test_client()
        self.expect_result = {'identity': 'Wrong id or password!'}
    
    def test_empty_name_password(self):
        """測試模擬場景，使用者名稱或密碼不完整"""

        response = self.client.post("/login", data={})
        resp_json = response.json
        self.assertEqual(resp_json, self.expect_result)

        response = self.client.post("/login", data={"name": "admin"})
        resp_json = response.json
        self.assertEqual(resp_json, self.expect_result)


    def test_wrong_name_password(self):
        """測試使用者名稱或密碼錯誤"""
        
        response = self.client.post("/login", data={"name": "admin", "password": "xxx"})
        resp_json = response.json
        self.assertEqual(resp_json, self.expect_result)


if __name__ == '__main__':
    unittest.main()