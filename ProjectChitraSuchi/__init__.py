#!/usr/bin/python3

from flask import Flask, flash, redirect, render_template, request, session, abort,Response,Markup
import enroll_form
from camera import VideoCamera
import mysql.connector as mysql
from plotly.offline import plot
from plotly.graph_objs import Bar
import numpy as np
import datetime
import get_sub_id as gsid
from dbconnect import connectdb

app = Flask(__name__)
 
camera1 = None
userdata = None

@app.route("/")
def index():
	if camera1 != None :
		camera1.__del__()
		camera1 == None
	return render_template("index.html")

@app.route("/enroll", methods=['GET','POST'])
def enroll():
	global userdata

	if request.method=='GET' :
		return render_template("enroll.html")
	elif request.method=='POST' :
		if request.form["action"] == 'SUBMIT':
			userdata = request.form
			return render_template('take_pic.html',result=userdata)
		else :
			return "bad request!! Error"
	else :
		return "page not found"

@app.route("/takepic")
def takepic():
	global camera1
	global userdata

	if camera1 == None :
		print('object created')
		camera1 = VideoCamera()
	camera1.save_image()
	camera1.__del__()
	camera1 = None
	status = enroll_form.init(userdata)
	# userdata = None
	return render_template('take_pic.html',message=status,result=userdata)

@app.route("/cam")
def camera_in_page():
	return "integration in process"

@app.route("/mark_attendance")
def mark_attendance():
	return render_template("mark_attendance.html")

#to open camera in webpage streamed with python
def gen():
	global camera1
	if camera1 == None :
		print('object created')
		camera1 = VideoCamera()
	while True:
		frame = camera1.get_frame()
		# yield method is used to return without destroying local variable instances
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

# to mark attendance
@app.route('/capture_image')
def capture_image():
	global camera1
	if camera1 == None :
		print('object created')
		camera1 = VideoCamera()
	camera1.save_image()
	camera1.__del__()
	camera1 = None
	status = gsid.init()
	return render_template('mark_attendance.html',message=status)

#for showing details
@app.route("/table")
def create_table():

	conn = connectdb()
	cursor = conn.cursor()

	if conn.is_connected():
		print("True")

	response = "<head><meta http-equiv='refresh' content='7'></head>"
	out = cursor.execute("SELECT * FROM students")
	data = cursor.fetchall()
	return render_template('db_tables.html', data=data)

# below code will show student economy on graph page linking matplotlib with html page
@app.route("/showgraph")
def results():
	# create an empty list to be filled with the elements in future using np.append()
	date_list = []
	student_list = []
	conn1 = connectdb()
	cursor1 = conn1.cursor(buffered=True)
	
	if conn1.is_connected():
		# fetch dates from database on to plot on x-axis	
		cursor1.execute("SELECT Distinct date from attendance")
		out1 = cursor1.fetchall()
		for i in out1:
			date_list.append(i[0])

		# fetch total presence on specific date from database on to plot on y-axis	
		try :
			for i in date_list:
				cursor1.execute("SELECT count(rno) FROM attendance where date = '%s' " %i)
				total = cursor1.fetchall()
				# total returns a list of tuple
				student_list.append(str(total[0][0]))
		except mysql.errors.InternalError as e:
			print(e)

		# my_plot_div = plot([Scatter(x=date_list, y=student_list)], output_type='div')    	
		my_plot_div = plot([Bar(x=date_list, y=student_list)], output_type='div')    	
		return render_template('graph.html',div_placeholder=Markup(my_plot_div))

if __name__ == "__main__":
    app.run(debug=True)