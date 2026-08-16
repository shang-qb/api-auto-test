import pytest
import yaml
import allure
import os
from common.request_util import RequestUtil
from common.assert_util import AssertUtil

# 读取测试数据
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'article_data.yaml')
with open(data_path, 'r', encoding='utf-8') as f:
    test_data = yaml.safe_load(f)


@allure.feature("文章管理模块")
class TestArticle:

    @classmethod
    def setup_class(cls):
        cls.req = RequestUtil("http://localhost:8080")
        cls.assert_util = AssertUtil()

    @allure.story("文章列表查询")
    @pytest.mark.parametrize("case", test_data["test_get_article_list"])
    def test_get_article_list(self, case):
        """测试文章分页查询接口"""
        allure.dynamic.title(case["case_name"])

        params = {
            "pageNum": case["pageNum"],
            "pageSize": case["pageSize"]
        }
        if "keyword" in case:
            params["keyword"] = case["keyword"]

        response = self.req.get("/api/article/list", params=params)
        result = response.json()

        self.assert_util.assert_status_code(response, 200)
        self.assert_util.assert_code(result, case["expected_code"])
        assert "records" in result["data"], "响应数据中应包含records字段"

    @allure.story("发布文章")
    @pytest.mark.parametrize("case", test_data["test_save_article"])
    def test_save_article(self, case):
        """测试文章发布接口"""
        allure.dynamic.title(case["case_name"])

        payload = {
            "title": case["title"],
            "content": case["content"],
            "userId": case["userId"],
            "categoryId": case["categoryId"]
        }
        response = self.req.post("/api/article/save", json=payload)
        result = response.json()

        self.assert_util.assert_status_code(response, 200)
        self.assert_util.assert_code(result, case["expected_code"])
