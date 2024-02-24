# pip install mysql-connector
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bootstrap import Bootstrap
import random
import string
import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Change this to a random string for production
bootstrap = Bootstrap(app)

# Dummy data for demonstration
shipments = [
    {'tracking_id': 'ABC123', 'status': 'In transit', 'location': 'New York', 'eta': '2 days'},
    {'tracking_id': 'XYZ789', 'status': 'Delivered', 'location': 'Los Angeles', 'eta': 'Delivered on 21st Feb'},
 ]

@app.route('/')
def index():
    # return ("abc")
    return render_template("index.html", shipments=shipments)

@app.route('/track', methods=['POST'])
def track():
    tracking_id = request.form['tracking_id']
    # Dummy logic to check tracking ID
    for shipment in shipments:
        if shipment['tracking_id'] == tracking_id:
            return render_template('tracking_result.html', shipment=shipment)
    flash('Tracking ID not found!', 'danger')
    return redirect(url_for('index'))

@app.route('/create_shipment', methods=['GET', 'POST'])
def create_shipment():
    if request.method == 'POST':
        tracking_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        status = request.form['status']
        location = request.form['location']
        eta = request.form['eta']
        shipments.append({'tracking_id': tracking_id, 'status': status, 'location': location, 'eta': eta})
        flash('Shipment created successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('create_shipment.html')

if __name__ == '__main__':
    app.run(debug=True)
