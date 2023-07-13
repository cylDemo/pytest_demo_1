import pytest

def test_a1(login):
    print('执行测试用例a1，继承login函数，即登录后的用例')

def test_a2():
    print('用例a2不需要登录，即可执行操作')

def test_a3(login):
    print('执行测试用例a3，继承login函数，即登录后的用例')

if __name__ == '__main__':
    pytest.main()

