import pymysql
import json

def mysql_connect():
    host = '18.180.248.102'
    port = 3306
    database = 'mytable'
    name = 'root'
    password = 'test1234'
    conn = pymysql.connect(host=host,port=port,database=database,user=name,password=password)

    return conn

def mysql_query():

    conn = mysql_connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'SELECT * FROM login'
    cur.execute(sql)
    res = cur.fetchall()

    return json.dumps(res,indent=1)

def mysql_query2(id,nickname):

    conn = mysql_connect()
    sql = "insert into login(name,password) values ('"+str(id)+"',"+"'"+str(nickname)+"')"
    cur=conn.cursor()
    cur.execute(sql)
    conn.commit()

    return "successed"