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


def img_downloader(number_of_images, sel_number, driver):
    for image in range(1, number_of_images+1):
        image_url = driver.find_element(By.XPATH, f'//*[@id="islrg"]/div[1]/div[{image}]/a[1]/div[1]/img').get_attribute('src')
        if not os.path.exists(os.getcwd() + f"/images/{sel_number}"):
            os.makedirs(os.getcwd() + f"/images/{sel_number}" )
            urllib.request.urlretrieve(image_url, os.getcwd() + f"/images/{sel_number}/" + f"{image}.png")
        else:
            urllib.request.urlretrieve(image_url, os.getcwd() + f"/images/{sel_number}/" + f"{image}.png")


def get_driver(website_url):
    options = Options()
    options.add_extension(os.getcwd() + "/scraper" + "\cookieblocker.crx")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.implicitly_wait(40)
    driver.get(website_url)
    return driver


def number_image_scraper():
    sel_number = st.sidebar.selectbox('Select number to scrape', (0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    number_of_images = st.sidebar.slider('select how many images to download', 0, 24, 1)
    numbers = {0: "Number zero", 1: "Number one", 2: "Number two", 3: "Number three", 4: "Number four", 5: "Number 5", 6: "Number six", 7: "Number seven", 8: "Number eight", 9: "Number nine"}
    website_url = 'https://www.google.com/imghp'
    if st.button('click here to start scraper'):
        driver = get_driver(website_url)
        search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search_box.click()
        search_box.send_keys(numbers[sel_number])
        search_box.send_keys(Keys.ENTER)
        img_downloader(number_of_images, sel_number, driver)

