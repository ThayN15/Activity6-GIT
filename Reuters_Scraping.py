# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 00:06:28 2020

@author: Nadun
"""

#Import Libraries
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException

#-------------------------------------------------------------------------------------------

#Getting the driver
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.reuters.com/search/news?blob=Python+Language&sortBy=date&dateRange=all")
driver.implicitly_wait(25)

#Passing driver for bs   
soup = BeautifulSoup(driver.page_source, 'html')        

#Dates
date =[]     
dateList = soup.findAll('h5',{'class':'search-result-timestamp'})
for name in dateList:
    dl=(name.get_text())
    date.append(dl)
dat = (date)

