import os,sqlite3

def db_join(key,path):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    try:
        sql = "INSERT INTO data(key,path) VALUES ('" + key + "','" + path + "')"
        cursor.execute(sql)
        db.commit()
    except:
        pass

def db_delete(table):
    sql = sqlite3.connect('data.db')
    cur = sql.cursor()
    try:
        cur.execute('DELETE from {};'.format(table))
        sql.commit()
        sql.close()
    except:
        pass

def db_read(table,name):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    select_sql = 'SELECT {} FROM {}'.format(name,table)
    try:
        cursor.execute(select_sql)
        result = cursor.fetchall()
        return result
    except:
        print("Select is failed")
        cursor.close()
        db.close()
        return

def db_search(obj):
    key_read=db_read('data','key')
    n=len(key_read)
    list2=[]
    for m in range(n):
        p=str(key_read[m][0])
        if obj in p:
            path_read=db_read('data','path')
           # print(path_read[m][0])
            list2.append(path_read[m][0])
    return list2

#print (db_search('狗'))