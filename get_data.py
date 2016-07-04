# coding utf-8 
import sys
import MySQLdb    
    
      

def get_table(html):

    # Reading line by line.  Create a string of html without new lines.

    all_lines = ''

    f = open(html)

    for line in iter(f):
        all_lines = all_lines+line.rstrip()

    f.close()

    pos = all_lines.find("d-sole")
    table = all_lines[pos:]
    
    pos = table.find('<table')
    table = table[pos:]
    
    pos = table.find('</table>')
    table = table[0:pos+8]

    return table


def get_rows(table):

    pos1 = 1
    count = 0
    
    while pos1 > 0:
        count = count + 1

        print count

        # Stuck in the work so I start learning to git.

        pos1 = table.find('<tr')

        if pos1 > 0:
            table = table[pos1:]
            pos2   = table.find('/tr>')

            table = table[pos2:]

        
        
        

        

def get_fields(table):

    DEBUG = 1

    # For every table skip the header first
    rec = ''
    pos = table.find('<tr')
    rec = table[pos:]

    pos = rec.find('/tr>')
    nxt = rec[pos+4:]
    rec = rec[0:pos]
    
    # new
    rec = nxt
    pos = rec.find('/td>')
    nxt = rec[pos+4:]
    rec = rec[0:pos+4]
    pos = rec.find('<td')
    new = rec[pos:]

    if DEBUG: print new

    # rec
    ren = nxt
    pos = ren.find('/td>')
    nxt = ren[pos+4:]
    ren = ren[0:pos+4]
    pos = ren.find('<td')
    ren = ren[pos:]

    if DEBUG: print rec

    # id

    rec = nxt
    pos = rec.find('/td>')
    nxt = rec[pos+4:]
    rec = rec[0:pos+4]
    pos = rec.find('<td')
    rec = rec[pos:]

    pos = rec.find('</a>')
    rec = rec[0:pos+4]
    pos = rec.find('<a id')
    id  = rec[pos:]
    
    if DEBUG: print id

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

    if DEBUG: print salary

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

    if DEBUG: print date


    connector = MySQLdb.connect(host="localhost",
                                db="hellowork",
                                user="root",
                                passwd="mysql",
                                charset="utf8")

    cursor = connector.cursor()
    sql = "INSERT INTO jobsearch (rec, id, title, salary, hours, category, location, date) " + "VALUES ('"+ren+"', '"+id+"', '"+title+"', '"+salary+"', '"+hours+"', '"+category+"', '"+location+"', '"+date+"')"  

    if DEBUG: print sql
    
    cursor.execute(sql)
    connector.commit()

    cursor.close()
    connector.close()

    
if __name__ == '__main__':

    table = get_table("Osaka_IT.html")

    # Should be getting 20 rows per table.
    get_rows(table)

    # get fields from mysql table 
    # get_fields(table)
