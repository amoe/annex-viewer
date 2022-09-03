from flask import Flask
import markdown
import os
import pdb

m = markdown.Markdown()

app = Flask(__name__)

ANNEX_LOCATION = "/home/amoe/ng-annex"

HEADER = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Conforming HTML5 Template</title>

<link rel="shortcut icon" href="data:," type="image/x-icon">
<style>
body{
margin:40px
auto;max-width:650px;line-height:1.6;font-size:18px;color:#444;padding:0
10px;
font-family: serif;
}h1,h2,h3{line-height:1.2}
</style>
</head>
<body>
"""

FOOTER = """
</body>
</html>
"""

@app.route('/annex/<path:path>')
def hello(path):
    full_path = os.path.join(ANNEX_LOCATION, os.path.normpath(path))
    with open(full_path, 'r') as f:
        html = m.convert(f.read())
    m.reset()
    return "{}\n{}\n{}".format(HEADER, html, FOOTER)


@app.route('/hello')
def test():
    return 'Hello, world2!'
