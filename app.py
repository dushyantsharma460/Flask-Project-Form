from flask import Flask ,render_template,request,redirect,url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'registration_db'
app.config['MYSQL_PASSWORD']= 'mamta@sharma123'

mysql = MySQL(app)

@app.route("/")
def registration_form():
    return render_template('index.html')

@app.route('/register',methods =['POST'])
def register():
    if (request.method =='POST'):
        student_name = request.form['student_name']
        father_name = request.form['father_name']
        student_mother_name = request.form['student_mother_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        date_of_birth = request.form['date_of_birth']
        student_address = request.form['student_address']
        blood_group = request.form['blood_group']
        department = request.form['department']
        course = request.form['course']
        password= request.form['passwords']
        


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (student_name, father_name, student_mother_name, phone_number, email, date_of_birth, student_address, blood_group, department, course, password) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (student_name, father_name, student_mother_name, phone_number, email, date_of_birth, student_address, blood_group, department, course, password))

        mysql.connection.commit()
        cur.close()

        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)