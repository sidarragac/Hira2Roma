from flask import current_app, render_template
from utils.image_predictor import ImagePredictor
from utils.image_processor import ImageProcessor
from utils.transliterator import Transliterator

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def translate_char():
    return render_template('translate_char.html')

def process_char(image):
    if not allowed_file(image.filename):
        return {'error': 'Tipo de archivo no permitido'}, 400

    predictor = ImagePredictor()
    transliterator = Transliterator()

    predicted_char = predictor.predict_image(image)
    romanized_char = transliterator.transliterate(predicted_char)

    viewdata = {}
    viewdata['predicted_char'] = predicted_char
    viewdata['romanized_char'] = romanized_char

    return render_template('processed_char.html', viewdata=viewdata)

def translate_text():
    return render_template('translate_text.html')
