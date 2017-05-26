from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect('scrape.db')
curs = conn.cursor()

curs.execute(''' CREATE TABLE CATEGORY(ID INTEGER PRIMARY KEY,NAME TEXT)''')
curs.execute(''' CREATE TABLE BOOKS(CAT_ID INTEGER, NAME TEXT,PRICE INTEGER,AVAILABILITY TEXT,RATING TEXT)''')
html_content = requests.get('http://books.toscrape.com')
soup = BeautifulSoup(html_content.content)

categories = soup.find('div',class_='side_categories')
cat_list = categories.findAll('a')
count = 1
for i in range (len(cat_list)):
    print cat_list[i].text.strip()
    text1 = cat_list[i].text.strip()
    curs.execute("INSERT INTO CATEGORY(ID,NAME) VALUES(?,?)",(count,text1))
    count +=1

for x in range(len(cat_list)):
    html_content=requests.get('http://books.toscrape.com/' + cat_list[x].get('href'))
    soup = BeautifulSoup(html_content.content)
    book_list = soup.findAll('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for y in range(len(book_list)):
        book_name = book_list[y].find('h3').text.strip()
        book_price = book_list[y].find('p',class_='price_color').text.strip()
        book_availability = book_list[y].find('p',class_="instock availability").text.strip()
        if (book_list[y].find('p',class_="star-rating One")):
            book_rating = 1
        elif (book_list[y].find('p',class_="star-rating Two")):
            book_rating=2
        elif (book_list[y].find('p',class_="star-rating Three")):
            book_rating=3
        elif (book_list[y].find('p',class_="star-rating Four")):
            book_rating=4
        elif(book_list[y].find('p',class_="star-rating Five")):
            book_rating=5
        #print book_name,book_price,book_availability,book_rating
        curs.execute("INSERT INTO BOOKS VALUES(?,?,?,?,?)",(x,book_name,book_price,book_availability,book_rating))
conn.commit()
conn.close()
