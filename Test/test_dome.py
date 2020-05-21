# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/16:45
# @Author : Yuye
# @File   : test_dome.py

import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Testxiangshangwang (object):
    driver = webdriver

    @classmethod
    def setup_class(cls):
        print("setup class")
        cls.driver = cls.Starat_App()

    def setup_method(self):
        print("setup method")
        self.driver = self.Restart_App()

    def test_login(self):
        self.driver.find_element_by_id("com.up360.teacher.android.activity:id/username").send_keys("18682344378")
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("com.up360.teacher.android.activity:id/pwd").send_keys("123456")
        self.driver.implicitly_wait(3)
        self.driver.find_element_by_id("com.up360.teacher.android.activity:id/login").click()
        time.sleep(6)
        TouchAction(self.driver).press(x=337, y=1127).move_to(x=325, y=316).release().perform()

    def test_fabulinaxi(self):
        self.driver.find_element_by_xpath("//*[@text='发布练习']").click()

    def teardown_method(self):
        self.driver.quit()

    @classmethod
    def Install_App(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "7.1.2"
        caps["deviceName"] = "xiaoyao"
        caps["app"] = "/Apk/.apk"
        caps["autoGrantPermissions"] = "true"

    @classmethod
    def Starat_App(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "7.1.2"
        caps["deviceName"] = "xiaoyao"
        caps["appPackage"] = "com.up360.teacher.android.activity"
        caps["appActivity"] = ".ui.IndexActivity"
        caps["autoGrantPermissions"] = "true"
        caps["resetKeyboard"] = "true"
        caps["unicodeKeyboard"] = "true"
        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(6)
        return driver

    @classmethod
    def Restart_App(cls):
        caps = {}
        caps["platformName"] = "android"
        caps["platformVersion"] = "7.1.2"
        caps["deviceName"] = "xiaoyao"
        caps["appPackage"] = "com.up360.teacher.android.activity"
        caps["appActivity"] = ".ui.IndexActivity"
        caps["autoGrantPermissions"] = "true"
        caps["resetKeyboard"] = "true"
        caps["unicodeKeyboard"] = "true"
        caps["noReset"] = "true"
        driver = webdriver.Remote ("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait (6)
        return driver
