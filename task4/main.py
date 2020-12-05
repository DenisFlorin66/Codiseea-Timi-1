#Selenium imports here
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import time
import re
from urllib.request import urlopen
# from urllib.request import urlopen    
import json
from pandas.io.json import json_normalize
import pandas as pd, numpy as np
import bs4, requests


#Other imports here
import os
import wget

driver=webdriver.Chrome('C:/Users/Professional/Downloads/chromedriver_win32/chromedriver.exe')

# Fisiere txt
instagram = open('./instagram.txt', 'r') 

#Variables
URL='https://www.instagram.com/'
URL_BEST = 'https://www.instagram.com/best_chisinau/'
POST_URL_PATTERN='https://www.instagram.com/best_chisinau/p/<post-slug-id>'
post_xpath_str = "//a[contains(@href, '/p/')]"
post_links = driver.find_elements_by_xpath(post_xpath_str)
post_link_el = None

driver.get(URL)

#target username
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

#enter username and password
username.clear()
username.send_keys("massveritas")
password.clear()
password.send_keys("#123456")

#target the login button and click it
button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()


#nadle NOT NOW
not_now = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()
# not_now2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Not Now")]'))).click()

driver.implicitly_wait(10)

driver.get(URL_BEST)

# scroll to the bottom of the page
lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount==lenOfPage:
        match=True

# find all links on the page and if they match '/p' append to list named posts
posts = []
links = driver.find_elements_by_tag_name('a')
for link in links:
    post = link.get_attribute('href')
    if '/p/' in post:
      posts.append( post )

for post in posts:
    driver.get( post )
    page = requests.get(post)
    soup = BeautifulSoup(page.text, "lxml")
    print(soup.find_all('span'))

instagram = open('./instagram.txt', 'r') 


# Citire line by line
# 
Lines = instagram.readlines()

#Variabile
instagram_array=[]
roman_numbers=[]
keys=[]

#Parsing txts
for line in Lines: 
    new_line = line.strip().split(':')
    instagram_array.append(new_line)

class Solution(object):
   def romanToInt(self, s):
      """
      :type s: str
      :rtype: int
      """
      roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
      i = 0
      num = 0
      while i < len(s):
         if i+1<len(s) and s[i:i+2] in roman:
            num+=roman[s[i:i+2]]
            i+=2
         else:
            #print(i)
            num+=roman[s[i]]
            i+=1
      return num
ob1 = Solution()

for x in instagram_array:
    print(ob1.romanToInt(x[0]))
    roman_numbers.append([ob1.romanToInt(x[0]), x[1]])




# print(sorted(roman_numbers, key=lambda x: x[0], reverse=False))

sortedArray = sorted(roman_numbers, key=lambda x: x[0], reverse=False)

concatArray = []
for i in sortedArray:
    concatArray.append(i[1].strip())



print(''.join(concatArray))



