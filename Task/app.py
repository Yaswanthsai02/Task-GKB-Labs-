from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization
conn = sqlite3.connect('userdata.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, age INTEGER, dob DATE)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    dob = request.form['dob']

    if not (name and email and age and dob):
        return "All fields are required!"

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except ValueError:
        return "Age must be a positive integer!"

    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (name, email, age, dob) VALUES (?, ?, ?, ?)", (name, email, age, dob))
    conn.commit()
    conn.close()

    return redirect(url_for('show_data'))

@app.route('/data')
def show_data():
    conn = sqlite3.connect('userdata.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    data = c.fetchall()
    conn.close()

    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
