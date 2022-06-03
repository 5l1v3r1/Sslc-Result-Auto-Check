from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()

driver.get("https://kseeb.karnataka.gov.in/sslcmainexamresults2022/")

input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtReg"]')
input.send_keys('20220429543') #put your reg no

#time.sleep(2)

dropdown = Select(driver.find_element_by_id("ContentPlaceHolder1_ddlDay"))
dropdown.select_by_value("27") #put your date of birth date

time.sleep(2)

dropdown = Select(driver.find_element_by_id("ContentPlaceHolder1_ddlMonth"))
dropdown.select_by_value("05") #put your date of birth month

time.sleep(2)

dropdown = Select(driver.find_element_by_id("ContentPlaceHolder1_ddlYear"))
dropdown.select_by_value("2006") #put your date of birth year

#time.sleep(2)

input=driver.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnview"]').click()

time.sleep(3)











