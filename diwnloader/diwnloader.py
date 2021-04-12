from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

driver = webdriver.Edge()
mainPage = "https://di.fm/login"
driver.get(mainPage)
username = "tavn1992@gmail.com"
login_page = "http://di.fm/login"
session_requests = requests.session()



driver.find_element_by_name('member_session[username]').send_keys(payload[0])

