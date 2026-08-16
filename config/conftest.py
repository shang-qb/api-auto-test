import pytest
import yaml
import os
import logging

# 读取配置文件
config_path = os.path.join(os.path.dirname(__file__), 'config.yaml')
with open(config_path, 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 默认使用test环境
env = os.environ.get('TEST_ENV', 'test')
current_config = config[env]


@pytest.fixture(scope='session')
def base_url():
    """返回基础URL"""
    return current_config['base_url']


@pytest.fixture(scope='session')
def db_config():
    """返回数据库配置"""
    return current_config['db']


@pytest.fixture(scope='function', autouse=True)
def log_separator():
    """每个用例之间打印分隔线"""
    logging.info("=" * 60)
    yield
    logging.info("=" * 60)
