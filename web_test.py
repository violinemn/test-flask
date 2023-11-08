from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def web_test():
    return """
<p>Which Hogwarts lesson would be your favourite:</p>

<form action="submit" method="post">
    <input type="radio" id="a" name="answer" value="a" />
    <label for="a">defence against the dark arts</label><br>
    <input type="radio" id="b" name="answer" value="b" />
    <label for="b">potions class</label><br>
    <input type="radio" id="c" name="answer" value="c" />
    <label for="c">herbology</label><br>
    <input type="radio" id="d" name="answer" value="d" />
    <label for="d">charms</label><br>
    <input type="submit" value="Submit" />
</form>
"""

@app.route('/submit', methods=['POST']) 
def read_form(): 
    data = request.form 
    answer = data['answer']

    return "you selected: "+answer
