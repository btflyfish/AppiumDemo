import pytest
import allure

class test_ABC:
    # 函数级开始
    @allure.step('测试函数级setup和teardown')
    def setup(self):
        print("------->setup_method")
    # 函数级结束
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def teardown(self):
        print("------->teardown_method")
    def test_a(self):
        allure.attach('描述', '我是test_a函数')
        print("------->test_a")
        assert 1
    #test_b函数应用
    def test_b(self):
        allure.attach('描述', '我是test_b函数')
        print("------->test_b")
