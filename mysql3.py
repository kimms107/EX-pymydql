import pymysql
def create_table(conn, cur):
    try:
        query1 = "drop table if exists customer"
        query2 = """create table customer (name varchar(10), category smallint, region varchar(10))"""
        cur.execute(query1)
        cur.execute(query2)
        conn.commit()
        print('Table 생성 완료')
    except Exception as e:
        print(e)
def	main():
    conn = pymysql.connect(host='localhost', user='kimms', password='min12231!!', db='sqlclass_db', charset='utf8')
    cur = conn.cursor()
    create_table(conn, cur)
    cur.close()
    conn.close()
    print('Database	연결 종료')
main()