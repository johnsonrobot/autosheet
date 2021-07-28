from selenium import webdriver
from datetime import date
from time import sleep
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

vals = []
config_ele = []
head = config.sections()
for key in head:
    vals.append(config.options(key))

for key in range(len(head)):
    for val in vals[key]:
        config_ele.append(config.get(head[key], val))
        
today = date.today()

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])

google = webdriver.Chrome(options=option)
google.get(config_ele[0])

google.find_element_by_name(config_ele[4]).send_keys(config_ele[1])
google.find_element_by_xpath(config_ele[5]).click()

google.implicitly_wait(5)

google.find_element_by_name(config_ele[6]).send_keys(config_ele[2])
google.find_element_by_xpath(config_ele[7]).click()

google.implicitly_wait(50)

google.find_element_by_class_name(config_ele[8]).send_keys(config_ele[3])  
google.find_element_by_xpath(config_ele[9]).send_keys(today.month)
google.find_element_by_xpath(config_ele[10]).send_keys(today.day)
google.find_element_by_xpath(config_ele[11]).click()
google.find_element_by_xpath(config_ele[12]).click()
google.find_element_by_xpath(config_ele[13]).click()
google.find_element_by_xpath(config_ele[14]).click()
google.find_element_by_xpath(config_ele[15]).click()
sleep(3)
google.close()