# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/17:36
# @Author : Yuye
# @File   : steps.py

from Utils import Log
from Utils.Environment import Environment


class Steps:
    @staticmethod
    @allure.step(title="获取账号和密码")
    def get_account():
        account = Environment().get_inited_config().account_success
        pwd = Environment().get_inited_config().password_success
        Log.d('账号:%s 密码 %s' % (account, pwd))
        return [account, pwd]