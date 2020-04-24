from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory

#gc for garbage collector, os required by favicon, mysql.connector for exception handling
import gc, os, mysql.connector

#wraps required for login_required feature
from functools import wraps

#for instant connection formation to mysql server
from dbconnect import connection

app = Flask(__name__)
app.secret_key = "our_secret_key"

@app.route('/favicon.ico')
def favicon():
   return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

"""
def favicon():
    return redirect(url_for('static', filename='favicon.ico'))
"""

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        curs, conn = connection()
        no_user = True
        curs.execute("select password from users where email=%s", (request.form['email'], ))
        if curs.rowcount > 0:
            if request.form['password'] == curs.fetchall()[0][0]:
                session['logged_in'] = True
                curs.execute("select uid from users where email=%s", (request.form['email'], ))
                session['userid'] = curs.fetchall()[0][0]
                curs.close()
                conn.close()
                gc.collect()
                return redirect(url_for('user_dashboard'))
            else:
                flash("Invalid Credentials. Try Again.")
                return redirect(url_for('login'))
        curs.execute("select password from admins where email=%s", (request.form['email'], ))
        if curs.rowcount > 0:
            if request.form['password'] == curs.fetchall()[0][0]:
                session['logged_in'] = True
                curs.execute("select aid from admins where email=%s", (request.form['email'], ))
                session['adminid'] = curs.fetchall()[0][0]
                curs.close()
                conn.close()
                gc.collect()
                return redirect(url_for('admin_dashboard'))
            else:
                flash("Invalid Credentials. Try Again.")
                return redirect(url_for('login'))
        if no_user:
            flash("Invalid Credentials. Try Again.")
            return redirect(url_for('login'))
    return render_template("login.html")
    
@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        department = request.form['department']
        designation = request.form['designation']
        
        curs, conn = connection()
        emailQuery = "select email from users where email='%s'" % (email,)
        curs.execute(emailQuery)
        if curs.rowcount > 0:
            flash("That email is already in use, please choose another.")
        else:
            query = "insert into users (fname, lname, email, password, department, designation) values ('%s', '%s', '%s', '%s', '%s', '%s')" % (fname, lname, email, password, department, designation)
            curs.execute(query)
            conn.commit()
            curs.close()
            conn.close()
            gc.collect()
            flash("Successfully Registered!")
            flash("""Please click <a href="/" class="alert-link">here</a> to return to login page.""")
    return render_template("signup.html")                

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login'))
    return wrap


@app.route('/logout')
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    gc.collect()
    return redirect(url_for('login'))

@app.route('/uDashboard')
@login_required
def user_dashboard():
    curs, conn = connection()
    curs.execute("select * from users where uid=%s", (session['userid'], ))
    user_data = curs.fetchall()[0]
    curs.close()
    conn.close()
    gc.collect()
    return render_template("user_dashboard.html", user_data=user_data)

@app.route('/ReqLeave', methods = ['GET', 'POST'])
@login_required
def request_leave():
    try:
        curs, conn = connection()
        curs.execute("select * from users where uid=%s", (session['userid'], ))
        user_data = curs.fetchall()[0]
        if request.method == "POST":
            curs.execute("select * from leaves where uid=%s and status='pending'", (request.form['uid'], ))
            if curs.rowcount > 0:
                flash("Your another leave is in queue.")
                flash("Please wait until it get response.")
            else:
                query = "insert into leaves (name, email, uid, department, designation, leavetype, fromdate, todate, brief, status) values ('%s', '%s', %s, '%s', '%s', '%s', '%s', '%s', '%s', 'pending')" % (request.form['name'], request.form['email'], request.form['uid'], request.form['department'], request.form['designation'], request.form['leavetype'], request.form['fromdate'], request.form['todate'], request.form['brief'])
                curs.execute(query)
                conn.commit()
                flash("Request has been sent successfully!")
        curs.close()
        conn.close()
        gc.collect()
    except mysql.connector.errors.DataError:
        flash("Some Data is Out of Range")
    return render_template("user_request_leave.html", user_data=user_data)

@app.route('/uNotifications')
@login_required
def user_notifications():
    curs, conn = connection()
    curs.execute("select * from leaves where uid=%s", (session['userid'], ))
    rows=curs.fetchall()
    curs.close()
    conn.close()
    gc.collect()
    return render_template("user_notification.html", rows=rows)

@app.route('/aDashboard')
@login_required
def admin_dashboard():
    curs, conn = connection()
    curs.execute("select * from admins where aid=%s", (session['adminid'], ))
    admin_data = curs.fetchall()[0]
    curs.close()
    conn.close()
    gc.collect()
    return render_template("admin_dashboard.html", admin_data=admin_data)

@app.route('/aNotifications')
@login_required
def admin_notifications():
    curs, conn = connection()
    curs.execute("select * from admins where aid=%s", (session['adminid'], ))
    curs.execute("select * from leaves where department=%s and status='pending'", (curs.fetchall()[0][5], ))
    rows=curs.fetchall()
    curs.close()
    conn.close()
    gc.collect()
    return render_template("admin_notification.html", rows=rows)

@app.route('/aNotifications/approve/<int:lid>', methods = ['GET', 'POST'])
@login_required
def approve_leave(lid):
    curs, conn = connection()
    curs.execute("update leaves set status='approved' where lid=%s", (lid,))
    conn.commit()
    curs.close()
    conn.close()
    gc.collect()
    return redirect(url_for('admin_notifications'))

@app.route('/aNotifications/deny/<int:lid>', methods = ['GET', 'POST'])
@login_required
def deny_leave(lid):
    curs, conn = connection()
    curs.execute("update leaves set status='denied' where lid=%s", (lid,))
    conn.commit()
    curs.close()
    conn.close()
    gc.collect()
    return redirect(url_for('admin_notifications'))

if __name__ == "__main__":
    app.run()
