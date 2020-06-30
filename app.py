from selenium_tools import get_datetime

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        for html_type, val in request.form.items():
            print(get_datetime(html_type, val))
    return open('form.html').read()

if __name__ == '__main__':
    app.run(debug=True)