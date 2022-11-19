import datetime
import time
import allure

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base
from utilities.logger import Logger


class Finish_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators






    #Getters




    # Actions



    # Methods

    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method="finish")
            self.get_current_url()
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="finish")

