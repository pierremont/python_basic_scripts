
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

password = input("enter password: ")


driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path=r'd:\\Program Files\\PyCharm Community Edition 2020.1.3\\geckodriver.exe')
driver.get('https://my.enel.ro/#!ApplicationLogin')
driver.maximize_window()
time.sleep(1)

driver.find_element_by_id('gwt-uid-3').send_keys("your_user")
driver.find_element_by_id('gwt-uid-5').send_keys(password)

driver.find_element_by_xpath("//div[contains(@class, 'buton-enel')]").click()

#driver.find_element_by_css_selector('div.v-button v-widget primary v-button-primary buton-enel v-button-buton-enel pink v-button-pink margin-top v-button-margin-top v-has-width').click()
#driver.find_element_by_xpath("//button[@class='v-button v-widget primary v-button-primary buton-enel v-button-buton-enel pink v-button-pink margin-top v-button-margin-top v-has-width']").click()
#driver.find_element_by_class_name('v-button v-widget primary v-button-primary buton-enel v-button-buton-enel pink v-button-pink margin-top v-button-margin-top v-has-width').click()
#driver.find_element_by_xpath("//button[@class='v-button-caption']").click()