#!/usr/bin/env python
# encoding=utf8 
import sys
import MySQLdb
import urllib2


reload(sys)
sys.setdefaultencoding('utf8')


def fetch_details(url):

    response = urllib2.urlopen(url)
    html = response.read()

    details = html
    pos = details.find("仕事の内容")
    details = details[pos:]
    pos = details.find("<td>")
    details = details[pos+4:]
    pos = details.find("</td>")
    details = details[0:pos]

    details = details.replace('<div class=\"wordBreak\">','')
    details = details.replace('</div>','')

    details = details.rstrip()
    details = details.lstrip()

    number = html
    pos    = number.find("従業員数")
    number = number[pos:]
    pos    = number.find("<div>")
    number = number[pos+5:]
    pos    = number.find("</div>")
    number = number[0:pos]

    local = number
    pos   = local.find("うち就業場所:")
    local = local[pos+19:]
    pos   = local.find("人")
    local = local[0:pos]

    return (details, number, local)


def get_details_uuid():

    connector = MySQLdb.connect(host="localhost",
				db="hellowork",
				user="root",
				passwd="mysql",
				charset="utf8")

    cursor = connector.cursor()


    # Working on jobsearch
    cursor.execute("SELECT uuid, url FROM jobsearch ORDER BY date DESC")

    result = cursor.fetchall()

    # For each UUID details are obtained.
    for row in result:

           uuid = row[0]
           url  = row[1]

           sql = "SELECT num FROM jobdetails WHERE uuid='"+uuid+"'"

           cursor.execute(sql)
           if (cursor.rowcount < 1):
           
               (detail, number, number_local) = fetch_details(url)
          
               # Working on jobdetails
               sql = "INSERT IGNORE INTO jobdetails (uuid, detail, number, number_local) VALUE ('"+uuid+"', '"+detail+"', '"+number+"', '"+number_local+"')"

               cursor.execute(sql)
               connector.commit()
                                      
    cursor.close()
    connector.close()




if __name__ == '__main__':


    get_details_uuid()
