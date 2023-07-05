from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  # SQLite database
app.secret_key = 'your_secret_key'  # Secret key for session
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    college = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    roll_no = db.Column(db.String(20), nullable=False)
    mobile_no = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Student {self.name}>"
    
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        college = request.form['college']
        age = int(request.form['age'])
        roll_no = request.form['roll_no']
        mobile_no = request.form['mobile_no']
        email = request.form['email']

        error_messages = []

        if age < 18:
            error_messages.append("Age must be greater than or equal to 18")

        if len(mobile_no) != 10:
            error_messages.append("Mobile number must have 10 digits")

        if not validate_email(email):
            error_messages.append("Invalid email format")

        if Student.query.filter_by(roll_no=roll_no).first():
            error_messages.append("Roll number already exists")

        if Student.query.filter_by(mobile_no=mobile_no).first():
            error_messages.append("Mobile number already exists")

        if Student.query.filter_by(email=email).first():
            error_messages.append("Email already exists")

        if error_messages:
            session['error_messages'] = error_messages
            return redirect(url_for('index'))

        student = Student(name=name, college=college, age=age, roll_no=roll_no, mobile_no=mobile_no, email=email)
        db.session.add(student)
        db.session.commit()

        return redirect(url_for('display_data'))

    if 'error_messages' in session:
        error_messages = session['error_messages']
        session.pop('error_messages', None)
        return render_template('index.html', error_messages=error_messages)

    return render_template('index.html')


@app.route('/display', methods=['GET'])
def display_data():
    students = Student.query.all()
    return render_template('display.html', students=students)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
