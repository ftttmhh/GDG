from flask import Blueprint, request, current_app, url_for
from twilio.twiml.voice_response import VoiceResponse, Gather
from app.services.language_service import detect_language, translate_text
from app.services.health_service import get_health_advice

bp = Blueprint('call', __name__, url_prefix='/call')

@bp.route('/incoming', methods=['POST'])
def incoming_call():
    """Handle incoming calls and prompt for language selection"""
    response = VoiceResponse()
    
    # Initial greeting (English as default)
    response.say("Welcome to the Rural Health Advisory Service. " 
                "Please press 1 for English, 2 for Hindi, 3 for Tamil, 4 for Telugu.",
                voice='alice')
    
    # Create a gather with options
    gather = Gather(num_digits=1, action=url_for('call.language_selected'), 
                    timeout=10, method='POST')
    
    # Add Hindi prompt
    gather.say("हिंदी के लिए 2 दबाएं", language='hi-IN')
    
    # Add Tamil prompt
    gather.say("தமிழுக்கு 3 ஐ அழுத்தவும்", language='ta-IN')
    
    # Add Telugu prompt
    gather.say("తెలుగు కోసం 4 నొక్కండి", language='te-IN')
    
    response.append(gather)
    
    # If no input, retry
    response.redirect(url_for('call.incoming'))
    
    return str(response)

@bp.route('/language', methods=['POST'])
def language_selected():
    """Handle language selection and prompt for health concern"""
    digit_pressed = request.form.get('Digits', None)
    response = VoiceResponse()
    
    language_map = {
        '1': 'en',  # English
        '2': 'hi',  # Hindi
        '3': 'ta',  # Tamil
        '4': 'te',  # Telugu
    }
    
    if digit_pressed in language_map:
        language = language_map[digit_pressed]
        
        # Save the language choice in the session (we'll use Twilio cookies as we can't use Flask sessions)
        # In a production app, you would store this in a database with the call SID
        
        # Ask for health concerns in the selected language
        gather = Gather(input='speech', action=url_for('call.health_concern', language=language),
                       timeout=5, method='POST')
        
        if language == 'en':
            gather.say("Please describe your health concern.", voice='alice')
        elif language == 'hi':
            gather.say("कृपया अपनी स्वास्थ्य चिंता का वर्णन करें।", language='hi-IN')
        elif language == 'ta':
            gather.say("உங்கள் உடல்நல கவலையை விவரிக்கவும்.", language='ta-IN')
        elif language == 'te':
            gather.say("దయచేసి మీ ఆరోగ్య సమస్యను వివరించండి.", language='te-IN')
        
        response.append(gather)
        
        # If no input, retry
        response.redirect(url_for('call.language_selected'))
    else:
        # Invalid option, redirect to start
        response.say("Invalid option. Let's try again.", voice='alice')
        response.redirect(url_for('call.incoming'))
    
    return str(response)

@bp.route('/health-concern/<language>', methods=['POST'])
def health_concern(language):
    """Process spoken health concern and provide advice"""
    response = VoiceResponse()
    
    # Get the speech input
    speech_result = request.form.get('SpeechResult', '')
    
    if speech_result:
        # Translate to English if not already in English
        if language != 'en':
            english_text = translate_text(speech_result, source=language, target='en')
        else:
            english_text = speech_result
        
        # Get health advice based on the concern
        advice = get_health_advice(english_text)
        
        # Translate advice back to the selected language
        if language != 'en':
            translated_advice = translate_text(advice, source='en', target=language)
        else:
            translated_advice = advice
        
        # Speak the advice in the appropriate language
        lang_voice_map = {
            'en': 'alice',
            'hi': 'hi-IN',
            'ta': 'ta-IN',
            'te': 'te-IN'
        }
        
        response.say(translated_advice, voice=lang_voice_map.get('en', 'alice'), 
                    language=lang_voice_map.get(language))
        
        # Ask if they have another question
        gather = Gather(num_digits=1, action=url_for('call.another_question', language=language),
                       timeout=5, method='POST')
        
        if language == 'en':
            gather.say("Press 1 if you have another question, or 2 to end the call.", voice='alice')
        elif language == 'hi':
            gather.say("यदि आपका कोई अन्य प्रश्न है तो 1 दबाएं, या कॉल समाप्त करने के लिए 2 दबाएं।", language='hi-IN')
        elif language == 'ta':
            gather.say("உங்களிடம் வேறு கேள்வி இருந்தால் 1 ஐ அழுத்தவும், அல்லது அழைப்பை முடிக்க 2 ஐ அழுத்தவும்.", language='ta-IN')
        elif language == 'te':
            gather.say("మీకు మరొక ప్రశ్న ఉంటే 1 నొక్కండి, లేదా కాల్ ముగించడానికి 2 నొక్కండి.", language='te-IN')
        
        response.append(gather)
    else:
        # No speech detected
        if language == 'en':
            response.say("I'm sorry, I didn't hear anything. Let's try again.", voice='alice')
        elif language == 'hi':
            response.say("क्षमा करें, मुझे कुछ सुनाई नहीं दिया। फिर से कोशिश करते हैं।", language='hi-IN')
        elif language == 'ta':
            response.say("மன்னிக்கவும், எனக்கு எதுவும் கேட்கவில்லை. மீண்டும் முயற்சிப்போம்.", language='ta-IN')
        elif language == 'te':
            response.say("క్షమించండి, నాకు ఏమీ వినిపించలేదు. మళ్ళీ ప్రయత్నిద్దాం.", language='te-IN')
        
        # Redirect back to get health concern
        gather = Gather(input='speech', action=url_for('call.health_concern', language=language),
                       timeout=5, method='POST')
        response.append(gather)
    
    return str(response)

@bp.route('/another-question/<language>', methods=['POST'])
def another_question(language):
    """Handle request for another question or end call"""
    digit_pressed = request.form.get('Digits', None)
    response = VoiceResponse()
    
    if digit_pressed == '1':
        # Another question - go back to health concern gathering
        gather = Gather(input='speech', action=url_for('call.health_concern', language=language),
                       timeout=5, method='POST')
        
        if language == 'en':
            gather.say("Please describe your health concern.", voice='alice')
        elif language == 'hi':
            gather.say("कृपया अपनी स्वास्थ्य चिंता का वर्णन करें।", language='hi-IN')
        elif language == 'ta':
            gather.say("உங்கள் உடல்நல கவலையை விவரிக்கவும்.", language='ta-IN')
        elif language == 'te':
            gather.say("దయచేసి మీ ఆరోగ్య సమస్యను వివరించండి.", language='te-IN')
        
        response.append(gather)
    else:
        # End call with goodbye message
        if language == 'en':
            response.say("Thank you for using our health advisory service. Goodbye!", voice='alice')
        elif language == 'hi':
            response.say("हमारी स्वास्थ्य सलाह सेवा का उपयोग करने के लिए धन्यवाद। अलविदा!", language='hi-IN')
        elif language == 'ta':
            response.say("எங்கள் சுகாதார ஆலோசனை சேவையைப் பயன்படுத்தியதற்கு நன்றி. வணக்கம்!", language='ta-IN')
        elif language == 'te':
            response.say("మా ఆరోగ్య సలహా సేవను ఉపయోగించినందుకు ధన్యవాదాలు. వీడ్కోలు!", language='te-IN')
        
        response.hangup()
    
    return str(response) 