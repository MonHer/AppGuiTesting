# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/17:49
# @Author : Yuye
# @File   : S.py

from appium import webdriver
from Base.Action import ElementActions
from Utils.Environment import Environment

env = Environment().get_environment_info()
capabilities = {'platformName': env.devices[0].platform_name,
                'platformVersion': env.devices[0].platform_version,
                'deviceName': env.devices[0].device_name,
                'app': env.apk,
                'clearSystemFiles': True,
                'appActivity': env.app_activity,
                'appPackage': env.app_package,
                'automationName': 'UIAutomator2',
                'noSign': True,
                'newCommandTimeout': 60 * 100}
host = "http://localhost:4723/wd/hub"
driver = webdriver.Remote(host, capabilities)
action = ElementActions(driver)