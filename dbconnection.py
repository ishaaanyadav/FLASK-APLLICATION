import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="",
                             database="testdb")
cur = mydb.cursor()
mysql="insert into students(firstName,lastName,phone) values (%s,%s,%s)"
dets=[("ayush","patra",123456789),("shrey","pingoo",9876543210)]
cur.executemany(mysql,dets)
mydb.commit()