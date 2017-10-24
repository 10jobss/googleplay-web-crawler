# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 11:50:53 2017

@author: kyunghoon
"""
import time, csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def get_info(input_url):
    driver.implicitly_wait(5)
    driver.get(input_url)
    driver.implicitly_wait(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    main_content = soup.find('div', class_='main-content')
    name = main_content.find('h1', class_='document-title').find('div', class_='id-app-title').get_text().strip()
    dev = main_content.find('div', class_='left-info').find('span', itemprop="name").get_text().strip()
    genre = main_content.find('div', class_='left-info').find('span', itemprop="genre").get_text().strip()
    rating_score = main_content.find('div', class_='score').get_text().strip()
    rating_count = main_content.find('div', class_='right-info').find('span', class_='rating-count').get_text().strip()
    print(name + "***" + dev + "***" + genre + "***" + rating_score + "***" + rating_count)
    content_dis = main_content.find('div', class_='meta-info contains-text-link')
    containers = content_dis.find_all('div', {'class' : 'content'})
    age_limit = containers[0].get_text().strip()
    age_limit = age_limit.split(' ')[1]
    try:
        attribute = containers[1].get_text().strip()
    except:
        attribute = "NA"
        pass
    print(age_limit + "***" + attribute)
    meta_infos = main_content.find_all('div', {'class' : 'meta-info'})
    for meta_info in meta_infos:
        tmp = meta_info
        if tmp.find('div', class_='title').get_text() == "설치 수":
            downloads = tmp.find('div', itemprop="numDownloads").get_text().strip()
        elif tmp.find('div', class_='title').get_text() == "지원되는 Android 버전":
            support_version = tmp.find('div', itemprop="operatingSystems").get_text().strip()
            support_version = support_version.strip().split(' ')[0]
    print(downloads + "***" + support_version)
    print(" Success!")
        
    tmp_dict = {'name' : name, 'dev' : dev, 'genre' : genre, 'rating_score' : rating_score,
                'rating_count' : rating_count, 'age_limit' : age_limit, 'attribute' : attribute,
                'downloads' : downloads, 'support_version' : support_version}
    data_sets.append(tmp_dict)

    time.sleep(5)
    
start_url = 'https://play.google.com/store/apps/category/GAME/collection/topselling_free'
#url1 = 'https://play.google.com/store/apps/details?id=ru.brothersappsandgames.prizemachinespinnersimulator'
#url2 = 'https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo'
url3 = 'https://play.google.com/store/apps/details?id=com.mycraft.mine.craft'
#url4 = 'https://play.google.com/store/apps/details?id=at.ner.lepsWorld2'
url5 = 'https://play.google.com/store/apps/details?id=com.netease.dhhzlggkr'
data_sets = []
driver = webdriver.Chrome('C:/Users/kyunghoon/Downloads/chromedriver_win32/chromedriver')
#get_info(url1)
#get_info(url2)
get_info(url3)
get_info(url5)

data_keys = data_sets[0].keys()

with open('test_6.csv', 'w', errors='ignore') as csvfile:
    writer = csv.DictWriter(csvfile, delimiter=',',lineterminator='\n', fieldnames = data_keys)
    writer.writeheader()
    writer.writerows(data_sets)