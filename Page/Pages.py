# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/17:31
# @Author : Yuye
# @File   : Pages.py

from Page import Tools

pages = Tools.parse()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class HomePage:
    登录入口 = get_locater('HomePage', '登录入口')


class LoginPage:
    账户 = get_locater('LoginPage', '账户')
    密码 = get_locater('LoginPage', '密码')
    登录 = get_locater('LoginPage', '登录')