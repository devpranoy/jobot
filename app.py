from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging
from slacker import Slacker
slackClient =Slacker("xoxb-368007597783-376852833876-z57UPooZ3FHD1n50hOv46mmC")
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		name=request.form['name']
		email=request.form['Email']
		subject=request.form['Subject']
		message=request.form['Message']
		slackClient.chat.post_message("#general","boisss we have a customer",as_user=True)
		slackClient.chat.post_message("#general","Name: "+name,as_user=True)
		slackClient.chat.post_message("#general","Email: "+email,as_user=True)
		slackClient.chat.post_message("#general","Subject: "+subject,as_user=True)
		slackClient.chat.post_message("#general","Message: "+message,as_user=True)
		return "Yo, it's working! "
	else:
		
		messageToChannel = "Hey Martin, Ren Says Hi"
		slackClient.chat.post_message("#general",messageToChannel,as_user=True)
		return "Yo it works!123"

if __name__ == "__main__":
	app.run()
