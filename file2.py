from sqlalchemy import create_engine
import pymysql

engine = create_engine('mysql+pymysql://root:@localhost/my_test_db')

conn = engine.connect()

result = conn.execute("SELECT * from personal_info")

for data in result:
    print(data)