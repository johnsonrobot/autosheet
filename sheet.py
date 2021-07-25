from selenium import webdriver
from datetime import date
import configparser

config = configparser.ConfigParser()
config.read("config.ini")

url = config.get("url", "path")
user = config.get("user", "user")
pwd = config.get("user", "pwd")
id = config.get("user", "id")

user_ele = config.get("user_element", "user")
user_next = config.get("user_element", "next")

pwd_ele = config.get("pwd_element", "pwd")
pwd_next = config.get("pwd_element", "next")

id_ele = config.get("sheet_element", "user_id")

today = date.today()

option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation'])

google = webdriver.Chrome(options=option)
google.get(url)

google.find_element_by_name(user_ele).send_keys(user)
google.find_element_by_xpath(user_next).click()

google.implicitly_wait(5)

google.find_element_by_name(pwd_ele).send_keys(pwd)
google.find_element_by_xpath(pwd_next).click()

google.implicitly_wait(50)
#id
google.find_element_by_class_name(id_ele).send_keys(id)  
#month
google.find_element_by_xpath("//form[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/div[2]/div/div/div/input").send_keys(today.month)
#day
google.find_element_by_xpath("//form[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/input").send_keys(today.day)
#radiobutton
google.find_element_by_xpath("//div[@id='i13']/div[3]/div").click()
#next
google.find_element_by_xpath("//form[@id='mG61Hd']/div[2]/div/div[3]/div/div/div/span/span").click()
#radiobutton
google.find_element_by_xpath("//div[@id='i5']/div[3]/div").click()
#next
google.find_element_by_xpath("//form[@id='mG61Hd']/div[2]/div/div[3]/div/div/div[2]/span/span").click()
# submit
