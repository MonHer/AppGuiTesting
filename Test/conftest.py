# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/17:35
# @Author : Yuye
# @File   : conftest.py

import pytest
from appium import webdriver
from Base.Action import ElementActions
from Utils.Environment import Environment


@pytest.fixture()
def action():
    env = Environment().get_environment_info()
    capabilities = {'platformName': env.devices[0].platform_name,
                    'platformVersion': env.devices[0].platform_version,
                    'deviceName': env.devices[0].device_name,
                    'app': env.apk,
                    'clearSystemFiles': True,
                    'appActivity': env.app_activity,
                    'appPackage': env.app_package,
                    'automationName': 'UIAutomator2',
                    'noSign': True
                    }
    host = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(host, capabilities)
    yield ElementActions(driver).reset(driver)
    driver.quit()


@pytest.fixture(scope="module")
def action2():
    env = Environment().get_environment_info()
    capabilities = {'platformName': env.devices[0].platform_name,
                    'platformVersion': env.devices[0].platform_version,
                    'deviceName': env.devices[0].device_name,
                    'app': env.apk,
                    'clearSystemFiles': True,
                    'appActivity': env.app_activity,
                    'appPackage': env.app_package,
                    'automationName': 'UIAutomator2',
                    'noSign': True
                    }
    host = "http://localhost:4723/wd/hub"
    driver = webdriver.Remote(host, capabilities)
    yield ElementActions(driver).reset(driver)
    driver.quit()
