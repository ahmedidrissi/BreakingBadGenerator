from flask import Blueprint, render_template, request
from website import generator
from website import speaker
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])

def home():
    image = ''

    if request.method == 'GET':
        image = 'img/bg-img4.jpg'

    elif request.method == 'POST':
        text_input = request.form.get('textInput')
        if text_input != '':
            generate_image(text_input)        
            image = 'img/result.jpg'
        else:
            image = 'img/bg-img4.jpg'
        
    return render_template("index.html", background=image)

@views.route('/clear-image', methods=['POST'])
def clear_image():
    image = 'img/bg-img4.jpeg'
    return render_template("index.html", background=image)

def generate_image(text):
    bbg = generator.BreakingBadGenerator(text, "website/static/img/bg-img4.jpg")
    bbg.createImage()

def speak(text):
    speaker.Speaker(text, None).speak()