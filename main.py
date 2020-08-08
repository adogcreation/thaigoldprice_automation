import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

homepage = 'https://www.goldtraders.or.th/'
web_req = requests.get(homepage) #นำ url ที่ 1 เข้ามา เป็นหน้า level A
web_page = web_req.text #ใช้ class text ดึงข้อมูลข้างในมาโชว์
soup = BeautifulSoup(web_page, "html.parser") #อันนี้ไปดึงข้อมูลมาจาก url ด้านบนสุดที่ใช้กับ request
#recheck all div tags รีเช็คว่า tag div ออกมาหน้าตาเป็นอย่างไร
#soup.find_all('div')
#price = soup.find_all("div",{"class":"main-panel"})

def gold_one():
  gold_list = []
  for i in soup.find_all("span",{"id":"DetailPlace_uc_goldprices1_lblBLSell"}):
    gold_list.append(i.text)

    return gold_list

price_goldbar_sells = gold_one()
listToStr_one = ' '.join(map(str, price_goldbar_sells))
price_goldbar_sell = listToStr_one

def gold_two():
  gold_list = []
  for i in soup.find_all("span",{"id":"DetailPlace_uc_goldprices1_lblBLBuy"}):
    gold_list.append(i.text)

    return gold_list

price_goldbar_buys = gold_two()
listToStr_two = ' '.join(map(str, price_goldbar_buys))
price_goldbar_buy = listToStr_two

def gold_three():
  gold_list = []
  for i in soup.find_all("span",{"id":"DetailPlace_uc_goldprices1_lblOMSell"}):
    gold_list.append(i.text)

    return gold_list

price_goldjewelry_sells = gold_three()
listToStr_three = ' '.join(map(str, price_goldjewelry_sells))
price_goldjewelry_sell = listToStr_three

def gold_four():
  gold_list = []
  for i in soup.find_all("span",{"id":"DetailPlace_uc_goldprices1_lblOMBuy"}):
    gold_list.append(i.text)

    return gold_list

price_goldjewelry_buys = gold_four()
listToStr_four = ' '.join(map(str, price_goldjewelry_buys))
price_goldjewelry_buy = listToStr_four

def date_time():
  gold_list = []
  for i in soup.find_all("span",{"id":"DetailPlace_uc_goldprices1_lblAsTime"}):
    gold_list.append(i.text)

    return gold_list

date_times = date_time()
listToStr_five = ' '.join(map(str, date_times))
date = listToStr_five

print('ราคาทองตามประกาศของสมาคมค้าทองคำ ประจำวันที่',date,'\n'
,'ทองคำแท่ง 96.5%','ขายออก',price_goldbar_sell,'บาท','รับซื้อ',price_goldbar_buy,'บาท','\n'
,'ทองรูปพรรณ 96.5%','ขายออก',price_goldjewelry_sell,'บาท','รับซื้อ',price_goldjewelry_buy,'บาท')