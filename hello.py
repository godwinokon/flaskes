from flask import Flask, render_template


# Create a Flask Instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')

#def index():
	#return "<h1>Hello World!</h1>"
#FILTERS
	#safe
	#capitalize
	#lower
	#upper
	#title
	#trim
	#striptags

def index():
	first_name="godwin"
	#stuff ="This is <strong>Bold</strong> Text"
	stuff ="This is Bold Text"
	#stuff ="This is <strong>Bold</strong> Text"

	favorite_soup = ["oha", "okazi", "afam", "idikaiko", 50]
	return render_template("index.html", 
		first_name=first_name,
		stuff=stuff,
		favorite_soup=favorite_soup
		)

#localhost:5000/user/Godwin
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)

# Create Custom Error Pages

#Invalid URL
@app.errorhandler(400)
def page_not_found(e):
	return render_template("400.html"), 400

#Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
	return render_template("500.html"), 500

