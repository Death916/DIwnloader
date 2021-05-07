from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import os
import json
import selenium
from selenium.webdriver.common.by import By
import pickle
import time

def main():
    
    driver = webdriver.Edge()
    login_page = "https://di.fm/login"
    main_page = "https://di.fm"
    driver.get(main_page)
    LOGIN = 1
    
    

    def login():
        with open(os.getcwd() + "\login.json") as k:
            keys = json.load(k)
        driver.get(login_page)
        driver.find_element_by_name('member_session[username]').send_keys(keys['username'])

        driver.find_element_by_name('member_session[password]').send_keys(keys['password'])

        driver.find_element_by_class_name('btn.submit-btn').click()
        LOGIN == 1
        


    

    def get_likes():
        likes = 'https://www.di.fm/my/likes'

        driver.get(likes)

        likes_class = driver.find_element(By.TAG_NAME, 'div')
        for e in likes_class:
            print(e.text)
    
    

    cookies = driver.get_cookies()
    if LOGIN == 0:
        print("NO COOKIES")
        login()
        pickle.dump(driver.get_cookies(), open("cookies.pk1","wb"))
        print("SAVED COOKIES")
    else:
        cookies = pickle.load(open("cookies.pk1", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.get("https://www.di.fm")    
        print("LOADED COOKIES")

    

    """if LOGIN!= 0:
        cookies = pickle.load(open("cookies.pk1", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        print("LOADED COOKIES")"""


    #get_likes()
    

main()
time.sleep(100)

