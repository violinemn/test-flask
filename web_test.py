from flask import Flask, request

app = Flask(__name__)

question_number = 0
questions = [
    ["On a rainy day, would you rather:", ["stay in bed all day", "visit the local library", "play on devices", "snuggle up and read"]], 
    ["Which Hogwarts lesson would be your favourite:", ["defence against the dark arts", "potions class", "herbology", "charms"]], 
    ["Which quality best describes you:", ["confident", "brave", "smart", "hard working"]],
    ["Who would you most like to turn into a toad:", ["Draco Malfoy", "Hagrid", "You-Know-Who", "Professor Snape"]], 
    ["What is your favourite movie genre:", ["action", "drama", "comedy", "documentary"]]
     ]

@app.route("/", methods=['GET'])
def web_test():
    global question_number
    if question_number == 5:
        return "Thank you for playing"
    else:
        current_question = questions[question_number]
        return create_question(current_question[0], current_question[1])

@app.route('/submit', methods=['POST']) 
def read_form(): 
    global question_number
    data = request.form 
    answer = data['answer']
    question_number = question_number + 1
    return "you selected: "+answer+ "<p> \n Please click the link for next question: \n <a href=\"/\">Click here</a>  </p>"

def create_question(question, answers):
    text_to_ask_user = """
    <p>{question}</p>

    <form action="submit" method="post">
        <input type="radio" id="a" name="answer" value="a" />
        <label for="a">{answers0}</label><br>
        <input type="radio" id="b" name="answer" value="b" />
        <label for="b">{answers1}</label><br>
        <input type="radio" id="c" name="answer" value="c" />
        <label for="c">{answers2}</label><br>
        <input type="radio" id="d" name="answer" value="d" />
        <label for="d">{answers3}</label><br>
        <input type="submit" value="Submit" />
    </form>
  """.format(question=question, answers0=answers[0], answers1=answers[1], answers2=answers[2], answers3=answers[3])
    return text_to_ask_user
