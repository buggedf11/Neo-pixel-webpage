import serial
from flask import Flask, render_template, request

app = Flask(__name__)

# Configure the serial port
ser = serial.Serial('COM3', 9600)  # Change 'COM3' to the appropriate port for your Arduino

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_color', methods=['POST'])
def update_color():
    # Get RGB values from the form
    r = int(request.form['red'])
    g = int(request.form['green'])
    b = int(request.form['blue'])

    # Send RGB values to Arduino
    ser.write(bytes(f'{r},{g},{b}\n', 'utf-8'))

    return 'Color updated successfully'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
