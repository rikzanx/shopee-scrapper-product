from tempfile import NamedTemporaryFile
import shutil
import csv
import requests
import csv
import time
import random
from os import path
import os
from requests.api import get
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'cookie': '_gcl_au=1.1.961206468.1594951946; _med=refer; _fbp=fb.2.1594951949275.1940955365; SPC_IA=-1; SPC_F=y1evilme0ImdfEmNWEc08bul3d8toc33; REC_T_ID=fab983c8-c7d2-11ea-a977-ccbbfe23657a; SPC_SI=uv1y64sfvhx3w6dir503ixw89ve2ixt4; _gid=GA1.3.413262278.1594951963; SPC_U=286107140; SPC_EC=GwoQmu7TiknULYXKODlEi5vEgjawyqNcpIWQjoxjQEW2yJ3H/jsB1Pw9iCgGRGYFfAkT/Ej00ruDcf7DHjg4eNGWbCG+0uXcKb7bqLDcn+A2hEl1XMtj1FCCIES7k17xoVdYW1tGg0qaXnSz0/Uf3iaEIIk7Q9rqsnT+COWVg8Y=; csrftoken=5MdKKnZH5boQXpaAza1kOVLRFBjx1eij; welcomePkgShown=true; _ga=GA1.1.1693450966.1594951955; _dc_gtm_UA-61904553-8=1; REC_MD_30_2002454304=1595153616; _ga_SW6D8G0HXK=GS1.1.1595152099.14.1.1595153019.0; REC_MD_41_1000044=1595153318_0_50_0_49; SPC_R_T_ID="Am9bCo3cc3Jno2mV5RDkLJIVsbIWEDTC6ezJknXdVVRfxlQRoGDcya57fIQsioFKZWhP8/9PAGhldR0L/efzcrKONe62GAzvsztkZHfAl0I="; SPC_T_IV="IETR5YkWloW3OcKf80c6RQ=="; SPC_R_T_IV="IETR5YkWloW3OcKf80c6RQ=="; SPC_T_ID="Am9bCo3cc3Jno2mV5RDkLJIVsbIWEDTC6ezJknXdVVRfxlQRoGDcya57fIQsioFKZWhP8/9PAGhldR0L/efzcrKONe62GAzvsztkZHfAl0I="'
    }
driver = webdriver.Firefox(executable_path='d:/geckodriver/geckodriver.exe')

filename = 'larisa_ismi.id.csv'
tempfile = NamedTemporaryFile(mode='w', delete=False,newline="")

fields = ['shopid','itemid','catid','modelid','name','variation','price','stock','description','images']
header = ['shopid','itemid','catid','modelid','name','variation name 0','variation 0','variation name 1','variation 1','price','stock','description','images']
judul = "fix "+filename

with open(filename, 'r') as csvfile, tempfile:
    reader = csv.DictReader(csvfile, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=header)
    rowData = {'shopid': 'shopid','itemid' : 'itemid','catid' : 'catid','modelid' : 'modelid','name' : 'name','variation name 0': 'variation name 0','variation 0':'variation 0','variation name 1':'variation name 1','variation 1':'variation 1','price':'price','stock':'stock','description':'description','images': 'images'}
    writer.writeheader()
    for row in reader:
        if(row['shopid'] == "shopid"):
            continue
        rowData = {
            'shopid': row['shopid'],
            'itemid' : row['itemid'],
            'catid' : row['catid'],
            'modelid' : row['modelid'],
            'name' : row['name'],
            'variation name 0': '',
            'variation 0':'',
            'variation name 1':'',
            'variation 1':'',
            'price':'',
            'stock':row['stock'],
            'description':row['description'],
            'images': row['images']
        }
        shopee_url = ("https://shopee.co.id/(BISA-COD)-HIJAB-JILBAB-KERUDUNG-PASHMINA-PLISKET-CERUTY-PLEATED-SHAWL-BABY-DOLL-TERLARIS-i.{}.{}").format(row['shopid'],row['itemid'])
        driver.get(shopee_url)
        driver.implicitly_wait(15)
        harga = driver.find_element_by_css_selector("._3e_UQT")
        if(row['variation'] == ""):
            my_list = []
        else:
            my_list = row['variation'].split(",")
        if(len(my_list)>=1):
            parent_div = driver.find_elements_by_css_selector(".flex._3AHLrn._2XdAdB > .flex.flex-column > .flex.items-center")
            index = 0
            for i in range(0,len(my_list)):
                elementList = parent_div[index].find_elements_by_css_selector("button.product-variation")
                variasi = parent_div[index].find_element_by_css_selector("._2IW_UG")
                variasi = variasi.text
                for elemen in elementList:
                    if my_list[index] in elemen.text:
                        elemen.click()
                        var_name = "variation name "+str(index)
                        var = "variation "+str(index)
                        rowData[var_name] = variasi
                        rowData[var] = elemen.text
                index+=1
        price = harga.text
        price = price.replace("Rp","")
        price = price.replace(".","")
        rowData['price'] = price
        writer.writerow(rowData)
shutil.move(tempfile.name, judul)