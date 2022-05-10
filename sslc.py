from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://karresults.nic.in/first_sslc_kar21.asp")


input=driver.find_element_by_xpath('//*[@id="InputRegno"]')
input.send_keys('2021109991')

#select day,month,year and leave it 

time.sleep(10)

button=driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/form/button').click()










