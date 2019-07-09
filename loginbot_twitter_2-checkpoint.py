# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 12:25:29 2019

@author: Luis Rodriguez
"""

from selenium import webdriver
from getpass import getpass

def login_twitter(username, password):
    driver = webdriver.Chrome()
    driver.get("https://twitter.com/login")

    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    driver.implicitly_wait(1)
    
    password_field.send_keys(password)
    driver.implicitly_wait(1)

    driver.find_element_by_class_name("EdgeButtom--medium").click()


if __name__ == "__main__":
    username = input("user name : ")
    password = getpass("password  : ")
    login_twitter(username, password)