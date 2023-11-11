from flask import Flask, request

app = Flask(__name__)

scores = [["gryffindor", 0], ["slytherin", 0], ["hufflepuff", 0], ["ravenclaw", 0]]

question_number = 0
questions = [
    ["Which Hogwarts lesson would be your favourite:", ["Defence against the dark arts", "Potions class", "Herbology", "Charms"]], 
    ["Which quality best describes you:", ["Confident", "Brave", "Smart", "Hard working"]],
    ["Who would you most like to turn into a toad:", ["Draco Malfoy", "Hagrid", "You-Know-Who", "Professor Snape"]], 
    ["What is your favourite movie genre:", ["Action", "Drama", "Comedy", "Documentary"]],
    ["Which creature would you prefer for a pet:", ["Hippogriff", "Dragon", "Unicorn", "Centaur"]],
    ["How do you get on in school:", ["I survive the lessons, but with adventure on my mind", "I'm the class prankster/clown and I don't care", "I pay attention and am very interactive with the students and the teacher", "I get very good grades, and exceed exceptionally"]],
    ["Which would you most want to use magic for:", ["Helping protect others", "Gaining power for myself", "Doing fun magic tricks", "Solving world hunger"]],
    ["Which flavour of jelly bean would you prefer:", ["Strawberry", "Chocolate", "Peanut butter", "Licorice"]]
     ]
html_page="""
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="/static/my_stylesheet.css">
    <link rel="icon" type="image/x-icon" href="/static/sorting_hat_favicon_new.ico">
    </head>
    <body>
    {main_paragraph}
    </body>
    </html>
    """
@app.route("/", methods=['GET'])
def web_test():
    global question_number, scores, html_page
    content_paragraph = ""
    if question_number == 8:
        # find highest house score
        content_paragraph = "<p>🎉 It sounds like you'd fit best in "+get_highest_house_from_scores(scores)+"</p>"
    else:
        current_question = questions[question_number]
        content_paragraph = create_question(current_question[0], current_question[1])
    return html_page.format(main_paragraph = content_paragraph)

@app.route('/submit', methods=['POST']) 
def read_form(): 
    global question_number, scores, html_page
    data = request.form 
    answer = data['answer']
    calculate_question_score(answer, scores)
    question_number = question_number + 1
    content_paragraph = "<p><center> You answered: "+answer+ "<center><p>""<p><center> \n Please click the link for next question: \n <a href=\"/\">Click here</a>  <center></p>"
    return html_page.format(main_paragraph = content_paragraph)

def create_question(question, answers):
    text_to_ask_user = """
    <p><center><font size="+50">\n{question}</font><center></p>
    <img src="static/sorting_hat_pic.png" alt="the sorting hat" height="300px">
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
    #<img src="cosy_rainy_day.jpg" alt="cosy things on windowsill rainy day">
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

#<a href="{{ url_for('web_test') }}">Sorting Hat Quiz</a>
