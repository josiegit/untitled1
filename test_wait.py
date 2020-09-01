# -*- coding:utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class TestWait:
     def setup(self):
          self.driver=webdriver.Chrome()
          self.driver.get("https://ceshiren.com/categories")
          # self.driver.implicitly_wait(10)
     def test_wait(self):

          WebDriverWait(self.driver,10).until(EC.presence_of_element_located(By.XPATH,'//*[@class="table-heading"]')
          self.driver.find_element(By.XPATH, "//*[@title=\"在最近的一年，一月，一周或一天最活跃的主题\"]").click()