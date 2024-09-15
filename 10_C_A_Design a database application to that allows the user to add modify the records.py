import mysql.connector 
db=mysql.connector.connect(host="localhost",user="root",passwd="root",database="COMPANY") 
# prepare a cursor object using cursor() method 
cursor = db.cursor()  
# Prepare SQL query to INSERT a record into the database. 
sql = "INSERT INTO EMPLOYEE(ID,FIRST_NAME, \
   LAST_NAME, AGE,GENDER,INCOME,PHONE_NO,COUNTRY) \
   VALUES ('%d','%s', '%s', '%d', '%s', '%d','%d','%s' )" % \
   (323164,'Ashwin', 'Mehta', 23, 'M', 29000,98631239,'FINLAND') 
try:
    # Execute the SQL command
    cursor.execute(sql)
    print("Data Added Successfully")
    # Commit your changes in the database
    db.commit() 
except:
    # Rollback in case there is any error
    db.rollback()
    # disconnect from server
    db.close()
#10_C_Design a database application to that allows the user to MODIFY the records
