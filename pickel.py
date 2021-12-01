import requests
from bs4 import BeautifulSoup
import json

pickel_url="https://paytmmall.com/shop/search?q=pickles&from=organic&child_site_id=6&site_id=2&category=101471"
response=requests.get(pickel_url)
url_content=response.content
soup=BeautifulSoup(url_content,"html.parser")
table_tag=soup.find("div",class_="_3RA-")
pickel_list=[]
# print(table_tag)
for i in table_tag:
    pickel_name=i.find_all("div",class_="UGUy")
    for j in pickel_name:
        name=j.get_text()
        # print(name)
    # pickel_price=i.find_all("div",class_="_2MEo")
    # for j in pickel_price:
    #     price=j.get_text()
    #     # print(price)
    pickel_discount_price=i.find_all("span",class_="")
    for j in pickel_discount_price:
        discount_price=j.get_text()
        # print(discount_price)
    # pickel_image=i.find_all(class_="https://assetscdn1.paytm.com/images/catalog/produc…F69C/1626410079288_0..jpg?imwidth=282&impolicy=hq")
    # for j in pickel_image:
    #     image=j.get_text()
    #     print(image)
    image_url=i.find_all("img",class_="")
    k=1
    while k <len(table_tag):
        for j in image_url:
            link=j["src"]
            image_link="https://assetscdn1.paytm.com"+link
            print(image_link)
            dict={"serial_no":"","name":"","image_url":"","price":""}
            dict["sirial_no"]=k
            dict["name"]=name
            dict["image_url"]=image_link
            dict["price"]=discount_price
            pickel_list.append(dict)
with open("pickel.json","w") as file:
    json.dump(pickel_list,file,indent=4)
   