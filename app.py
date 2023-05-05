from flask import Flask, render_template
from flaskwebgui import FlaskUI 
import webview

app = Flask(__name__)
# ui= FlaskUI(app) 
window = webview.create_window('Flask_app',app)
@app.route('/')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 22, 'Eat' : 4, 'Commute' : 6, 'Watching TV' : 5, 'Sleeping' : 15}
    return render_template('index.html', data=data)
 
if __name__ == "__main__":
    app.run()
    # webview.start()
    # FlaskUI(app=app, server="flask").run()