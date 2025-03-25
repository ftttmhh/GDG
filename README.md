# Telehealth Voice Assistant

A voice-based telehealth assistant that allows users to describe their health concerns and receive preliminary medical advice. The system uses Twilio for voice calls and implements a callback mechanism for user interactions.

## Features

- **Voice Call Handling**: Users can call and describe their health concerns
- **Callback System**: Supports requesting callbacks for later consultations
- **Speech Recognition**: Converts user's voice input to text
- **Medical Response System**: Provides preliminary medical advice based on user symptoms
- **Error Handling**: Robust error handling for network issues and service interruptions

## Technical Stack

### Backend (Python)
- Flask: Web framework for the backend API
- Twilio: For voice call handling and callbacks
- PocketSphinx: For speech recognition (currently being upgraded)
- Medicine-LLM: For generating medical advice (in development)

### Frontend (Flutter)
- Flutter SDK: For cross-platform mobile app development
- HTTP package: For API communication
- Platform-specific packages for call handling

### Dependencies
- Python 3.10+
- Flutter SDK
- Flask
- Twilio
- SpeechRecognition
- PyDub (for audio processing)
- PocketSphinx
- Transformers (for LLM integration)
- PyTorch

## Setup

1. Clone the repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - `TWILIO_ACCOUNT_SID`
   - `TWILIO_AUTH_TOKEN`
   - `TWILIO_PHONE_NUMBER`

4. Install Flutter dependencies:
   ```bash
   cd telehealth_mvp
   flutter pub get
   ```

## Project Structure

```
├── telehealth_mvp/        # Flutter mobile application
│   ├── lib/              # Flutter source code
│   ├── android/          # Android-specific files
│   ├── ios/              # iOS-specific files
│   └── pubspec.yaml      # Flutter dependencies
│
├── backend/              # Python Flask backend
│   └── app.py           # Main Flask application
│
├── requirements.txt      # Python dependencies
└── README.md            # Project documentation
```

## Current Status

- ✅ Basic call handling implemented
- ✅ Callback system working
- ✅ Basic speech recognition implemented
- 🔄 Upgrading speech recognition for better accuracy
- 🔄 Implementing advanced medical response system

## Known Issues & Future Improvements

1. Speech Recognition Accuracy
   - Current PocketSphinx implementation has accuracy limitations
   - Planning to upgrade to more accurate cloud-based solutions

2. Medical Response System
   - Currently using template-based responses
   - Working on integrating advanced LLM for better medical advice

## Security & Compliance

- All medical advice includes disclaimers
- No personal health information is stored
- Calls are handled securely through Twilio
