# AppGuiTesting
基于appium封装的测试框架
#主要实现功能
1.智能安装App
2.基础操作安装
3.采用yaml文件管理对应驱动管理元素
4.使用jinja2工具yaml文件生成Pages文件
5.集成allure
6.集成Travis-CI
7.采用coverage与coveralls完成代码覆盖率的统计
8.引入watchdog监听yaml文件的变化，保证测试稳定
9.实现了本地运行环境的检测
10.实现了对运行log的封装
11。

# Appium启动方式
```
appium --address 127.0.0.1 --port 4723 --log "log_path" --log-timestamp --local-timezone --session-override
```
