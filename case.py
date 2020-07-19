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
stuff=list()
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
    info_div = bs.find("div",class_="site-stats-count").find_all("li")
    all_details = ""
    for block in info_div:
        try:
            count = block.find("strong").get_text()
            stuff.append(count)
            text = block.find("span").get_text()
            all_details = all_details + text +" : " + count + "\n"
        except:
            break
    active=stuff[0]
    cured=stuff[1]
    deaths=stuff[2]
    migrated=stuff[3]
    # print(format_date, active, cured, deaths, migrated)

    database.cur.execute('SELECT active FROM tracker WHERE cured= ?',(cured, ) )
    row=database.cur.fetchone()
    if row is None:
        database.cur.execute('''INSERT OR IGNORE INTO tracker (date, active,cured,deaths,migrated)
            VALUES ( ?, ?, ?, ?, ? )''', ( format_date, active, cured, deaths, migrated, ) )
        database.conn.commit()
    else:
        yo=row[0]
        if(yo!=int(active)):
            database.cur.execute('''INSERT OR IGNORE INTO tracker (date, active,cured,deaths,migrated)
                VALUES ( ?, ?, ?, ?, ? )''', ( format_date, active, cured, deaths, migrated, ) )
            database.conn.commit()

    return all_details

# FUNCTION TO PRODUCE NOTIFICATION
def get_corona_detail_of_india_noti():
    url= "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)

    bs = bs4.BeautifulSoup(html_data.text, 'html.parser') # MAKING OF OBJECT
    info_div = bs.find("div",class_="site-stats-count").find_all("li")
    all_details = ""
    for block in info_div:
        try:
            count = block.find("strong").get_text()
            text = block.find("span").get_text()
            all_details = all_details + text +" : " + count + "\n"
        except:
            break
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
