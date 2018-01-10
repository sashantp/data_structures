import threading
import random
import time
import MySQLdb
from faker import Factory


# conn = MySQLdb.connect(host='localhost',user='root',passwd='sas.msql@243',db='test')
# print(conn)
# cur = conn.cursor()

# fake = Factory.create()
# i = 0

# try:
# 	while i < 100 :
# 		name = fake.name()
# 		address = fake.address()
# 		query = "insert into users (name,address) values(\""+name+"\",\""+address+"\")"
# 		print(query)
# 		cur.execute(query)
# 		conn.commit()
# 		i = i+1
# except:
# 	conn.rollback()

# cur.close()


def getRecords(limit,offset):
	print("hi")
	conn = MySQLdb.connect(host='localhost',user='root',passwd='sas.msql@243',db='test')
	cur = conn.cursor()
	try:
		cur.execute("""select * from users limit %s offset %s""",(limit,offset))
		resSet = cur.fetchall()
		print(resSet)
		conn.commit()
		time.sleep(2)
		print(threading.get_ident())		
	except Exception as msg:
		print(msg)
		conn.rollback()


threading.Thread(group=None, target=getRecords(5,0), name=None, args=(), kwargs={}, daemon=None)
threading.Thread(group=None, target=getRecords(5,5), name=None, args=(), kwargs={}, daemon=None)
threading.Thread(group=None, target=getRecords(5,10), name=None, args=(), kwargs={}, daemon=None)
threading.Thread(group=None, target=getRecords(5,15), name=None, args=(), kwargs={}, daemon=None)
