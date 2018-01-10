import sys
import threading
import random
import time
import MySQLdb
from faker import Factory


fake = Factory.create()
name = fake.name()
address = fake.address()
address = fake.text()

try:
	conn = MySQLdb.connect(host='localhost',user='root',passwd='sas.msql@243',db='test')
	print(conn)
	cur = conn.cursor()
	query = "insert into users (name,address) values(\""+name+"\",\""+address+"\")"
	print(query)
	cur.execute(query)
	conn.commit()
	cur.close()
except Exception as msg:
	print(msg)
	sys.exit("Fatal")
	conn.rollback()
	cur.close()


