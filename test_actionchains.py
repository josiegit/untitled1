# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver import ActionChains
import pytest
from time import sleep
from selenium.webdriver.common.keys import Keys

class TestActionChains():
    def setup(self):
        self.driver=webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    """单击/右击/双击"""
    # def test_case_click(self):
    # self.driver.get("http://sahitest.com/demo/clicks.htm")
    #     element_click=self.driver.find_element_by_xpath("//input[@value='click me']")
    #     element_dblclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
    #     element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
    #     action=ActionChains(self.driver)
    #     action.click(element_click)
    #     #右击
    #     action.context_click(element_rightclick)
    #     #双击
    #     action.double_click(element_dblclick)
    #     sleep(3)
    #     action.perform()
    #     sleep(3)
    # """查看悬浮菜单"""
    # @pytest.mark.skip
    # def test_movetoelement(self):
    #     self.driver.get("https://www.baidu.com/")
    #     ele = self.driver.find_element_by_id("s-usersetting-top")
    #     action = ActionChains(self.driver)
    #     action.move_to_element(ele)
    #     action.perform()
    #     sleep(3)
    # """拖放"""
    # def test_dragdrop(self):
    #     self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
    #     self.driver.implicitly_wait(5)
    #     drag_element=self.driver.find_element_by_id("dragger")
    #     drop_element=self.driver.find_element_by_class_name("item")
    #     action=ActionChains(self.driver)
    #     action.drag_and_drop(drag_element,drop_element).perform()
    #     sleep(3)
    """模拟键盘输入"""
    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele=self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action=ActionChains(self.driver).pause(1)
        action.send_keys("haha").pause(1)
        action.send_keys(Keys.SPACE).pause(1)#空格
        action.send_keys("to").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)

if __name__=='__main__':
    pytest.main('-v','-s','test_actionchains.py')