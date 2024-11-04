import pymysql
import pandas as pd
conn = pymysql.connect(host='localhost', user='kimms', password='min12231!!', db='sakila', charset='utf8')
cur = conn.cursor(pymysql.cursors.DictCursor)
cur.execute('select * from language')
rows = cur.fetchall()	
language_df = pd.DataFrame(rows)
print(language_df)
#print(language_df.iloc[0:3])
print()
print(language_df['name'])
cur.close()
conn.close()