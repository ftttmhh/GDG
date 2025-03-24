# Rural Telehealth Backend

This is the Flask backend for the Rural Telehealth Voice-based AI system that allows people to call a toll-free number and get automated health advice in their native language.

## Features

- Voice-based health advice via Twilio integration
- Multi-language support (English, Hindi, Tamil, Telugu)
- Automatic language detection
- Translation services
- REST API for integration with the Flutter mobile app

## Setup Instructions

1. Clone the repository
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Copy the `.env.example` file to `.env` and update with your configuration:
   ```
   cp .env.example .env
   ```
6. Update the `.env` file with your Twilio credentials

## Running the Application

```
python run.py
```

The application will be available at http://localhost:5000

## API Endpoints

### Health Advice API

```
POST /api/health-advice
```

Request body:
```json
{
  "query": "I have a fever and headache",
  "language": "en"  // Optional, defaults to 'en', can be 'auto' for detection
}
```

### Language API

```
GET /api/languages
```

Returns a list of supported languages.

### Translation API

```
POST /api/translate
```

Request body:
```json
{
  "text": "Text to translate",
  "source": "en",  // Optional, defaults to 'auto'
  "target": "hi"   // Required
}
```

## Twilio Integration

The application includes Twilio webhook handlers for interactive voice response:

- `/call/incoming`: Handles incoming calls and language selection
- `/call/language`: Processes language selection
- `/call/health-concern/<language>`: Processes speech input for health concerns
- `/call/another-question/<language>`: Handles additional questions

## Production Deployment

For production deployment, consider:

1. Using a production WSGI server like Gunicorn
2. Setting up proper SSL certificates
3. Implementing proper monitoring and error handling
4. Ensuring environment variables are securely managed 