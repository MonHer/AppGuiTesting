# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/17:48
# @Author : Yuye
# @File   : run.py

import pytest
from Utils.Environment import Environment
from Utils.Shell import Shell
from Utils import Log
import sys

"""
run all case:
    python run.py

run one module case:
    python run.py test/test_home.py

run case with key word:
    python run.py -k <keyword>

"""

if __name__ == '__main__':
    env = Environment()
    xml_report_path = env.get_environment_info().xml_report
    html_report_path = env.get_environment_info().html_report
    # 开始测试
    args = ['-s', '-q', '--alluredir', xml_report_path]
    self_args = sys.argv[1:]
    pytest.main(args + self_args)
    # 生成html测试报告
    cmd = "allure generate %s -o %s" % (xml_report_path, html_report_path)
    try:
        Shell.invoke(cmd)
    except:
        Log.e("Html测试报告生成失败,确保已经安装了Allure-Commandline")
