from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<p>Welcome to Emily's flask experiment! \n Please click the link to visit page 2: \n <a href=\"page2\">Click here</a>  </p>"

@app.route("/page2")
def page2():
    return "<p>To daddy, \n If you're reading this then I have successfully made a link on page 1 to access page 2!</p>"