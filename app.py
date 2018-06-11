from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging
from slacker import Slacker
import json
import requests
slackClient =Slacker("xoxb-368007597783-376852833876-z57UPooZ3FHD1n50hOv46mmC")
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		name=request.form['name']
		email=request.form['Email']
		subject=request.form['Subject']
		message=request.form['Message']
		#sending to slack
		slackClient.chat.post_message("#general","We have a customer",as_user=True)
		slackClient.chat.post_message("#general","Name: "+name,as_user=True)
		slackClient.chat.post_message("#general","Email: "+email,as_user=True)
		slackClient.chat.post_message("#general","Subject: "+subject,as_user=True)
		slackClient.chat.post_message("#general","Message: "+message,as_user=True)
		#sending data to log it on aws 
		data = {'name':name,'email':email,'subject':subject,'message':message}
		data_json = json.dumps(data)
		r = requests.post('https://www.iodev.co.in', data=data_json)
		return "Yo, it's working! "
	else:
		
		messageToChannel = "Guys, someone is trying to undress me. Help!!"
		slackClient.chat.post_message("#general",messageToChannel,as_user=True)
		return "Yo it works!123"

if __name__ == "__main__":
	app.run()
