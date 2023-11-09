from flask import Flask, request

app = Flask(__name__)

scores = [["gryffindor", 0], ["slytherin", 0], ["hufflepuff", 0], ["ravenclaw", 0]]

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
    global question_number, scores
    if question_number == 5:
        # find highest house score
        return "It sounds like you'd fit best in "+get_highest_house_from_scores(scores)
    else:
        current_question = questions[question_number]
        return create_question(current_question[0], current_question[1])

@app.route('/submit', methods=['POST']) 
def read_form(): 
    global question_number, scores
    data = request.form 
    answer = data['answer']
    calculate_question_score(answer, scores)
    question_number = question_number + 1
    return "<p><center> You answered: "+answer+ "<center><p>""<p><center> \n Please click the link for next question: \n <a href=\"/\">Click here</a>  <center></p>"

def create_question(question, answers):
    text_to_ask_user = """
    <p><center><font size="+100">\n{question}</font><center></p>

    <form action="submit" method="post">
        <table>  
            <tr>
                <td><input type="radio" style="vertical-align: middle" id="a" name="answer" value="a" />
                <label for="a">{answers0}</label><br></td>
            </tr>
            <tr>
                <td><input type="radio" style="vertical-align: middle" id="b" name="answer" value="b" />
                <label for="b">{answers1}</label><br></td>
            </tr>
            <tr>
                <td><input type="radio" style="vertical-align: middle" id="c" name="answer" value="c" />
                <label for="c">{answers2}</label><br></td>
            </tr>
            <tr>
                <td><input type="radio" style="vertical-align: middle" id="d" name="answer" value="d" />
                <label for="d">{answers3}</label><br><br></td>
            </tr>
        </table>
            <input type="submit" value="Submit" />
    </form>
  """.format(question=question, answers0=answers[0], answers1=answers[1], answers2=answers[2], answers3=answers[3])
    return text_to_ask_user

def calculate_question_score(answer, scores):
    if answer == "a":
        add_one_to_house("gryffindor", scores)
    if answer == "b":
        add_one_to_house("slytherin", scores)
    if answer == "c":
        add_one_to_house("hufflepuff", scores)
    if answer == "d":
        add_one_to_house("ravenclaw", scores)

def add_one_to_house(house_name, scores):
    houses = get_houses_from_scores(scores)
    house_score = scores[houses.index(house_name)][1]
    scores[houses.index(house_name)] = [house_name, house_score + 1]

def get_houses_from_scores(scores):
    return [score_item[0] for score_item in scores]

 #pass in scores, find highest and return name of house
def get_highest_house_from_scores(scores):
    scores.sort(key = lambda x: x[1])
    scores.reverse()
    return scores[0][0]