# -*- coding:utf-8 -*-
"""
    打开chrome->
    打开百度页面->
    搜索框输入selenium测试->
    通过TouchAction点击搜索框->
    滑动到底部，点击下一页->
    关闭Chrome
"""
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
import pytest

from time import sleep
class TestTouchAction():
    def setup(self):
        option=webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver=webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollbotton(self):
        self.driver.get("https://www.baidu.com/")
        ele=self.driver.find_element_by_id("kw")
        ele_search=self.driver.find_element_by_id("su")
        ele.send_keys("selenium测试")
        action=TouchActions(self.driver)
        action.tap(ele_search).perform()
        action.scroll_from_element(ele,0,10000).perform()
        sleep(3)

if __name__=="__main__":
    pytest.main('-v','-s',test_touchaction.py)

