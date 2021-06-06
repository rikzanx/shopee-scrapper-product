import requests
import csv
import time
import random
from os import path
import os
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By

shopId = 9011098
limit=30

def get_price(shopid,itemid,tujuan=""):
    price = ""
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
        'cookie': '_gcl_au=1.1.961206468.1594951946; _med=refer; _fbp=fb.2.1594951949275.1940955365; SPC_IA=-1; SPC_F=y1evilme0ImdfEmNWEc08bul3d8toc33; REC_T_ID=fab983c8-c7d2-11ea-a977-ccbbfe23657a; SPC_SI=uv1y64sfvhx3w6dir503ixw89ve2ixt4; _gid=GA1.3.413262278.1594951963; SPC_U=286107140; SPC_EC=GwoQmu7TiknULYXKODlEi5vEgjawyqNcpIWQjoxjQEW2yJ3H/jsB1Pw9iCgGRGYFfAkT/Ej00ruDcf7DHjg4eNGWbCG+0uXcKb7bqLDcn+A2hEl1XMtj1FCCIES7k17xoVdYW1tGg0qaXnSz0/Uf3iaEIIk7Q9rqsnT+COWVg8Y=; csrftoken=5MdKKnZH5boQXpaAza1kOVLRFBjx1eij; welcomePkgShown=true; _ga=GA1.1.1693450966.1594951955; _dc_gtm_UA-61904553-8=1; REC_MD_30_2002454304=1595153616; _ga_SW6D8G0HXK=GS1.1.1595152099.14.1.1595153019.0; REC_MD_41_1000044=1595153318_0_50_0_49; SPC_R_T_ID="Am9bCo3cc3Jno2mV5RDkLJIVsbIWEDTC6ezJknXdVVRfxlQRoGDcya57fIQsioFKZWhP8/9PAGhldR0L/efzcrKONe62GAzvsztkZHfAl0I="; SPC_T_IV="IETR5YkWloW3OcKf80c6RQ=="; SPC_R_T_IV="IETR5YkWloW3OcKf80c6RQ=="; SPC_T_ID="Am9bCo3cc3Jno2mV5RDkLJIVsbIWEDTC6ezJknXdVVRfxlQRoGDcya57fIQsioFKZWhP8/9PAGhldR0L/efzcrKONe62GAzvsztkZHfAl0I="'
    }
    driver = webdriver.Firefox(executable_path='d:/geckodriver/geckodriver.exe')
    # shopee_url = ("https://shopee.co.id/shop/{}/search?page=0&sortBy=pop").format(tokoid,page)
    shopee_url = ("https://shopee.co.id/(BISA-COD)-HIJAB-JILBAB-KERUDUNG-PASHMINA-PLISKET-CERUTY-PLEATED-SHAWL-BABY-DOLL-TERLARIS-i.{}.{}").format(shopid,itemid)
    driver.get(shopee_url)
    driver.implicitly_wait(15)
    harga = driver.find_element_by_css_selector("._3e_UQT")
    if(tujuan == ""):
        my_list = []
    else:
        my_list = tujuan.split(",")
    if(len(my_list)>=1):
        parent_div = driver.find_elements_by_css_selector(".flex.items-center._2oeDUI")

        for list in my_list:
            print(list)
        index = 0
        for list in my_list:
            print(index)
            elementList = parent_div[index].find_elements_by_css_selector("button.product-variation")
            for elemen in elementList:
                print(elemen.text)
                if my_list[index] in elemen.text:
                    elemen.click()
            index+=1
    price = harga.text
    print(price)
    price = price.replace("Rp","")
    print(price)
    price = price.replace(".","")
    print(price)
    driver.close()
    a=price
    return a
    
 
def product_detail(shopId,itemid):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0',
        "accept": "*/*",
        "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "if-none-match": "9da620d2f3dc9ecb769a367f0978222e",
        "if-none-match-": "55b03-839402e6be9977bbfe566814ff457076",
        "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-api-source": "pc",
        "x-requested-with": "XMLHttpRequest",
        "x-shopee-language": "id",
        "cookie": "_fbp=fb.2.1613324794230.1290892498; SPC_IA=-1; SPC_EC=-; SPC_F=ZEgWn6R8HpsgzaIppPyau2vpQVedTVq6; REC_T_ID=e80cd43e-703b-11eb-966c-b4969184477a; SPC_U=-; _gcl_au=1.1.1854481322.1621320509; SPC_SI=bfftocid3.HDOIPb8kiDxCUetHJdeadbC1fkHgcuJq; _gid=GA1.3.1048919544.1622524282; _med=refer; csrftoken=UpXaMMFwY3dxeEXvJdS0nFdjNt9bLZ9c; welcomePkgShown=true; AMP_TOKEN=%24NOT_FOUND; _ga=GA1.3.800883329.1613324799; SPC_R_T_ID=\"LDIJSk+mR1W+SCaYjs9bJlpYoVIXCLYyn1r4yXXtJUg7DTMzyraO2lKNiJO3Hq+JeoLEEjW3yckJtAsneO9X8CzISBa/TgTzRxItU8Vg2yU=\"; SPC_T_IV=\"qr++YMcVufwG9N8eiYaO3Q==\"; SPC_R_T_IV=\"qr++YMcVufwG9N8eiYaO3Q==\"; SPC_T_ID=\"LDIJSk+mR1W+SCaYjs9bJlpYoVIXCLYyn1r4yXXtJUg7DTMzyraO2lKNiJO3Hq+JeoLEEjW3yckJtAsneO9X8CzISBa/TgTzRxItU8Vg2yU=\"; _ga_SW6D8G0HXK=GS1.1.1622530053.7.1.1622541525.60",
        "referrer": "https://shopee.co.id/Atasan-Wanita-Lengan-78-Baju-Songket-Cewek-Pakaian-Wanita-Motif-i.219835045.7731651120",
        "referrerPolicy": "strict-origin-when-cross-origin",
        "method": "GET",
        "mode": "cors"
    }   
    url = ("https://shopee.co.id/api/v2/item/get?itemid={}&shopid={}").format(itemid,shopId)
    return requests.get(url,headers=headers).json()

def product_variations(shopId,itemId,modelid):
    url = ("https://shopee.co.id/api/v4/product/get_purchase_quantities_for_selected_model?itemId={}&modelId={}&quantity=1&shopId={}").format(itemId,modelid,shopId)
    return requests.get(url).json()
    
def getShopDetail(shopname):
    url =("https://shopee.co.id/api/v4/shop/get_shop_detail?username={}").format(shopname)
    return requests.get(url).json()

def get_products(shopId,page):
    newest = page*limit
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'referer': 'https://shopee.co.id/Atasan-Wanita-Lengan-78-Baju-Songket-Cewek-Pakaian-Wanita-Motif-i.219835045.7731651120',
        'x-shopee-language':'id',
        'x-api-source':'pc',
        'accept-encoding':'gzip, deflate, br',
        'if-not-match':'d0d0d6ce5559415e22b5133907a565a5',
        'if-none-match-': '55b03-839402e6be9977bbfe566814ff457076'
    }   
    url = ("https://shopee.co.id/api/v2/search_items/?by=sales&limit={}&match_id={}&newest={}&order=desc&page_type=shop&version=2").format(limit,shopId,newest)
    return requests.get(url,headers=headers).json()

def writeCSV(data,username):
    judul = username+".csv"
    with open(judul, "a",newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=';')
        for line in data:
            writer.writerow(line)

def download_image(imageName,itemName,counter=0):
    #name the file so we'll easily find the image
    if counter > 0:
        newFileName = itemName.replace('"',"inch").replace("/","_").replace(" ","_").replace("*","_")+"_"+str(counter)+".jpg"
    else:
        newFileName = itemName.replace('"',"inch").replace("/","_").replace(" ","_").replace("*","_")+".jpg"
    #download if file not exists
    if not path.exists("images/"+newFileName):
        response = requests.get("https://cf.shopee.co.id/file/"+imageName)
        with open("images/"+newFileName, "wb") as file:
            file.write(response.content)
    return newFileName    
    
if __name__ == "__main__":
    toko = input("Masukkan nama toko : ")
    tokoDetail = getShopDetail(toko)
    shopId = tokoDetail['data']['shopid']
    
    #Create image folder if not exists
    if not path.exists('images'):
        os.makedirs('images')
    judul = toko+".csv"
    with open(judul, "a",newline='') as csv_file:
        writer = csv.writer(csv_file)
        #write header
        header = ['shopid','itemid','catid','modelid','product name','variation name','price','stock','description','images']
        writer.writerow(header)

        #loop for how many page
        for i in range(0,1):
            ##get product per page
            products = get_products(shopId,i)
            for j, item in enumerate(products['items'],start=1):
                #delay random 2-5 seconds
                time.sleep(random.randrange(2,5))

                ##get product detail
                detail = product_detail(shopId,item['itemid'])
                # get produk category
                catid = ""
                for category in detail['item']['categories']:
                    catid = category['catid']
                
                models = detail['item']['models']
                modelsindex=0
                for model in models :
                    #get only stock > 0
                    price=0
                    if model['normal_stock'] > 0 :
                        images = []
                        if len(item['images']) > 1 :
                            for k, image in enumerate(item['images'],start=1):
                                newFileName = download_image(image,item['name'],k)
                                images.append(newFileName)
                        else:
                            newFileName = download_image(item['images'][0],item['name'])
                            images.append(newFileName)
                        images = ','.join(images)
                        rowData = [shopId,item['itemid'],catid,modelsindex,item['name'],model['name'],price,model['normal_stock'],detail['item']['description'].encode('utf8'),images]
                        writer.writerow(rowData)
                    print(item['name']+" : OK")
                    modelsindex=modelsindex+1

