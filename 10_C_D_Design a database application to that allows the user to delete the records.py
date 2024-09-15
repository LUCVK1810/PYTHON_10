import mysql.connector 
db=mysql.connector.connect(host="localhost",user="root",passwd="root",database="COMPANY") 
# prepare a cursor object using cursor() method 
cursor = db.cursor()
sql = "DELETE FROM EMPLOYEE WHERE AGE < '%d'" % (22) 
try:
    # Execute the SQL command
    cursor.execute(sql)
    print("Data DELETEEd Successfully")
    # Commit your changes in the database
    db.commit() 
except:
    # Rollback in case there is any error
    db.rollback()
    # disconnect from server
    db.close()
