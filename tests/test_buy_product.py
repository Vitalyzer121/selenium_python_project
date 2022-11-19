import datetime
import time
import pytest
import allure

from pages.finish_page import Finish_page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.client_information_page import Client_information_page
from pages.payment_page import Payment_page


# @pytest.mark.run(order=3)
@allure.description("Test buy product 1")
def test_buy_product_1():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path="C:\\Python39\\resource\\chromedriver.exe", chrome_options=options)

    print("Start Test 1")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_products_1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    cip = Client_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.click_finish_button()

    f = Finish_page(driver)
    f.finish()

    print("Finish Test 1")
    #time.sleep(10)
    driver.quit()

# @pytest.mark.run(order=1)
# def test_buy_product_2():
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(executable_path="C:\\Python39\\resource\\chromedriver.exe", chrome_options=options)
#
#     print("Start Test 2")
#
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)
#     mp.select_products_2()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
#     print("Finish Test 2")
#     time.sleep(10)
#     driver.quit()
#
# @pytest.mark.run(order=2)
# def test_buy_product_3():
#     options = Options()
#     options.add_experimental_option('excludeSwitches', ['enable-logging'])
#     driver = webdriver.Chrome(executable_path="C:\\Python39\\resource\\chromedriver.exe", chrome_options=options)
#
#     print("Start Test 3")
#
#     login = Login_page(driver)
#     login.authorization()
#
#     mp = Main_page(driver)
#     mp.select_products_3()
#
#     cp = Cart_page(driver)
#     cp.click_checkout_button()
#
#     print("Finish Test 3")
#     time.sleep(10)
#     driver.quit()







