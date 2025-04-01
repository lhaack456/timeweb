from flask import Flask, render_template
import os 

app = Flask(__name__)
app.secret_key='REPLACE_ME_WITH_RANDOM_CHARACTERS'


from datetime import datetime




@app.route('/')
def main():
    now = datetime.now()
    formatted_date = now.strftime("%b %d, %Y %H:%M") 
    return "<h1>Current Date and Time:</h1><p>{}</p>".format(formatted_date)

if __name__ == "__main__":
    app.run(host="10.92.21.104", port="42069", debug=False)
