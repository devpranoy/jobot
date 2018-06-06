from flask import Flask ,render_template, flash, redirect, url_for, session, request, logging

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
	if request.method == "POST":
		name=request.form['name']
		email=request.form['email']
		subject=request.form['subject']
		message=request.form['message']
		return "Yo, it's working! "+name+email+subject+message
	else:
		return "Yo it works!"

if __name__ == "__main__":
	app.run()
