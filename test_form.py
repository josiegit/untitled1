# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
import pytest
"""提交登陆表单"""
class TestForm():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()
    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("josiegit")
        self.driver.find_element_by_id("user_password").send_keys("23632680a")
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[4]/input").click()
        sleep(3)