import mysql.connector
import pandas as pd
conn = mysql.connector.connect(user='root', password='', host='localhost', database='my_test_db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM personal_info')
data = cursor.fetchall()
df = pd.DataFrame(data)
print(df)
conn.close()