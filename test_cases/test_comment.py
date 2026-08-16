import pytest
import yaml
import allure
import os
from common.request_util import RequestUtil
from common.assert_util import AssertUtil

# 读取测试数据
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'comment_data.yaml')
with open(data_path, 'r', encoding='utf-8') as f:
    test_data = yaml.safe_load(f)


@allure.feature("评论管理模块")
class TestComment:

    @classmethod
    def setup_class(cls):
        cls.req = RequestUtil("http://localhost:8080")
        cls.assert_util = AssertUtil()

    @allure.story("评论列表查询")
    @pytest.mark.parametrize("case", test_data["test_get_comment_list"])
    def test_get_comment_list(self, case):
        """测试评论列表查询接口"""
        allure.dynamic.title(case["case_name"])

        params = {"articleId": case["articleId"]}
        response = self.req.get("/api/comment/list", params=params)
        result = response.json()

        self.assert_util.assert_status_code(response, 200)
        self.assert_util.assert_code(result, case["expected_code"])

    @allure.story("发表评论")
    @pytest.mark.parametrize("case", test_data["test_save_comment"])
    def test_save_comment(self, case):
        """测试发表评论接口"""
        allure.dynamic.title(case["case_name"])

        payload = {
            "articleId": case["articleId"],
            "userId": case["userId"],
            "content": case["content"]
        }
        response = self.req.post("/api/comment/save", json=payload)
        result = response.json()

        self.assert_util.assert_status_code(response, 200)
        self.assert_util.assert_code(result, case["expected_code"])
