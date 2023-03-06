import sqlite3
from flask import Flask, render_template, request , session ,redirect
from flask_session import Session
import datetime

from helpers import login_required


#Configure app
app = Flask(__name__)

#Configure session
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = "filesystem"
Session(app)


tasks = []

@app.route("/")
@login_required
def index():
    try:
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        cursor2 = db.cursor()
        id = session.get("user_id")
        page = request.args.get("type")
        date = request.args.get("date")
        if date:
            date = date
        elif not date :
            date = datetime.datetime.now()
            date = date.strftime("%x")
        cursor2.execute("SELECT count(task_id) from tasks where id=? and status=0 and date=?" ,(id,date,))
        count = cursor2.fetchall()  
        if page == "all" or not page:
            cursor.execute("SELECT task,task_id,status FROM tasks WHERE id=? and date=?" ,(id,date,) )
            output = cursor.fetchall()
        elif page == "active":
            cursor.execute("SELECT task,task_id FROM tasks WHERE id=? and date=? and status=0" ,(id,date,) )
            output = cursor.fetchall()

     
        return render_template("index.html", data=output , date=date, count=count)
    except:
        return render_template("index.html")
    

@app.route("/add" , methods=["POST"])
@login_required
def add():

    if request.method == "POST":
        task = request.form.get("task")

        if not task:
            return render_template("apology.html" , message="Field cannot be blank")


        date = datetime.datetime.now()
        date = date.strftime("%x")

        id = session.get("user_id")
        record = [(id,task,date)]
      
        
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        cursor2 = db.cursor()
        cursor.executemany("INSERT INTO tasks(id,task,date,status) VALUES(?,?,?,0)" , record)
        cursor.execute("SELECT task,task_id,status FROM tasks WHERE id=? and date=?" ,(id,date,))
        cursor2.execute("SELECT count(task_id) from tasks where id=? and status=0 and date=?" ,(id,date,))


        output = cursor.fetchall()
        count = cursor2.fetchall()  

        db.commit()
        db.close()

        return render_template("index.html" , data=output , date=date, count=count)


@app.route("/register" , methods=["GET" , "POST"])
def register():

    if request.method == "POST":


        name = request.form.get("username")
        password = request.form.get("password")

        record = [(name,password)]

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.executemany('''INSERT INTO users(username,password) VALUES(?,?)''',record)     
        conn.commit()
        conn.close()

        return render_template("login.html")
    else:
        return render_template("register.html")

@app.route("/login" , methods=["GET" , "POST"])
def login():

    session.clear()

    if request.method == "POST":
        
        username = request.form.get("username")
        password = request.form.get("password")

        record = [(username)]

        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        try:
            cursor.execute('''SELECT * FROM users WHERE username = ?''' ,record )

        
            output = cursor.fetchall()
            db_password = output[0][2]

            if password!=db_password:
                return render_template("apology.html" , message="Password Invalid")
            
            session['user_id'] = output[0][0]

            return redirect("/")
        except:
            return render_template("apology.html" , message="User not registered")

    else:
        return render_template("login.html")


@app.route("/remove" , methods=["POST"])
@login_required
def remove():

    task_id = request.form.get("id")
    task_id = [(task_id)]
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    print(task_id)

    cursor.execute('''DELETE FROM tasks WHERE task_id=?''' , task_id)

    db.commit()
    db.close()

    return redirect("/")


@app.route("/logout")
def logout():
    
    session.clear()

    return redirect("/")

@app.route("/record" , methods=["POST"])
@login_required
def record():
    date = datetime.datetime.now()
    date = date.strftime("%x")
    task_id = request.form.get("id_s")
    id = session.get("user_id")
    db = sqlite3.connect("data.db")
    cursor = db.cursor()

    cursor.execute("UPDATE tasks SET status=1 WHERE id=? and task_id=?;",(id,task_id,))
    print("updated")
    db.commit()
    db.close()

    return redirect("/")

@app.route("/completed" , methods=["POST"])
@login_required
def completed():
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        cursor2 = db.cursor()
        id = session.get("user_id")
        date = datetime.datetime.now()
        date = date.strftime("%x")
        
        cursor.execute("SELECT task,task_id FROM tasks WHERE id=? and status=1" ,(id,) )
        cursor2.execute("SELECT count(task_id) from tasks where id=? and status=0 and date=?" , (id,date,))
        output = cursor.fetchall()
        count = cursor2.fetchall()
        return render_template("index.html", data=output, count=count)


if __name__ == "__main__":
    app.run()







    



