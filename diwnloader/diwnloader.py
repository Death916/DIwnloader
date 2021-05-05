from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import json
import selenium

def main():
    
    driver = webdriver.Edge()
    mainPage = "https://di.fm/login"
    driver.get(mainPage)
    username = "tavn1992@gmail.com"


    print(os.getcwd())

    def login():
        with open(os.getcwd() + "\diwnloader"  + "\login.json") as k:
            keys = json.load(k)

        driver.find_element_by_name('member_session[username]').send_keys(keys['username'])

        driver.find_element_by_name('member_session[password]').send_keys(keys['password'])

        driver.find_element_by_class_name('btn.submit-btn').click()


    connect()

    def get_likes():
        likes = 'https://www.di.fm/my/likes'

        driver.get(likes)