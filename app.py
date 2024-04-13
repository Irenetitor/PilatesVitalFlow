from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_question_list = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/faqs', methods=['GET', 'POST'])
def faqs():
    faq_list = get_faq_list()
    print(request.method)
    if (request.method == 'POST'):
        question=request.form.get('user-question-text')
        print(question)
        user_question_list.append(question)
        return redirect(url_for('faqs_list'))
    
    return render_template('faqs.html', faq_list=faq_list, user_question_list=user_question_list)

@app.route('/faqs-list')
def faqs_list():
    faq_list = get_faq_list()
    return render_template('faqs-list.html', faq_list=faq_list, user_question_list=user_question_list)

@app.route('/exercises')
def exercises():
    return render_template('exercises.html')

@app.route('/find-your-style')
def find_your_style():
    return render_template('find-your-style.html')

@app.route('/get-in-touch')
def get_in_touch():
    return render_template('getintouch.html')

# Return a list of dictionary containing FAQ data
def get_faq_list():
    faq_list = [
        {   
            'question': 'For whom is Pilates suitable??', 
            'answer': 'Pilates is suitable for a wide range of individuals, including beginners, athletes, and those recovering from injuries. It focuses on core strength, flexibility, and overall body awareness.'
        },
        {
            'question': 'How is Pilates different from yoga?', 
            'answer': 'While both Pilates and yoga emphasize mind-body connection, Pilates primarily focuses on strengthening the core muscles and improving posture. Yoga, on the other hand, incorporates various postures (asanas),breathing techniques, and meditation.'
        },
        {
            'question': 'How often do I need to practice Pilates to feel an effect?', 
            'answer': 'Consistent practice is essential. Aim for at least 2-3 sessions per week to experience the benefits. Regularity is key to improving strength, flexibility and alignment.'
        },
        {
            'question': 'Can I lose weight with Pilates?', 
            'answer': 'Pilates alone may not lead to significant weight loss, but it can complement a healthy lifestyle. It improves muscle tone, which can indirectly contribute to weight management.'
        },
        {
            'question': 'Does Pilates help with back pain?', 
            'answer': 'Yes, Pilates can be effective in alleviating back pain. It strengthens the core and promotes better spinal alignment, reducing strain on the back.'
        },
        {
            'question': 'Does Pilates help with shoulder pain?', 
            'answer': 'Pilates exercises can enhance shoulder stability and mobility. Consult with a qualified instructor to address specific shoulder issues.'
        },
        {
            'question': 'Can I train my pelvic floor with Pilates?', 
            'answer': 'Absolutely! Pilates emphasizes pelvic floor engagement during exercises, promoting better pelvic health and stability.'
        }
    ]
    return faq_list