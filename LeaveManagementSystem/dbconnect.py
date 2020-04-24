import mysql.connector

def connection():
    conn = mysql.connector.connect(host="localhost", user="sd", password="Deepu@123", database="lms", auth_plugin='mysql_native_password', buffered=True)
    curs = conn.cursor()
    return curs, conn
