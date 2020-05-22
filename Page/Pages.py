# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/15:49
# @Author : Yuye
# @File   : pages

from Page import Tools

pages = Tools.parse()


def get_locater(clazz_name, method_name):
    locators = pages[clazz_name]['locators']
    for locator in locators:
        if locator['name'] == method_name:
            return locator


class HomePage:
    发布练习 = get_locater('HomePage', '发布练习')

    
class LoginPage:
    账号 = get_locater('LoginPage', '账号')
    密码 = get_locater('LoginPage', '密码')
    登录 = get_locater('LoginPage', '登录')