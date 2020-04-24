# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 16:30:19 2019

@author: Karan
"""

import mysql.connector

def connection():
    conn = mysql.connector.connect(host="localhost", user="sd", password="Deepu@123", database="cbeg")
    curs = conn.cursor()
    return curs, conn
