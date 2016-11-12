from bs4 import BeautifulSoup

data_list = []
with open("./1_2_homework_required/index.html", "r") as file:
    soup = BeautifulSoup(file, "lxml")
    img_list = soup.select("body > div > div > div.col-md-9 > div > div > div > img")
    name_list = soup.select(
        "body > div > div > div.col-md-9 > div > div > div > div.caption > h4 > a")
    money_list = soup.select(
        "body > div > div > div.col-md-9 > div > div > div > div.caption > h4.pull-right")
    des_list = soup.select(
        "body > div > div > div.col-md-9 > div > div > div > div.caption > p")
    star_list = soup.select(
        "body > div > div > div.col-md-9 > div > div > div > div.ratings > p:nth-of-type(2)")
    review_list = soup.select(
        "body > div > div > div.col-md-9 > div > div > div > div.ratings > p.pull-right")
    # print(img_list, name_list, money_list, des_list,star_list, review_list, sep="\n--------------\n")


for img,name,money,des,star,review in zip(img_list,name_list,money_list,des_list,star_list,review_list):
    data = {
        "img" : img.get("src"),
        "name" : name.get_text(),
        "money" : money.get_text(),
        "des" : des.get_text(),
        "star" : len(star.find_all("span", class_='glyphicon glyphicon-star')),
        "review" : review.get_text()
    }
    data_list.append(data)

print(data_list)

"""
img:
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > img
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > img
name:
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4:nth-child(2) > a
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.caption > h4:nth-child(2) > a
money:
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > h4.pull-right
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.caption > h4.pull-right
des:
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.caption > p
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.caption > p
star:
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p:nth-child(2)
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.ratings > p:nth-child(2)
review:
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(1) > div > div.ratings > p.pull-right
body > div:nth-child(2) > div > div.col-md-9 > div:nth-child(2) > div:nth-child(2) > div > div.ratings > p.pull-right
"""
