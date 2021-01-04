from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from time import sleep
import time
from selenium.webdriver.common.keys import Keys

####################################
######## PUT GUI CODE HERE #########
####################################
#web driver that we will run our project on it
driver = webdriver.Chrome()
#make the window mazmize or fullscreen
driver.maximize_window()
#go to instagram website
driver.get("https://www.instagram.com/")
#wait 8 seconds to load and search
driver.implicitly_wait(8)
#find the username input field and write the passed email
# replace "User9596917" with the email that will like ,comment or follow others
#replace "medO123@!" with the password of new email
username = driver.find_element_by_css_selector("input[name='username']").send_keys("User9596917")
password = driver.find_element_by_css_selector("input[name='password']").send_keys("medO123@!"+Keys.ENTER)
#wait for loadding
sleep(5)
#while openning instagram there is a pop-up shown to enable notification
#this code to cancle it
if driver.find_elements_by_css_selector('div.mt3GC > button.aOOlW.HoLwm'):
    driver.find_element_by_css_selector("div.mt3GC > button.aOOlW.HoLwm").click()  #click at "Not now" botton
#do a search to find the user that we will like or comment his/her posts
#replace "instagram" with destination person
driver.find_element_by_css_selector("div.LWmhU._0aCwM > input").send_keys("mohammad._.kher")  # Search about instagram
sleep(4)
#make sure from the username as we will select first search result here
firstChoice = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[4]/div/a[1]").click()
sleep(2)
#now we will go to his/her posts by clicking on post button
post = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/article/div/div/div[1]/div[1]/a").click()
sleep(2)
#check if we do a like berfore or not if no -> press yes and print "Not Liked" if yes print -> "Already Liked"
likeFlag = driver.find_element_by_css_selector("article[role='presentation'] div > section > span > button > div > span > svg").get_attribute('aria-label')
if likeFlag == 'Like':
    print('Not Liked.')
    like_btn = driver.find_element_by_css_selector(' span.fr66n > button > div > span > svg')
    like_btn.click()
else:
    print('Already Liked.')
sleep(2)
#now it's the time to comment so we will find the comment textarea by class name
#make the bot to write anything u want
textArea = driver.find_element_by_class_name("Ypffh")
textArea.click()
textArea.send_keys(" Hi , It's my new project : Instabot ;) " + Keys.ENTER)
sleep(4)
#after comment go to the next post and print "success"
nextPic = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a").click()
print("success")
sleep(2)
#repeat the previous code 10 times
for i in range(10):
    driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.fr66n > button").click()
    sleep(2)
    textArea = driver.find_element_by_class_name("Ypffh")
    textArea.click()
    sleep(2)
    textArea = driver.find_element_by_class_name("Ypffh")
    textArea.send_keys("Hi I'm not a Bot ;)" + Keys.ENTER)
    sleep(5)
    nextPic = driver.find_element_by_css_selector("body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow")
    nextPic.click()
    print("success")
    sleep(2)
#now we will go to "Suggestions For You" section to follow more accounts
driver.get("https://www.instagram.com/explore/people/suggested/")
for x in range(100):
    #press on follow button for the first 100 accounr with 5 second delay
    driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[2]/div/div/div[i]/div[3]/button").click()
    sleep(5)