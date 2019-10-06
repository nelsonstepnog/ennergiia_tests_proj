#!/usr/bin/env python
# -*- coding: utf-8 -*-


from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC, wait
from tests.features.directories_page.main_page.main_page import MainPage

# chromeDriverExe = "utilities\chromedriver.exe"
url_main_page = "https://www.ennergiia.com"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.delete_all_cookies()
driver.get(url_main_page)
timeout = 10


def close_reg_form():
    elem_close = driver.find_elements_by_xpath(MainPage.reg_popup_close_main_page)
    if len(elem_close) == 0:
        time.sleep(0.5)
        # print("   All is ok, reg form is closed   ")
    else:
        driver.find_element_by_xpath(MainPage.reg_popup_close_main_page).click()


class Helper(object):

    @staticmethod
    def wait_for_element(by_type, locator):
        global element
        find_element = driver.find_elements(by_type, locator)
        if len(find_element) == 0:
            element = EC.presence_of_element_located((by_type, locator))
            WebDriverWait(driver, timeout).until(element)
        else:
            time.sleep(0.5)
        return locator
