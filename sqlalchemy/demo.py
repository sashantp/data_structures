import sqlalchemy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey, Text

t = sqlalchemy.__version__  # doctest: +SKIP

print(t)

engine = create_engine('mysql://root:sas.msql@243@localhost/test')

print(engine)

metadata = MetaData()

units = Table('units',metadata,
			Column('id',Integer,primary_key=True),
			Column('title',String(50),nullable=False),
			Column('description',Text))

departments = Table('departments',metadata,
				Column('id',Integer,primary_key=True),
				Column('title',String(50),nullable=False),
				Column('description',Text))
				

tickets = Table('tickets',metadata,
			Column('id',Integer,primary_key=True),
			Column('unit_id',Integer,ForeignKey('units.id')),
			Column('department_id',Integer,ForeignKey('departments.id')))

ticket_posts = Table('ticket_posts',metadata,
			Column('id',Integer,primary_key=True),
			Column('content',Text,nullable=False),
			Column('ticket_id',Integer,ForeignKey('tickets.id')))

metadata.create_all(engine)