#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-08 11:34:34
# @Author  : xujn
# @Version : 1


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class PythonSearch(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_search_python(self):
        browser = self.browser
        browser.get('http://mail.163.com/')
        assert "163" in browser.title
        # user = browser.find_element_by_id("auto-id-1502869060479")
        # psw = browser.find_element_by_id("auto-id-1502869060482")
        # user = browser.find_element_by_xpath("//*[start-with(@id,'auto-id')]")
        # psw = browser.find_element_by_xpath("//*[start-with(@id,'auto-id')]")
        user = browser.find_element_by_class_name("j-inputtext dlemail")
        psw = browser.find_element_by_class_name("j-inputtext dlpwd")
        user.clear()
        psw.clear()
        user.send_keys("15696334323")
        psw.send_keys("xujianan1024*")
        time.sleep(5)
        psw.send_keys(Keys.RETURN)
        assert "No results found" not in browser.page_source


    def test_search_in_python_org(self):
        driver = self.browser
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
            self.browser.close()


if __name__ == "__main":
    unittest.main()

# //*[@id="auto-id-1503909247841"]
# //*[@id="auto-id-1503909247792"]