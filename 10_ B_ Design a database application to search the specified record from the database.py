import mysql.connector 
db=mysql.connector.connect(host="localhost",user="root",passwd="root",database="COMPANY") 
# prepare a cursor object using cursor() method 
cursor = db.cursor() 
sql ="SELECT * FROM EMPLOYEE \
WHERE INCOME > '%d'" % (1000) 
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Fetch all the rows in a list of lists.
    results = cursor.fetchall()
    for row in results:
        ID=row[0]
        fname = row[1]
        lname = row[2]
        age = row[3]
        GENDER = row[4]
        income = row[5]
        PHONE_NO=row[6]
        COUNTRY=row[7]
        # Now print fetched result
        print ("ID=%d,Fname=%s,Lname=%s,Age=%d,GENDER=%s,Income=%d,PHONE_NO=%d,COUNTRY=%s" % \
               (ID,fname, lname, age, GENDER, income,PHONE_NO,COUNTRY))
except:
    print ("Error: unable to fecth data")
    # disconnect from server
    db.close()
