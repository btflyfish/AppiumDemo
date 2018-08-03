import pytest   # 引入pytest包
import allure
def test_a(): # test开头的测试函数
    print("------->test_a")
    assert 1 # 断言成功

def test_b():
    print("------->test_b")
    assert 1 # 断言失败
