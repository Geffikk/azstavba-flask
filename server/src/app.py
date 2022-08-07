from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

from flask import Flask, request
import smtplib
import json

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():  # put application's code here
    data = request.get_json(force=True)
    js = str(request.json)
    js = json.loads(js)

    msg = MIMEMultipart()
    msg['Subject'] = js['email']
    msg['From'] = 'e@mail.cc'
    msg['To'] = 'e@mail.cc'

    body = """
    Meno: """ + js["name"] + """
    Email: """ + js['email'] + """
    
    """ + js['message']

    text = MIMEText(body, 'plain')
    msg.attach(text)

    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login("maros.geffert@gmail.com", "banglowmkajvflvc")
    s.sendmail("maros.geffert@gmail.com", "maros.geffert@gmail.com", msg.as_string())
    s.quit()
    print("Email sent...")
    return ""


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))