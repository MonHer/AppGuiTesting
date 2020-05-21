# -*- coding: utf-8 -*-
# @Pjname ; AppGuiTesting
# @Time   : 2020/05/21/17:51
# @Author : Yuye
# @File   : Watch_Dog.py


import time

from watchdog.events import PatternMatchingEventHandler
from watchdog.observers import Observer

from Page.Tools import GenPages
from Utils import Log
from Utils.Environment import Environment


def gen_page_py():
    GenPages.gen_page_py()


class WatchHandler(PatternMatchingEventHandler):
    patterns = ["*.yaml"]

    def on_modified(self, event):
        Log.i('监听到文件: yaml 发生了变化')
        try:
            gen_page_py()
        except Exception as e:
            Log.e('\n!!!!!!!---pages.yaml---!!!!!!\n解析文件 pages.yaml 错误\n'
                '请到{}路径下检查修改后重新保存.'.format(self.watch_path))


if __name__ == "__main__":
    event_handler = WatchHandler()
    full_path = Environment().get_environment_info().pages_yaml
    print(full_path)
    observer = Observer()
    observer.schedule(event_handler, full_path)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
