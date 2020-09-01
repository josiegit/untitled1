# -*- coding:utf-8 -*-
from selenium import webdriver
import pytest
from testing2.base import Base
from time import sleep

class TestWindows(Base):
    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows=self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("haha")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("13235322654")
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("xlbat6")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("23632680a")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()