#!/usr/bin/env python
# encoding=utf8 
import sys
import MySQLdb
import urllib2


reload(sys)
sys.setdefaultencoding('utf8')
      

def get_table(html):

    # Reading line by line.  Create a string of html without new lines.

    all_lines = ''

    for line in iter(html):
        all_lines = all_lines+line.rstrip()

    pos = all_lines.find("d-sole")
    table = all_lines[pos:]
    
    pos = table.find('<table')
    table = table[pos:]
    
    pos = table.find('</table>')
    table = table[0:pos+8]

    return table


# Create a row to process at a time

def get_rows(table):

    pos_1 = 1  # Position of the <tr>
    pos_2 = 1  # Position of the </tr>
    count = 0
    
    while pos_1 >= 0:
        count = count + 1
        
        pos_1 = table.find('<tr')

        if pos_1 >= 0:
            table = table[pos_1:]

            pos_2 = table.find('/tr>')
            row = table[0:pos_2+4]

            # Take out the header of the table
            if count != 1:
                get_fields(row)
            
            table = table[pos_2+4:]


# Process a row and query the all fields            

def get_fields(row):

    DEBUG = 0
    
    # new
    rec = row
    pos = rec.find('/td>')
    nxt = rec[pos+4:]
    rec = rec[0:pos+4]
    pos = rec.find('<td')
    new = rec[pos:]


    
    if DEBUG: print new

    # ren
    
    ren = nxt
    pos = ren.find('/td>')
    nxt = ren[pos+4:]
    ren = ren[0:pos+4]
    pos = ren.find('<td')
    ren = ren[pos:]

    pos = ren.find('<div>')
    ren = ren[pos+5:]
    pos = ren.find('</div>')
    ren = ren[0:pos]
        
    if DEBUG: print ren

    # id

    rec = nxt
    pos = rec.find('/td>')
    nxt = rec[pos+4:]
    rec = rec[0:pos+4]
    pos = rec.find('<td')
    rec = rec[pos:]

    if DEBUG: print rec
    
    pos = rec.find('</a>')
    rec = rec[0:pos+4]
    pos = rec.find('<a')
    id  = rec[pos:]
    
    if DEBUG: print id

    # url

    url = id
    pos = url.find('href=\"')
    url = url[pos+8:]
    pos = url.find('target')
    url = url[0:pos-1]
    url = url.replace('amp;','')
    url = "https://www.hellowork.go.jp/servicef/"+url
    
    if DEBUG: print url

    # uuid

    uuid = id
    pos  = uuid.find('_blank\">')
    uuid = uuid[pos+8:]
    pos  = uuid.find("</a>")
    uuid = uuid[0:pos]
    uuid = uuid.rstrip()
    uuid = uuid.lstrip()
    
    if DEBUG: print uuid


    connector = MySQLdb.connect(host="localhost",
                                db="hellowork",
                                user="root",
                                passwd="mysql",
                                charset="utf8")

    cursor = connector.cursor()

    sql = "SELECT num FROM jobsearch WHERE uuid='"+uuid+"'"

    cursor.execute(sql)
    
    if (cursor.rowcount < 1):
        
	sys.stdout.write('.')
	sys.stdout.flush()

        # title

        rec = nxt
        pos = rec.find('/td>')
        nxt = rec[pos+4:]
        rec = rec[0:pos+4]
        pos = rec.find('<td')
        rec = rec[pos:]

        pos = rec.find("Break\">")
        rec = rec[pos+7:]
        pos = rec.find("</div>")
        title = rec[0:pos]
        title = title.rstrip()

        if DEBUG: print title
    
        rec = nxt
        pos = rec.find('/td>')
        nxt = rec[pos+4:]
        rec = rec[0:pos+4]
        pos = rec.find('<td')
        salary = rec[pos:]

        pos = salary.find("／")
        salarystatus = salary[0:pos]
        pos = salarystatus.find("<div>")
        salarystatus = salarystatus[pos+5:]

        if DEBUG: print salarystatus

        pos = salary.find("円")
        salarylow = salary[0:pos]
        pos = salarylow.find("／")
        salarylow = salarylow[pos+7:]
        
        if DEBUG: print salarylow

        pos = salary.find("円</div>")
        salaryhigh = salary[0:pos]
        pos = salary.find("～")
        salaryhigh = salaryhigh[pos+3:]

        if DEBUG: print salaryhigh

        rec = nxt
        pos = rec.find('/td>')
        nxt = rec[pos+4:]
        rec = rec[0:pos+4]
        pos = rec.find('<td')
        hours = rec[pos:]

        if DEBUG: print hours

        rec = nxt
        pos = rec.find('/td>')
        nxt = rec[pos+4:]
        rec = rec[0:pos+4]
        pos = rec.find('<td')
        category = rec[pos:]

        if DEBUG: print category
    
        # location

        rec = nxt
        pos = rec.find('/td>')
        nxt = rec[pos+4:]
        rec = rec[0:pos+4]
        pos = rec.find('<td')
        location = rec[pos:]

        if DEBUG: print location
    
        # date

        rec = nxt
        pos = rec.find('/td>')
        nxt = rec[pos+4:]
        rec = rec[0:pos+4]
        pos = rec.find('<td')
        date = rec[pos:]

        pos1 = date.find('年')
        pos2 = date.find('月')
        pos3 = date.find('日')

        year  = date[pos1-2:pos1]
        month = date[pos1+7:pos2]
        day   = date[pos2+3:pos3]

        us_date = str(int(year)+1988)+"-0"+month+"-0"+day

        if DEBUG: print us_date

    
        sql = "INSERT IGNORE INTO jobsearch (rec, id, uuid, url, title, salary, salarystatus, salarylow, salaryhigh, hours, category, location, date, us_date) " + "VALUES ('"+ren+"', '"+id+"', '"+uuid+"', '"+url+"', '"+title+"', '"+salary+"', '"+salarystatus+"', '"+salarylow+"', '"+salaryhigh+"', '"+hours+"', '"+category+"', '"+location+"', '"+date+"', '"+us_date+"')"

        try:
            cursor.execute(sql)
            connector.commit()

        except:
            print "Error in MySQL."
    


    cursor.close()
    connector.close()

    
if __name__ == '__main__':

    html = open("Osaka_IT.html")
    
    table = get_table(html)
    
    get_rows(table)

    html.close()

    # get fields from mysql table 
    get_fields(table)

