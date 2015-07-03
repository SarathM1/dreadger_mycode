from sqlalchemy import *
from sqlalchemy.orm import mapper

db = create_engine('mysql+mysqlconnector://admin:aaggss@localhost/dredger')
 #FUll- PAth : sqlite:////tmp/tutorial/joindemo.db
 # sudo apt-get install python3-mysql.connector

db.echo = True  					# Print SQL for each SQLAlchemy instruction
metadata = MetaData(db)


def table_create():
    table = Table('db', metadata,
    Column('id',Integer, primary_key=True),
    Column('dredger_name',String(25)),
    Column('time',DateTime,unique=True),  # If not unique then there will be logical errors
    Column('storage_tank_level',Integer),
    Column('storage_tank_cap',String(25)),
    Column('service_tank_level',Integer),
    Column('service_tank_cap',String(25)),
    Column('flowmeter_1_in',Integer),
    Column('flowmeter_1_out',Integer),
    Column('engine_1_status',String(25)),
    Column('flowmeter_2_in',Integer),
    Column('flowmeter_2_out',Integer),
    Column('engine_2_status',String(25)),
    Column('error_other',String(25)),
    Column('error_gsm',String(25)),
    Column('error_gsm_timeout',String(25))
    )

    table.create()

