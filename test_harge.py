# -*- coding:utf-8 -*-
from selenium import webdriver
import time
class TestHog():
     def setup(self):
          self.driver=webdriver.Chrome()
          self.driver.maximize_window()
          self.driver.implicitly_wait(5)#隐性等待

     #资源回收
     def teardown(self):
          self.driver.quit()

     def test_hog(self):
          self.driver.get("https://testerhome.com/")
          self.driver.find_element_by_link_text("社区").click()
          self.driver.find_element_by_css_selector(".topic-25074 .title > a").click()
          time.sleep(10)