user_name = 'username'
password = 'password'

from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")
driver.get('https://'+user_name+':'+password+'@munet.mu-sigma.com/Enterpriseview.aspx?html.app=EMuSigmaQMS1744d1')
time.sleep(2)

location = driver.find_element_by_xpath('/html/body/form/div[3]/div[4]/div/div/div[4]/div/div[3]/div/div/div[2]/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/div/div[3]/div/table/tbody/tr[4]/td/div/div/div/div/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[5]/div/div')
location.click()
time.sleep(2)

click_ok = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/div')
click_ok.click()
