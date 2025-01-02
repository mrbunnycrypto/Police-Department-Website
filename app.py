from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///police.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class CrimeReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    details = db.Column(db.Text, nullable=False)

db.create_all()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/report')
def report():
    return render_template('report.html')

@app.route('/submit_report', methods=['POST'])
def submit_report():
    name = request.form['name']
    email = request.form['email']
    details = request.form['details']

    report = CrimeReport(name=name, email=email, details=details)
    db.session.add(report)
    db.session.commit()

    return f"Thank you, {name}, for reporting the crime. We will contact you at {email}."

if __name__ == '__main__':
    app.run(debug=True)
