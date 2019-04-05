import time
import os

import pymysql

# os.system("export PATH=$PATH:~/.lcoal/bin")
# while True:
#     os.system("~/.local/bin/scrapy crawl itcast -o teachers.json")
#     time.sleep(100)

conn = pymysql.connect(host='47.102.112.221', port=3306, user='chenchao', passwd='123456',db='bigdata')
cur = conn.cursor()
cur.execute("insert into items(id,itemname,oid) values(18,'aaa',1)")
cur.execute("select * from items")
for r in cur.fetchall():
    print(r)
cur.close()
conn.close()