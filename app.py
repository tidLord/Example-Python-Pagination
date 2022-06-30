#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3, math

count_per_page = 5 #จำนวนต่อหน้าที่ต้องการ
page_number = 1 #เลขหน้าที่ต้องการ
order_style = 'desc' #รูปแบบการเรียง asc=น้อยไปหามาก, desc=มากไปหาน้อย

limit = count_per_page #limit คือ จำนวนต่อหน้าที่ต้องการ
offset = (count_per_page*page_number)-count_per_page
#สูตร offset คือ (จำนวนต่อหน้าที่ต้องการ*เลขหน้าที่ต้องการ)-จำนวนต่อหน้าที่ต้องการ

#database
dbcon = sqlite3.connect('test.db')
dbcursor = dbcon.cursor()
dbcursor.execute("create table if not exists test_table(id integer primary key, title text)")

#หาจำนวนหน้าทั้งหมด
dbcursor.execute("select * from test_table")
db_res_all = dbcursor.fetchall()
total_data = len(db_res_all) #นับจำนวนข้อมูลทั้งหมดใน database
page_total = math.ceil(total_data/count_per_page) # จำนวนข้อมูลทั้งหมดในฐานข้อมูล/จำนวนต่อหน้าที่ต้องการ ใช้ math.ceil หารปัดเศษขึ้น

#เลือกและเรียงลำดับข้อมูลมาเพื่อแสดง ณ ที่นี้คือ order by id เซ็ตรูปแบบการเรียงลำดับ, limit, offset
dbcursor.execute("select * from test_table order by id "+order_style+" limit ? offset ?",(limit,offset))
db_res = dbcursor.fetchall()
dbcon.close()

#แสดงผล
print('Page '+str(page_number)+' from '+str(page_total))
for x in db_res:
    print(str(x[0])+'___'+x[1])