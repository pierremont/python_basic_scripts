

from selenium import webdriver
#from selenium.webdriver.common.by import By
import time

password = input("enter password: ")

driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path=r'd:\\Program Files\\PyCharm Community Edition 2020.1.3\\geckodriver.exe')
driver.get('https://sso.orange.ro/wp/oro?jspname=login.jsp&action=LOGINPAGE_SSO&full_page=true')
driver.maximize_window()
#time.sleep(2)

driver.find_element_by_css_selector(".inputMaterial").click()
#time.sleep(2)
driver.find_element_by_id('login').send_keys("your_phone")
driver.find_element_by_id('password').send_keys(password)

driver.find_element_by_xpath("//button[@class='orange-btn']").click()
