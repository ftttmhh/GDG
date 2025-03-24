from flask import Blueprint, request, jsonify, current_app
from app.services.health_service import get_health_advice
from app.services.language_service import detect_language, translate_text

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/health-advice', methods=['POST'])
def health_advice():
    """Get health advice based on the user's query and language preference"""
    data = request.get_json()
    
    if not data or 'query' not in data:
        return jsonify({'error': 'Query is required'}), 400
    
    query = data.get('query')
    language = data.get('language', 'en')
    
    try:
        # If language is not specified, try to detect it
        if not language or language == 'auto':
            detected_language = detect_language(query)
            language = detected_language
        
        # Translate to English if not already in English
        if language != 'en':
            english_query = translate_text(query, source=language, target='en')
        else:
            english_query = query
        
        # Get health advice
        advice = get_health_advice(english_query)
        
        # Translate advice back to the original language if needed
        if language != 'en':
            translated_advice = translate_text(advice, source='en', target=language)
            response = {
                'query': query,
                'detected_language': language,
                'advice': translated_advice,
                'original_advice': advice  # Include original English advice for reference
            }
        else:
            response = {
                'query': query,
                'detected_language': language,
                'advice': advice
            }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bp.route('/languages', methods=['GET'])
def get_languages():
    """Get a list of supported languages"""
    languages = [
        {'code': 'en', 'name': 'English'},
        {'code': 'hi', 'name': 'Hindi (हिन्दी)'},
        {'code': 'ta', 'name': 'Tamil (தமிழ்)'},
        {'code': 'te', 'name': 'Telugu (తెలుగు)'}
    ]
    
    return jsonify({'languages': languages})

@bp.route('/translate', methods=['POST'])
def translate():
    """Translate text between languages"""
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Text is required'}), 400
    
    text = data.get('text')
    source = data.get('source', 'auto')
    target = data.get('target', 'en')
    
    try:
        # If source is auto, detect the language
        if source == 'auto':
            detected_language = detect_language(text)
            source = detected_language
        
        # Translate the text
        translated_text = translate_text(text, source=source, target=target)
        
        response = {
            'original_text': text,
            'translated_text': translated_text,
            'source_language': source,
            'target_language': target
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500 