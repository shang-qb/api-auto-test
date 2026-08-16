import pytest
import yaml
import allure
import os
from common.request_util import RequestUtil
from common.assert_util import AssertUtil

# 读取测试数据
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'user_data.yaml')
with open(data_path, 'r', encoding='utf-8') as f:
    test_data = yaml.safe_load(f)


@allure.feature("用户管理模块")
class TestUser:

    @classmethod
    def setup_class(cls):
        cls.req = RequestUtil("http://localhost:8080")
        cls.assert_util = AssertUtil()

    @allure.story("用户登录")
    @pytest.mark.parametrize("case", test_data["test_login"])
    def test_login(self, case):
        """测试用户登录接口"""
        allure.dynamic.title(case["case_name"])

        payload = {
            "username": case["username"],
            "password": case["password"]
        }
        response = self.req.post("/api/user/login", json=payload)
        result = response.json()

        self.assert_util.assert_status_code(response, 200)
        self.assert_util.assert_code(result, case["expected_code"])

    @allure.story("用户注册")
    @pytest.mark.parametrize("case", test_data["test_register"])
    def test_register(self, case):
        """测试用户注册接口"""
        allure.dynamic.title(case["case_name"])

        payload = {
            "username": case["username"],
            "password": case["password"],
            "email": case["email"]
        }
        response = self.req.post("/api/user/register", json=payload)
        result = response.json()

        self.assert_util.assert_status_code(response, 200)
        self.assert_util.assert_code(result, case["expected_code"])
