#!/usr/bin/env python3

import mysql.connector as mysql

def connectdb() :

	conn = mysql.connect(user='sd',password='Deepu@123',database='studentdb',host='127.0.0.1')

	#check the connection with database
	if conn.is_connected():
		print("Database Connection is established")

	return conn