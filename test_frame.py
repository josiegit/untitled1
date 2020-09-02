# -*- coding:utf-8 -*-
from base import Base
import pytest
from selenium import webdriver
class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-example-droppable")
        self.driver.switch_to.frame("iframeResult")
        # print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.parent_frame()
