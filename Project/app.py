from flask import Flask, render_template, session, url_for, request, redirect,make_response
import random
import ibm_db
import ibm_db2_connect
# testing
app = Flask(__name__)
app.secret_key = "secret_key"


@app.route('/', methods=['GET', 'POST'])
def index():
    if session.get('logged_in'):
        return render_template('home.html')
    return render_template('index.html')


@app.route('/login',methods=['POST'])
def login():
    # conn = ibm_db2_connect.db2.get_conn()
    form_user = request.form['username']
    # form_password = request.form['password']
    # sql = 'SELECT username from user WHERE username=? and password=?'
    # stmt = ibm_db.prepare(conn, sql)
    # ibm_db.bind_param(stmt, 1, form_user)
    # ibm_db.bind_param(stmt, 2, form_password)
    # ibm_db.execute(stmt)
    # account = ibm_db.fetch_assoc(stmt)
    # if account:
    session['logged_in']=form_user
    return redirect('/')

@app.route('/loginvalidate',methods=['POST','GET'])
def loginvalidate():
    conn = ibm_db2_connect.db2.get_conn()
    data=request.get_json();
    form_user = data['username']
    form_password = data['password']
    sql = 'SELECT username from user WHERE username=? and password=?'
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt, 1, form_user)
    ibm_db.bind_param(stmt, 2, form_password)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    if account:
        # session['logged_in']=form_user
        response = make_response('success',200)
    else:
        response = make_response('failure',200)
    response.mimetype = "text/plain"
    return  response

@app.route('/register',methods=['POST'])
def register():
    try:
        conn = ibm_db2_connect.db2.get_conn()
        form_user = request.form['username']
        form_password = request.form['password']
        form_mail = request.form['mail']
        form_phone = request.form['phone']
        uid=getUid(form_user,form_phone)
        sql = 'insert into user values(?,?,?,?,?)'
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, uid)
        ibm_db.bind_param(stmt, 2, form_user)
        ibm_db.bind_param(stmt, 3, form_password)
        ibm_db.bind_param(stmt, 4, form_mail)
        ibm_db.bind_param(stmt, 5, form_phone)
        ibm_db.execute(stmt)

    except Exception as e:
        print(e)
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return render_template('index.html')

def getUid(username,usermobile):
    return random.randint(1,100000)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
