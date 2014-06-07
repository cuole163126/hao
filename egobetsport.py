#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import string
import re
import sys

def egobetsport():
    browser.get('http://www.egobet88.com/en/sport-early-bets.html')
    browser.maximize_window()
    time.sleep(10)
    browser.find_element_by_id("league").click()
    time.sleep(10)
    browser.find_element_by_id("ca").click()
    time.sleep(10)
    browser.find_element_by_id("tj").click()
    time.sleep(10)
    browser.find_element_by_id("nolive_page").click()
    time.sleep(10)
    a1=browser.find_elements_by_xpath("//option[@value='-1']")
    ii=1
    kk=""
    for jj in a1:
        browser.find_element_by_id("nolive_page").click()
        ss="//option[contains(text(),'"+str(ii)+"')]"
        ii=ii+1
        browser.find_element_by_xpath(ss).click()
        time.sleep(6)
        a2=browser.find_element_by_xpath("//td[@style='padding-left:3px; width:544px;']")
        kk=a2.get_attribute("outerHTML")+kk
        time.sleep(6)
    file1=open('egobetsport.html','w')
    file1.write(kk)
    file1.close()
    #os.popen('cp egobetsport1.html egobetsport.html')
    time.sleep(10)

reload(sys)
sys.setdefaultencoding('utf-8')
browser = webdriver.Firefox()
while 1:
    egobetsport()
