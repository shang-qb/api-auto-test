import pytest
import os
import subprocess

if __name__ == "__main__":
    # 运行测试并生成Allure结果
    pytest.main([
        "-v",
        "--alluredir=reports/allure-results",
        "--clean-alluredir",
        "test_cases"
    ])

    # 自动生成Allure报告（需要安装allure命令行工具）
    try:
        subprocess.run([
            "allure", "generate", "reports/allure-results",
            "-o", "reports/allure-report", "--clean"
        ], check=True)
        print("Allure报告已生成: reports/allure-report/index.html")
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("Allure命令行工具未安装，跳过报告生成。安装方法见README.md")
