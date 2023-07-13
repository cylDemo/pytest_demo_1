import pytest

@pytest.fixture()
def login():
    print('前置进行输入账号密码登录')