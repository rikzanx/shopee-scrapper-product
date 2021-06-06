import pandas as pd
import numpy as np
import re
from bs4 import BeautifulSoup as bs

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
import datetime
from os import path
import os
from progress.bar import Bar


driver = webdriver.Firefox(executable_path='d:/geckodriver/geckodriver.exe')
data = pd.DataFrame(columns=['link', 'penilaian', 'price', "spek", "seller_name", "seller_rate"])
link = []
keyword = input("Masukkan keyword 2 kata : ")
#loop the page
for page in range(4):
    #the main link strcuture based on keyword and the product filter
    main_link = f"https://shopee.co.id/search?keyword={keyword}&locations=Kota%2520Surabaya&noCorrection=true&page={page}&ratingFilter=4"
    
    driver.get(main_link)
    for i in range(10):
        sc = np.random.rand()
        driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight*{sc});")
    
    new_link = driver.find_elements_by_xpath('//a[@data-sqe="link"]')
    
    #extract the link and appending to 'link' list 
    for links in new_link:
        p_link = links.get_attribute('href')
        link.append(p_link)
# make empty dataframe 
data = pd.DataFrame(columns=['link', 'penilaian', 'price', "spek", "seller_name", "seller_rate"])
print("link found :" + str(len(link)))
total = len(link)
index = 1
bar = Bar('Processing', max=total)
for links in link:
    persen = index/total * 100
    persen = ("{}%").format(persen)
    index+=1
    driver.get(links)
    driver.implicitly_wait(2)
    
    #scroll down the page to make sure it contains the information we need
    driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight*0.7);")
    driver.implicitly_wait(2)
    
    # gathering the html data (our raw data)
    html = driver.page_source
    soup = bs(html, "lxml")
    seller = soup.find("div", class_ = "_34c6X6 page-product__shop")
    while seller == None:
        driver.implicitly_wait(1)
        html = driver.page_source
        soup = bs(html, "lxml")
        seller = soup.find("div", class_ = "_34c6X6 page-product__shop")
    penilaian = []
    #find the review infomation
    nilai = soup.find(class_ = "flex _21hHOx")
    
    ra = nilai.findAll(class_ = re.compile('OitLRu'))
    if(len(ra)<1):
        bar.next()
        continue
    penilaian.append(ra[0].text)
    penilaian.append(ra[1].text)
    penilaian.append(nilai.find(class_ = "aca9MM").text)
    
    #find the price of product
    price = soup.find(class_ = "_3e_UQT").text
    
    #find the product spesification
    spek = soup.find_all(class_ = "aPKXeO")
    spesifikasi = []
    for s in spek:
        try:
            val = s.text
        except:
            val = np.nan           
        spesifikasi.append(val)
    kondisi = False
    for spek in spesifikasi:
        if("SURABAYA" in spek):
            kondisi = True
    if(kondisi == False):
        bar.next()
        continue
    #extract the seller information
    seller = soup.find("div", class_ = "_34c6X6 page-product__shop")
    seller_rate = []
    try:
        name = seller.find(class_ = "_3uf2ae").text
        
        seller_ratess = seller.findAll(class_ = re.compile('zw2E3N'))
        for ra in seller_ratess:
            seller_rate.append(ra.text)
    except:
        name = np.nan
        seller_rate.append(np.nan)

    #append them to our empty dataframe
    data = data.append({'link':links, 'penilaian':penilaian, 'price':price, 'spek':spesifikasi,
                        "seller_name":name, "seller_rate":seller_rate}, ignore_index=True)
    bar.next()
bar.finish()
print ("Number of available supplier equal to:" , data["seller_name"].nunique())

# cleansing the datasets

# product information
data["star_rating"] = data["penilaian"].str[0]
data["cunt_rating"] = data["penilaian"].str[1]
data["sales"] = data["penilaian"].str[2]

data["category"] = data["spek"].str[0]
data["Merk"] = data["spek"].str[1]
data["Stock"] = data["spek"].str[2]

# supplier information
data["Supplier_Place"] = data["spek"].str[3]
data["total_penilaian"] = data["seller_rate"].str[0]
data["total_product"] = data["seller_rate"].str[1]
data["percentage_reply_m"] = data["seller_rate"].str[2]
data["reply_time_parameter"] = data["seller_rate"].str[3]
data["registered_date"] = data["seller_rate"].str[4]
data["follower"] = data["seller_rate"].str[5]

x = datetime.datetime.now()
waktu =x.strftime("%Y-%m-%d %H-%M-%S")
name = ("{} - {}.csv").format(keyword, waktu)
print(name)
data.to_csv(name, index=False)

data.drop(columns=["penilaian", "seller_rate", "spek"]).sample(10)
print(data)

driver.close()
