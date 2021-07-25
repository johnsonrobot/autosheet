from selenium import webdriver
from datetime import date
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

url = config.get("url", "path")
user = config.get("user", "user")
x = config.get("user", "x")
id = config.get("user", "id")

user_ele = config.get("user_element", "user")
user_next = config.get("user_element", "next")

y_ele = config.get("y_element", "y")
y_next = config.get("y_element", "next")

id_ele = config.get("sheet_element", "user_id")
mon_ele = config.get("sheet_element", "month")
day_ele = config.get("sheet_element", "day")
radio1_ele = config.get("sheet_element", "radio1")
radio2_ele = config.get("sheet_element", "radio2")
next1_ele = config.get("sheet_element", "next1")
next2_ele = config.get("sheet_element", "next2")

today = date.today()

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])

google = webdriver.Chrome(options=option)
google.get(url)

google.find_element_by_name(user_ele).send_keys(user)
google.find_element_by_xpath(user_next).click()

google.implicitly_wait(5)

google.find_element_by_name(y_ele).send_keys(x)
google.find_element_by_xpath(y_next).click()

google.implicitly_wait(50)

google.find_element_by_class_name(id_ele).send_keys(id)  
google.find_element_by_xpath(mon_ele).send_keys(today.month)
google.find_element_by_xpath(day_ele).send_keys(today.day)
google.find_element_by_xpath(radio1_ele).click()
google.find_element_by_xpath(next1_ele).click()
google.find_element_by_xpath(radio2_ele).click()
google.find_element_by_xpath(next2_ele).click()
# submit
