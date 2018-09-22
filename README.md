## About This
As a datascientist you may dont want to write any javascript. This will help you to build ajax callback without writing any javascript. Script is very simple and too small and works like a charm.

I build this script to plot graph dynamically using ajax but you can use this for anything you need for ajax call.

## Flask integration
### app.py
```
from flask import Flask, jsonify, render_template, request, url_for
import pyajax

app = Flask(__name__)

@app.route("/")
def index():
    config = [{
        'handler':{
            'event':{'url':'/ajaxname','target':'submit','method':'click'},
            'input':{'name':'name'},
            'action':{'output':'output'}
        }
    }]
    script = pyajax.buildscript(config)
    return render_template('myname.html', script=script)
    
@app.route("/ajaxname")
def ajaxname():
    return jsonify(output=request.args.get('name'))
    
if __name__ == '__main__':
    app.run()
```
### layout.html

<!doctype html>
<html lang="en">
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
    {% block javascript %}{% endblock %}
  </head>
  <body>
      {% block content %}{% endblock %}
  </body>
</html>

### myname.html
{% extends 'layout.html'%}

{% block content %}
<div><input type="text" id="name" /> <input type="submit" id="submit" value="submit"/></div>
<div>My Name: <span id="output">?</span></div>
{% endblock %}

{% block javascript %}
{{ script|safe }}
{% endblock %}
