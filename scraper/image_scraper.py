import time
from selenium.webdriver.common.keys import Keys
import selenium
import streamlit as st
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import urllib.request
import math


def img_downloader(number_of_images, sel_number, search_term, driver):
    for image in range(1, number_of_images):
        image_url = driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{image}]/a[1]/div[1]/img').get_attribute('src')
        if not os.path.exists(os.getcwd() + f"/images/{sel_number}"):
            os.makedirs(os.getcwd() + f"/images/{sel_number}")
            urllib.request.urlretrieve(image_url, os.getcwd() + f"/images/{sel_number}/" + f"{search_term}{image}.png")
        else:
            urllib.request.urlretrieve(image_url, os.getcwd() + f"/images/{sel_number}/" + f"{search_term}{image}.png")
    driver.back()



def get_driver(website_url):
    options = Options()
    options.add_extension(os.getcwd() + "/scraper" + "\cookieblocker.crx")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(40)
    driver.get(website_url)
    return driver


def number_image_scraper():
    st.write("Select number to scrape images of on the left and the click on the button below to start")
    sel_number = st.sidebar.selectbox('Select number to scrape', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    number_of_images = 24
    numbers = {0: ("Number zero", "pictures of number 0", "pictures of number zero", "number 0", "siffran 0", "siffran noll", "bilder på siffran noll", "bilder på siffran 0"),
               1: ("Number one", "pictures of number 1", "pictures of number one", "number 1", "siffran 1", "siffran ett", "bilder på siffran ett", "bilder på siffran 1"),
               2: ("Number two", "pictures of number 2", "pictures of number two", "number 2", "siffran 2", "siffran två", "bilder på siffran två", "bilder på siffran 2"),
               3: ("Number three", "pictures of number 3", "pictures of number three", "number 3", "siffran 3", "siffran tre", "bilder på siffran tre", "bilder på siffran 3"),
               4: ("Number four", "pictures of number 4", "pictures of number four", "number 4", "siffran 4", "siffran fyra", "bilder på siffran fyra", "bilder på siffran 4"),
               5: ("Number five", "pictures of number 5", "pictures of number five", "number 5", "siffran 5", "siffran fem", "bilder på siffran fem", "bilder på siffran 5"),
               6: ("Number six", "pictures of number 6", "pictures of number six", "number 6", "siffran 6", "siffran sex", "bilder på siffran sex", "bilder på siffran 6"),
               7: ("Number seven", "pictures of number 7", "pictures of number seven", "number 7", "siffran 7", "siffran sju", "bilder på siffran sju", "bilder på siffran 7"),
               8: ("Number eight", "pictures of number 8", "pictures of number eight", "number 8", "siffran 8", "siffran åtta", "bilder på siffran åtta", "bilder på siffran 8"),
               9: ("Number nine", "pictures of number 9", "pictures of number nine", "number 9", "siffran 9", "siffran nio", "bilder på siffran nio", "bilder på siffran 9")}
    website_url = 'https://www.google.com/imghp'
    if st.button('click here to start scraper'):
        driver = get_driver(website_url)
        search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search_box.click()
        for search_term in numbers[sel_number]:
            search_box.send_keys(search_term)
            search_box.send_keys(Keys.ENTER)
            img_downloader(number_of_images, sel_number, search_term, driver)

