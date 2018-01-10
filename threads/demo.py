import threading
import random
import time
import MySQLdb
from faker import Factory
import requests

class EventsHandler(threading.Thread):

	offset = 0
	limit = 0

	def __init__(self,offset):
		threading.Thread.__init__(self)
		self.offset = offset
		self.limit = 10

	def fetchRecords(self):			

		try:
			conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='test')
			print(conn)
			cur =conn.cursor()
			cur.execute("""select * from users limit %s offset %s""",(self.limit,self.offset))
			resSet = cur.fetchall()
			# print(resSet)

			for rec in resSet :
				print(threading.get_ident())
				print(rec)

			conn.commit()

			return resSet

		except Exception as msg:
			conn.rollback()
			print(msg)

	def run(self):
		try:
			conn = MySQLdb.connect(host='localhost',user='root',passwd='',db='test')
			print(conn)
			return self.fetchRecords()
			
			i = 1
			# limit = 5
			# while i < 10 :
			# 	fake = Factory.create()
			# 	name = fake.name()
			# 	address = fake.address()
			# 	address = fake.text()
				# print(name,address,text)
				# query = "insert into users(name,address) values(\""+name+"\",\""+address+"\")"
				# print(query)
				# conn.query(query)
				# cur.execute("""select * from users limit %s offset %s""",(limit,offset))
				# time.sleep(2)
				# t = random.randint(11,99)
				# print(t)
				# print(threading.get_ident())
				# i = i + 1
				# print(threading.active_count())
				# conn.commit()
		except Exception as msg:
			conn.rollback()
			print(msg)


class wayBackHandler(threading.Thread):

	domainName = "";
	responseObjsList = {}

	def __init__(self):
		threading.Thread.__init__(self)

	def setValues(self,domainName):
		self.domainName = domainName
			

	def wayBackCapture(self):

		wayBackEndpoint = "http://archive.org/wayback/available"
		
		apiParams = {'url':self.domainName}

		response = requests.get(wayBackEndpoint,apiParams)
		
		if response.status_code == 200 :
			print(response.text)

		print(response.url)


	def run(self):
		try:
			print(threading.get_ident())
			self.wayBackCapture()	
		except Exception as msg:
			print(msg)


class wayBackFactory():

	def create(self):
		return wayBackHandler()	


class objectPool():

	def addObject(self,object):
		
		
	def getObject(self,objectId):		


urls = ["exa.com","cheesecake.com.au","inghams.com.au","myntra.com"]

wayBackFact = wayBackFactory()

for url in urls :
	wayBack = wayBackFact.create()
	wayBack.setValues(url)
	wayBack.start()


# ev = EventsHandler(0)
# ev1 = EventsHandler(10)
# ev2 = EventsHandler(20)
# ev3 = EventsHandler(30)

# ev.start()
# ev.join()
# ev1.start()
# ev2.start()
# ev3.start()


# wayBack = wayBackHandler("exa.com")
# wayBack1 = wayBackHandler("cheesecake.com.au")
# wayBack2 = wayBackHandler("inghams.com.au")
# wayBack3 = wayBackHandler("myntra.com")

# 
# wayBack1.start()
# wayBack2.start()
# wayBack3.start()
