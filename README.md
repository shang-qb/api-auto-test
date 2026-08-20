# 接口自动化测试框架

基于 Python + Pytest + Requests + Allure 的企业级接口自动化测试框架，用于测试博客管理系统的后端 API，支持数据驱动、多环境切换、可视化测试报告。

## 技术栈

| 技术 | 用途 | 版本 |
|---|---|---|
| Python | 开发语言 | 3.10+ |
| Pytest | 测试框架 | 7.0+ |
| Requests | HTTP 请求库 | 2.28+ |
| Allure | 测试报告 | 2.12+ |
| PyYAML | 测试数据管理 | 6.0+ |
| PyMySQL | 数据库操作 | 1.0+ |
| OpenPyXL | Excel 数据驱动 | 3.0+ |

## 项目结构

```
api-auto-test/
├── common/                        # 公共模块
│   ├── __init__.py
│   ├── request_util.py            # HTTP 请求统一封装
│   ├── assert_util.py             # 断言工具类封装
│   └── db_util.py                 # 数据库操作封装
├── config/                        # 配置文件
│   ├── config.yaml                # 多环境配置（test/prod）
│   └── conftest.py                # Pytest 全局 Fixture 配置
├── data/                          # 测试数据（YAML 数据驱动）
│   ├── user_data.yaml             # 用户模块测试数据
│   ├── article_data.yaml          # 文章模块测试数据
│   └── comment_data.yaml          # 评论模块测试数据
├── test_cases/                    # 测试用例
│   ├── test_user.py               # 用户模块测试用例
│   ├── test_article.py            # 文章模块测试用例
│   └── test_comment.py            # 评论模块测试用例
├── reports/                       # 测试报告输出目录
│   ├── allure-results/            # Allure 原始结果
│   └── allure-report/             # Allure HTML 报告
├── logs/                          # 日志目录
├── run.py                         # 测试运行入口
├── requirements.txt               # Python 依赖清单
└── pytest.ini                     # Pytest 配置文件
```

## 框架设计

### 1. 数据驱动设计
测试数据与测试代码分离，使用 YAML 文件管理测试数据，支持参数化执行多条用例，新增用例只需修改 YAML 文件，无需改动代码。

### 2. 统一封装设计
- **请求封装**：统一处理 GET/POST/PUT/DELETE 请求，自动记录请求日志
- **断言封装**：封装状态码、业务码、响应消息、非空等常用断言
- **数据库封装**：封装增删改查操作，支持测试数据初始化和清理

### 3. 多环境支持
通过 `TEST_ENV` 环境变量切换 test/prod 环境，配置统一管理在 `config.yaml` 中。

### 4. 可视化报告
集成 Allure 测试报告，支持用例分类、步骤展示、附件添加，生成精美的 HTML 测试报告。

## 快速开始

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 配置环境
编辑 `config/config.yaml`，修改 base_url 和数据库连接信息：
```yaml
test:
  base_url: "http://localhost:8080"
  db:
    host: "localhost"
    port: 3306
    user: "root"
    password: "root"
    database: "blog_db"
```

### 3. 运行测试
```bash
# 方式一：运行入口（自动生成报告）
python run.py

# 方式二：Pytest 命令运行
pytest test_cases/ -v

# 方式三：指定运行某个模块
pytest test_cases/test_article.py -v

# 方式四：指定环境运行
set TEST_ENV=prod
pytest test_cases/ -v
```

### 4. 查看 Allure 报告
```bash
# 生成 HTML 报告
allure generate reports/allure-results -o reports/allure-report --clean

# 浏览器打开报告
allure open reports/allure-report
```

## Allure 安装

1. 下载 Allure 命令行工具：https://github.com/allure-framework/allure2/releases
2. 解压 `allure-2.x.x.zip`，将 `bin` 目录加入系统环境变量 PATH
3. 验证安装：`allure --version`
4. 依赖 JDK 环境（Allure 报告生成需要 Java）

## 测试模块覆盖

| 模块 | 测试文件 | 用例数 | 覆盖接口 |
|---|---|---|---|
| 用户管理 | test_user.py | 4 | 登录（正常/密码错误/用户不存在）、注册 |
| 文章管理 | test_article.py | 5 | 列表查询（分页/搜索）、发布文章（正常/异常） |
| 评论管理 | test_comment.py | 2 | 评论列表、发表评论 |

## 测试用例示例

### YAML 测试数据
```yaml
test_login:
  - case_name: "正常登录"
    username: "admin"
    password: "123456"
    expected_code: 200
  - case_name: "密码错误"
    username: "admin"
    password: "wrongpass"
    expected_code: 401
```

### Pytest 测试用例
```python
@allure.feature("用户管理模块")
class TestUser:
    @allure.story("用户登录")
    @pytest.mark.parametrize("case", test_data["test_login"])
    def test_login(self, case):
        allure.dynamic.title(case["case_name"])
        response = self.req.post("/api/user/login", json={
            "username": case["username"],
            "password": case["password"]
        })
        self.assert_util.assert_status_code(response, 200)
        self.assert_util.assert_code(response.json(), case["expected_code"])
```

## 项目亮点

1. **数据驱动**：测试数据与代码分离，YAML 管理，新增用例零代码改动
2. **统一封装**：请求、断言、数据库操作三层封装，减少重复代码，提升可维护性
3. **Allure 可视化报告**：精美的 HTML 测试报告，支持用例分类、步骤展示、趋势分析
4. **多环境支持**：test/prod 环境一键切换，配置统一管理
5. **Pytest 参数化**：一条用例代码执行多条测试数据，提升用例覆盖率
6. **日志记录**：自动记录请求和响应日志，便于问题定位和调试
7. **Fixture 机制**：利用 Pytest conftest 实现测试前置后置，环境配置统一注入

## 持续集成

框架支持接入 CI/CD 流水线：
```bash
# Jenkins/GitHub Actions 中执行
pip install -r requirements.txt
pytest test_cases/ -v --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
```

## 许可证

MIT License
