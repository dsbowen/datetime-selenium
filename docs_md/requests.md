# Get datetime objects from a form

You can also get `datetime.datetime` objects from a form using [Flask requests](https://flask.palletsprojects.com/en/1.1.x/reqcontext/).

Create this simple Flask app in `app.py`.

```python
from datetime_selenium import get_datetime

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
```

If you haven't already, download `form.html`.

```bash
$ curl https://raw.githubusercontent.com/dsbowen/datetime-selenium/master/form.html --output form.html
```

Run the app from your terminal.

```
$ python app.py
```

And navigate to <http://localhost:5000/> in your browser. Fill in the web form and hit the submit button. You'll see the `datetime.datetime` objects printed in your terminal.