# ALL THE IMPORTS

import requests
import bs4

# IMPORT FOR DISPLAYING NOTIFICATION
import plyer

# IMPORT FOR DISPLAYING DATE AND TIME
import time
import datetime as dt

#IMPORT FOR DATABASE CONNECTION
import sqlite3
import database

# MAKING THE CONNECTION TO DATABASE
try:
    database.cur.execute('CREATE TABLE tracker(date TEXT, active INTEGER, cured INTEGER, deaths INTEGER, migrated INTEGER)')
except:
    database.cur.execute('SELECT * FROM tracker')


# GLOBAL VARIABLES
date = dt.datetime.now()
format_date = f"{date:%a, %b %d %Y}"

# FUNCTION TO GET URL
def get_html_data(url):
    data = requests.get(url)
    return data

# FUNCTION TO GET THE CORONA DETAILS
def get_corona_detail_of_india():
    url= "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser') # MAKING OF OBJECT
    info_div1 = bs.find("li",class_="bg-blue").find_all('strong', class_="mob-hide")
    active=info_div1[0].get_text()
    active_no=info_div1[1].get_text().split()[0]
    info_div2 = bs.find("li",class_="bg-green").find_all('strong', class_="mob-hide")
    dis=info_div2[0].get_text()
    dis_no=info_div2[1].get_text().split()[0]
    info_div3 = bs.find("li",class_="bg-red").find_all('strong', class_="mob-hide")
    death=info_div3[0].get_text()
    death_no=info_div3[1].get_text().split()[0]
    mig="1"

    all_details = active+" : "+active_no+"\n"+dis+" : "+dis_no+"\n"+death+" : "+death_no+"\n"+"Migrated : "+mig

    database.cur.execute('SELECT active FROM tracker WHERE cured= ?',(dis_no, ) )
    row=database.cur.fetchone()
    if row is None:
        database.cur.execute('''INSERT OR IGNORE INTO tracker (date, active,cured,deaths,migrated)
            VALUES ( ?, ?, ?, ?, ? )''', ( format_date, active_no, dis_no, death_no, mig, ) )
        database.conn.commit()
    else:
        yo=row[0]
        if(yo!=int(active_no)):
            database.cur.execute('''INSERT OR IGNORE INTO tracker (date, active,cured,deaths,migrated)
                VALUES ( ?, ?, ?, ?, ? )''', ( format_date, active_no, dis_no, death_no, mig, ) )
            database.conn.commit()

    return all_details

# FUNCTION TO PRODUCE NOTIFICATION
def get_corona_detail_of_india_noti():
    url= "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser') # MAKING OF OBJECT
    info_div1 = bs.find("li",class_="bg-blue").find_all('strong', class_="mob-hide")
    active=info_div1[0].get_text()
    active_no=info_div1[1].get_text().split()[0]
    info_div2 = bs.find("li",class_="bg-green").find_all('strong', class_="mob-hide")
    dis=info_div2[0].get_text()
    dis_no=info_div2[1].get_text().split()[0]
    info_div3 = bs.find("li",class_="bg-red").find_all('strong', class_="mob-hide")
    death=info_div3[0].get_text()
    death_no=info_div3[1].get_text().split()[0]
    mig="1"

    all_details = active+" : "+active_no+"\n"+dis+" : "+dis_no+"\n"+death+" : "+death_no+"\n"+"Migrated : "+mig

    return all_details

# FUNCTION TO DISPLAY NOTIFICATION
def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID-19 CASES OF INDIA",
            message=get_corona_detail_of_india_noti(),
            timeout=10 # IT WILL SHOW UP FOR 10 SECONDS
        )
        time.sleep(1800) # IT WILL DISPLAY AFTER EVERY 1800 SECOND
