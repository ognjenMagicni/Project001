import pymysql
import json

jsonlFile = 'proccessedFile1.jsonl'

file = open(jsonlFile, 'r', encoding='utf-8')
lines = file.readlines()

conn = pymysql.connect(host = "localhost", user="root", password="Laptop1*", database="properties" )


title = 'Novi Sad Full'
description = "All estates in Novi Sad"
cursor = conn.cursor()
query = "INSERT INTO properties.search(price_min,price_max,square_min,Square_max,date,title,description) VALUES(%s,%s,%s,%s,CURDATE(),%s,%s)"
values = (20000, 5000000, 10, 500, title, description)
cursor.execute(query,values)
conn.commit()
id = cursor.lastrowid

for line in lines:
    d = json.loads(line)
    query = "INSERT INTO properties.property(fk_search,no_room,square,square_price,price,location,city,country,link,on_off) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (id,d['Rooms'],d['Square metres'],d['square Price'],d['Full price'],d['location'],d['city'],'Serbia',d['Link'],1)
    cursor.execute(query,values)
    conn.commit()

