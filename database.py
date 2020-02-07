#! /bin/python3.6

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=xxxx,
                             user='root',
                             password='xxx',
                             db='xxxx',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    #with connection.cursor() as cursor:
        # Create a new record
#        sql = "INSERT INTO `app_ai_oceane_open_ticket` (`origin`, `email_sent`) VALUES (%s, %s)"
 #       cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
   # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT * FROM `app_ai_oceane_open_ticket` where `email_sent`!=%s" 
        sql = "SELECT `email_identifier_1`, `email_origin`,`email_technical_impact`,`email_customer_impact`,`email_processing_priority`,`email_groupe_id` FROM `app_ai_oceane_open_ticket` where `email_sent`!=%s  order by `tstamp` asc"
        cursor.execute(sql,('10'))
        result = cursor.fetchone()
        #for i in result:
        print(result)
finally:
    connection.close() 