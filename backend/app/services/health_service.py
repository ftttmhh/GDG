import logging
import re

# Define common health concerns and predefined responses for the MVP
HEALTH_RESPONSES = {
    "fever": "For fever, get plenty of rest, stay hydrated, and take acetaminophen or ibuprofen as directed. If the fever persists for more than 3 days or exceeds 102.2°F (39°C), please see a healthcare provider.",
    
    "headache": "For headaches, rest in a quiet dark room, try cold or hot compresses, and take over-the-counter pain relievers like acetaminophen if needed. If headaches are severe, sudden, or accompanied by other symptoms, seek medical attention.",
    
    "cold": "For common cold, rest, drink fluids, use saline nasal spray, and take over-the-counter cold medications to ease symptoms. If symptoms worsen after a week or you develop a high fever, see a healthcare provider.",
    
    "cough": "For coughs, stay hydrated, use honey (if over 1 year old), try cough drops, and use a humidifier. If coughing persists for more than 2 weeks or is accompanied by wheezing or difficulty breathing, seek medical attention.",
    
    "stomach pain": "For stomach pain, try eating bland foods, staying hydrated, and avoiding spicy or fatty foods. Use antacids if appropriate. If pain is severe, persistent, or accompanied by vomiting or fever, seek medical attention.",
    
    "diarrhea": "For diarrhea, stay well-hydrated with water, clear broths, and electrolyte solutions. Eat bland, easy-to-digest foods. If diarrhea persists for more than 2 days or is accompanied by severe pain, high fever, or bloody stools, see a healthcare provider.",
    
    "vomiting": "For vomiting, avoid eating solid foods for a few hours, sip small amounts of clear fluids, then gradually reintroduce bland foods. If vomiting persists for more than 24 hours or is accompanied by severe pain or signs of dehydration, seek medical attention.",
    
    "rash": "For rashes, keep the area clean and dry, avoid scratching, and try calamine lotion or hydrocortisone cream for itching. If the rash is widespread, painful, or accompanied by fever or other symptoms, see a healthcare provider.",
    
    "injury": "For minor injuries like cuts or scrapes, clean the wound with soap and water, apply antibiotic ointment, and cover with a clean bandage. For deeper wounds, heavy bleeding, or signs of infection, seek medical attention.",
    
    "breathing": "For breathing difficulties, sit upright, try to stay calm, and remove any triggers like allergens. If you experience severe shortness of breath, bluish lips, or chest pain, seek emergency medical attention immediately.",
    
    "pregnancy": "For pregnancy-related concerns, ensure you're taking prenatal vitamins, staying hydrated, and getting adequate rest. For any unusual symptoms like severe abdominal pain, bleeding, or reduced fetal movement, contact your healthcare provider immediately."
}

# Default response when no matching concern is found
DEFAULT_RESPONSE = "Based on your description, I recommend consulting with a healthcare provider for proper diagnosis and treatment. In the meantime, ensure you're getting adequate rest and staying hydrated. If your symptoms worsen or you experience severe pain, please seek medical attention promptly."

def get_health_advice(query):
    """
    Get health advice based on the user's query.
    
    Args:
        query (str): The health concern described by the user
        
    Returns:
        str: Health advice related to the concern
    """
    try:
        # Normalize query: convert to lowercase and remove punctuation
        normalized_query = re.sub(r'[^\w\s]', '', query.lower())
        
        # Check for keyword matches in our predefined responses
        for keyword, response in HEALTH_RESPONSES.items():
            if keyword in normalized_query:
                return response
                
        return DEFAULT_RESPONSE
            
    except Exception as e:
        logging.error(f"Health advice error: {str(e)}")
        return DEFAULT_RESPONSE 