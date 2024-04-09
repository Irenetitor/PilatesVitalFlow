from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/faqs')
def faqs():
    faq_data = get_faq_data()
    return render_template('faqs.html', faq_data=faq_data)

@app.route('/nav-item2')
def nav_item2():
    return render_template('nav2.html')

@app.route('/nav-item3')
def nav_item3():
    return render_template('nav3.html')

@app.route('/nav-item4')
def nav_item4():
    return render_template('nav4.html')

# Retrun a list of dictionaries containing FAQ data
def get_faq_data():
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
        # Add more FAQ entries as needed
    ]
    return faq_list