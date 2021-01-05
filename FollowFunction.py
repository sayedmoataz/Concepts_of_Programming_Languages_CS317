from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.keys import Keys
import tkinter as tk
# web driver that we will run our project on it
driver = webdriver.Chrome()
# make the window mazmize or fullscreen
driver.maximize_window()
# go to instagram website
driver.get("https://www.instagram.com/")
# wait 8 seconds to load and search
driver.implicitly_wait(8)
# find the username input field and write the passed email
# replace "User9596917" with the email that will like ,comment or follow others
# replace "medO123@!" with the password of new email
username = driver.find_element_by_css_selector("input[name='username']").send_keys(show().my_email)
password = driver.find_element_by_css_selector("input[name='password']").send_keys(show().my_password)
# wait for loadding
sleep(5)
# while openning instagram there is a pop-up shown to enable notification
driver.get("https://www.instagram.com/")
# this code to cancle it
if driver.find_elements_by_css_selector('div.mt3GC > button.aOOlW.HoLwm'):
    driver.find_element_by_css_selector("div.mt3GC > button.aOOlW.HoLwm").click()  # click at "Not now" botton
driver.get("https://www.instagram.com/explore/people/suggested/")
#now we will go to "Suggestions For You" section to follow more accounts
for x in range(100):
    #press on follow button for the first 100 account with 5 second delay
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div[i]/div[3]/button").click()
    sleep(5)