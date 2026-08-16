import logging


class AssertUtil:
    @staticmethod
    def assert_status_code(response, expected_code=200):
        """断言响应状态码"""
        assert response.status_code == expected_code, \
            f"状态码断言失败，实际: {response.status_code}, 预期: {expected_code}"
        logging.info(f"状态码断言通过: {response.status_code}")

    @staticmethod
    def assert_code(result, expected_code=200):
        """断言业务状态码"""
        assert result.get("code") == expected_code, \
            f"业务码断言失败，实际: {result.get('code')}, 预期: {expected_code}"
        logging.info(f"业务码断言通过: {result.get('code')}")

    @staticmethod
    def assert_message(result, expected_msg):
        """断言响应消息"""
        assert result.get("message") == expected_msg, \
            f"消息断言失败，实际: {result.get('message')}, 预期: {expected_msg}"
        logging.info(f"消息断言通过: {result.get('message')}")

    @staticmethod
    def assert_not_none(data, field_name):
        """断言字段不为空"""
        assert data is not None, f"{field_name} 不应为空"
        logging.info(f"{field_name} 非空断言通过")

    @staticmethod
    def assert_in(actual, expected_list, field_name):
        """断言值在预期列表中"""
        assert actual in expected_list, \
            f"{field_name} 断言失败，实际: {actual}, 预期范围: {expected_list}"
        logging.info(f"{field_name} 包含断言通过: {actual}")
