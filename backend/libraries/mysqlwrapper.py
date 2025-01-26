import pymysql

def updateQuery(query,values):
    try:
        conn = pymysql.connect(host = "localhost", user="root", password="simple", database="properties" )
        cursor = conn.cursor()
        if values!=None:
            cursor.execute(query,values)
        else:
            cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred: {e}")


def selectQuery(query,values=None):
    try:
        conn = pymysql.connect(host = "localhost", user="root", password="simple", database="properties" )
        cursor = conn.cursor()
        if values!=None:
            cursor.execute(query,values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def selectBackend(pool,query,values=None):
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        if values!=None:
            cursor.execute(query,values)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    except Exception as e:
        print(f"An error occurred in mysqlwrapper in selectBackend: {e}")
        conn.close()
        return None
    
def insertBackend(pool,query,values=None):
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        if values!=None:
            cursor.execute(query,values)
        else:
            cursor.execute(query)
        conn.commit()
        id = cursor.lastrowid
        cursor.close()
        conn.close()
        return id
    except Exception as e:
        print(f"An error occurred in mysqlwrapper in insertBackend: {e}")
        conn.close()
        return None

def updateBackend(pool,query,values=None):
    try:
        conn = pool.get_connection()
        cursor = conn.cursor()
        if values!=None:
            cursor.execute(query,values)
        else:
            cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"An error occurred in mysqlwrapper in updateBackend: {e}")
        conn.close()

def deleteBackend(pool,query,values=None):
    updateBackend(pool,query,values)