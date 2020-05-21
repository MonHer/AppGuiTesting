# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/17:39
# @Author : Yuye
# @File   : Test_home.py

from Base.Action import ElementActions
from Page.Pages import *
from Test.steps import Steps
from Utils import Log


class TestLogin:
    def test_login(self, action: ElementActions):
        Log.d('test_login')
        account = Steps.get_account()
        action.click(HomePage.登录入口)
        action.text(LoginPage.账户, account[0])
        action.text(LoginPage.密码, account[1])
        action.sleep(1)
        action.click(LoginPage.登录)
        assert action.is_toast_s