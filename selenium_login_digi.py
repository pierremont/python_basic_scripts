
from selenium import webdriver
import time

password = input("enter password: ")

driver = webdriver.Firefox()
#driver = webdriver.Firefox(executable_path=r'd:\\Program Files\\PyCharm Community Edition 2020.1.3\\geckodriver.exe')
driver.get('https://www.digi.ro/auth/login')
driver.maximize_window()

driver.find_element_by_name("signin-input-email").send_keys("your_user")
driver.find_element_by_name("signin-input-password").send_keys(password)
driver.find_element_by_name("signin-submit-button").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@class='btn-new btn-white webpush-cancel'][.='Nu, mulțumesc']").click()

driver.find_element_by_xpath("//a[@title='Plătește factura online']").click()
#driver.find_element_by_xpath("//a[@href='/my-account/invoices']").click()
#('//a[@href="'+url+'"]')
#driver.quit()