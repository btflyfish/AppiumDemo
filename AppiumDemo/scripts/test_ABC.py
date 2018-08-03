import pytest
import allure

class test_ABCByClass:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step('测试类级setup和teardown')
    def setup_class(self):
        print("------->setup_class")
    def teardown_class(self):
        print("------->teardown_class")

    @pytest.mark.run(order=2)
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_a(self):
        allure.attach('描述', '我是test_a函数')
        print("------->test_a")
        assert 1

    @pytest.mark.run(order=1)
    def test_b(self):
        allure.attach('描述', '我是test_b函数')
        print("------->test_b")
        assert 1   # 断言失败
