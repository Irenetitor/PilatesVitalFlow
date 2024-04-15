from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

faq_list = []        
exercise_list = []        
user_question_list = []

# Open the JSON file
with open('faqs.json', 'r') as file:
    faq_data = json.load(file)
    faq_list = faq_data['faqs']

with open('exercises.json', 'r') as file:
    exercise_data = json.load(file)

class Exercise:
    def __init__(self, id, title, image, name, explanation, breathing_technique, level):
        """
        Represents the exercise.

        Args:
            id (str): The exercise id.
            title (str): The title of the exercise.
            image (str): Image file name.
            name (str): A dynamic warm-up exercise description.
            explanation (str): Detailed instructions for performing the exercise.
            breathing_technique (str): Instructions for coordinating breath with arm pumps.
            level (dict): A dictionary containing different difficulty levels.
                Keys: 'beginner', 'intermediate', 'advanced'
                Values: Descriptions for each level.
        """
        self.id = id
        self.title = title
        self.image = image
        self.name = name
        self.explanation = explanation
        self.breathing_technique = breathing_technique
        self.level = level

class ExerciseLevel:
    def __init__(self, beginner, intermediate, advanced):
        """
        Represents different difficulty levels for the exercise.

        Args:
            beginner (str): Instructions for beginners.
            intermediate (str): Instructions for intermediate level.
            advanced (str): Instructions for advanced level.
        """
        self.beginner = beginner
        self.intermediate = intermediate
        self.advanced = advanced       

# Create a list of Exercise objects
for item in exercise_data:
    exercise = Exercise(
        id = item["id"],
        title = item["title"],
        image = item["image"],
        name = item["name"],
        explanation = item["explanation"],
        breathing_technique = item["breathing_technique"],
        level = ExerciseLevel(
            beginner = item["level"]["beginner"],
            intermediate = item["level"]["intermediate"],
            advanced = item["level"]["advanced"]
        )
    )
    exercise_list.append(exercise)
    
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/faqs', methods=['GET', 'POST'])
def faqs():
    print(request.method)
    if (request.method == 'POST'):
        question=request.form.get('user-question-text')
        print(question)
        user_question_list.append(question)
        return redirect(url_for('faqs_list'))
    
    return render_template('faqs.html', faq_list=faq_list, user_question_list=user_question_list)

@app.route('/faqs-list')
def faqs_list():
    return render_template('faqs-list.html', faq_list=faq_list, user_question_list=user_question_list)

@app.route('/exercises')
def exercises():
    return render_template('exercises.html', exercise_list=exercise_list)

@app.route('/exercise-detail/<int:exercise_id>')
def exercise_detail(exercise_id):
    return render_template('exercise-detail.html', exercise= exercise_list[exercise_id])

@app.route('/find-your-style')
def find_your_style():
    return render_template('find-your-style.html')

@app.route('/get-in-touch')
def get_in_touch():
    return render_template('get-in-touch.html')
