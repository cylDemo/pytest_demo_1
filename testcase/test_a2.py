import pytest

def test_a4(login):
    print('执行测试用例a4，继承login函数，即登录后的用例')

def test_a5():
    print('用例a5不需要登录，即可执行操作')


if __name__ == '__main__':
    pytest.main()