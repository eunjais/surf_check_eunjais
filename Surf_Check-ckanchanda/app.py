from flask import Flask, render_template, redirect

import api_calls
import data.py

app = Flask(__name__)



@app.route("/")def index():    
	return render_template("index.html")

@app.route("/submit")def retrieve():       
  data = api_calls.get_beach_data()    
  return render_template("display_info.html", data=data)

if __name__ == "__main__":    
	app.run()
