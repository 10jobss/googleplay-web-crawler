# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:50:53 2017

@author: kyunghoon
"""
import requests, time, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def get_info(start_url):
    driver = webdriver.Chrome('C:/Users/kyunghoon/Downloads/chromedriver_win32/chromedriver')
    driver.implicitly_wait(15)
    driver.get(start_url)
    
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    elm = driver.find_element_by_tag_name('html')
    i = 1
    for i in range(1, 6):
        elm.send_keys(Keys.END)
        time.sleep(5)
    time.sleep(10)
    main_content = soup.find('div', class_='body-content') # problem 뒤로 back하면 다시 reload 됨
    apps = main_content.find_all('div', class_='card-content id-track-click id-track-impression')
    cnt = 1    
    for app in apps:
        code = app.find('a', class_='card-click-target').get('href')
        target_url = base_url + code
        driver.get(target_url)
        driver.implicitly_wait(15)
        
        print(code)
        
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")  
        main_content = soup.find('div', class_='main-content')
    
        name = main_content.find('h1', class_='document-title').find('div', class_='id-app-title').get_text()
        dev = main_content.find('div', class_='left-info').find('span', itemprop="name").get_text()
        genre = main_content.find('div', class_='left-info').find('span', itemprop="genre").get_text()
        rating_score = main_content.find('div', class_='score').get_text()
        rating_count = main_content.find('div', class_='right-info').find('span', class_='rating-count').get_text()
        print(name + " ** " + dev + " ** " + genre + " ** " + rating_score + " ** " + rating_count)
        content_dis = main_content.find('div', class_='meta-info contains-text-link')
        containers = content_dis.find_all('div', {'class' : 'content'})
        age_limit = containers[0].get_text()
        try:
            attribute = containers[1].get_text() 
        except:
            attribute = "NA"
            pass
        print(age_limit + " *** " + attribute)
        meta_infos = main_content.find_all('div', {'class' : 'meta-info'})
        for meta_info in meta_infos:
            tmp = meta_info
            if tmp.find('div', class_='title').get_text() == "설치 수":
                downloads = tmp.find('div', itemprop="numDownloads").get_text()
            elif tmp.find('div', class_='title').get_text() == "지원되는 Android 버전":
                support_version = tmp.find('div', itemprop="operatingSystems").get_text()
        print(downloads + " *** " + support_version)
        print(str(cnt) + " Success!")
        cnt += 1
        driver.execute_script("window.history.go(-1)")
    #f.close()
    
#url = 'https://play.google.com/store/apps/details?id=com.efunkr.ql.google'
start_url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_free'
base_url = 'https://play.google.com'
#f = open('app_info22.txt', 'w')
get_info(start_url)

'''
f.write(name + '\t')
f.write(dev+ '\t')
f.write(genre + '\t')
f.write(rating_score + '\t')
f.write(rating_count + '\t')
f.write(age_limit + '\t')
f.write(attribute + '\t')
f.write(downloads)
f.write(support_version)
'''