# 接口自动化测试框架

基于 Python + Pytest + Requests + Allure 的接口自动化测试框架，用于测试博客管理系统的后端API。

## 技术栈

- Python 3.10+
- Pytest（测试框架）
- Requests（HTTP请求库）
- Allure（测试报告）
- PyYAML（测试数据管理）
- PyMySQL（数据库操作）

## 项目结构

```
api-auto-test/
├── common/                    # 公共模块
│   ├── request_util.py        # 请求封装
│   ├── assert_util.py         # 断言封装
│   └── db_util.py             # 数据库操作
├── config/                    # 配置文件
│   ├── config.yaml            # 环境配置
│   └── conftest.py            # Pytest全局配置
├── data/                      # 测试数据（YAML）
│   ├── user_data.yaml
│   ├── article_data.yaml
│   └── comment_data.yaml
├── test_cases/                # 测试用例
│   ├── test_user.py
│   ├── test_article.py
│   └── test_comment.py
├── reports/                   # 测试报告输出目录
├── logs/                      # 日志目录
├── run.py                     # 运行入口
├── requirements.txt           # 依赖清单
└── pytest.ini                 # Pytest配置
```

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境
编辑 `config/config.yaml`，修改 base_url 和数据库连接信息。

### 3. 运行测试
```bash
# 方式一：直接运行
python run.py

# 方式二：用pytest命令
pytest test_cases/ -v

# 方式三：指定环境运行
set TEST_ENV=prod
pytest test_cases/ -v
```

### 4. 查看报告
```bash
# 生成Allure报告（需先安装allure命令行工具）
allure generate reports/allure-results -o reports/allure-report --clean

# 打开报告
allure open reports/allure-report
```

## Allure安装

1. 下载：https://github.com/allure-framework/allure2/releases
2. 解压后将 bin 目录加入系统环境变量 PATH
3. 验证：`allure --version`
4. 需要 JDK 环境（Allure 依赖 Java）

## 测试模块

| 模块 | 测试文件 | 覆盖接口 |
|---|---|---|
| 用户管理 | test_user.py | 登录、注册 |
| 文章管理 | test_article.py | 列表查询、发布文章 |
| 评论管理 | test_comment.py | 评论列表、发表评论 |

## 亮点

- 数据驱动：测试数据与代码分离，YAML管理
- 统一封装：请求、断言、数据库操作统一封装
- 精美报告：Allure生成可视化测试报告
- 多环境支持：test/prod环境切换
- 参数化：Pytest参数化执行多条用例
