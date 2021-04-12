from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import json
import selenium

driver = webdriver.Edge()
mainPage = "https://di.fm/login"
driver.get(mainPage)
username = "tavn1992@gmail.com"
login_page = "http://di.fm/login"

print(os.getcwd())

with open(os.getcwd() + "\diwnloader"  + "\login.json") as k:
    keys = json.load(k)



driver.find_element_by_name('member_session[username]').send_keys(keys['username'])
driver.find_element_by_name('member_session[password]').send_keys(keys['password'])

driver.find_element_by_class_name('btn.submit-btn').click()