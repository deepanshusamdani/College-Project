#!/usr/bin/python3

import kairos_face as kf
import json
import mysql.connector as mysql
from dbconnect import connectdb
import cv2
import requests

cursor = None
conn = None

#initializing enrollment
def init(data) :

	global cursor
	global conn

	# credentials for kairos
	# setting up API keys
	kf.settings.app_id = '83f1c13c'																			#'a123a233'
	kf.settings.app_key = '6cf873f34613874be9247c30dcd32012'									#'03a5065270150ba0e23a0584ae716b0d'

	try :
		# create a connection with database
		conn = connectdb()
		cursor = conn.cursor()

		#check the connection with database
		if conn.is_connected():
			print("Database Connection is established")
		
			if already_registered() :
				return "mark_attendance"
			else :
				sid = register(data)
				return enroll_student(sid)


	except kf.exceptions.ServiceRequestError as e1 :
		print(e1)
		return "kairos error"


def already_registered(img_path='user_img.png') :
	#recognizing registered faces
	recognized_faces = kf.recognize_face(file=img_path, gallery_name='students')

	status = recognized_faces['images'][0]['transaction']['status']

	if status == 'success' :
		return True

	elif status == 'failure' :
		return False

	else :
		print('Error in recognising')

def register(data,img_path='user_img.png') :

	global cursor
	global conn

	# storing data to list
	_fname = data['firstname']
	_lname = data['lastname']
	_dob = data['dob']
	_email = data['email']
	_branch = data['branch']
	_contact = data['contact']

	data = [_fname,_lname,_dob,_email,_branch,_contact]

	# enter into the database
	cursor.execute("INSERT INTO students (firstname,lastname,dob,email,branch,contact) VALUES (%s,%s,%s,%s,%s,%s)", (data[0],data[1],data[2],data[3],data[4],data[5]));
	conn.commit()

	cursor.execute("SELECT * FROM students where contact="+data[-1])
	out = cursor.fetchall()

	sid = out[0][0]
	return sid

def enroll_student(sid,img_path='user_img.png') :
	#enrolling face
	enrolled_face = kf.enroll_face(file=img_path, subject_id=str(sid), gallery_name='students')
	#returning status
	status = enrolled_face['images'][0]['transaction']['status']

	if status == 'success' :
		return "enrolled"
	elif status == 'failure' :
		return "not_able_to_enroll"
		