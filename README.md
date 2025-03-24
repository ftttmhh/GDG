# Rural TeleHealth Voice-based AI System

A voice-based AI system that allows people to call a toll-free number and get automated health advice in their native language, designed for underserved rural communities.

## Project Overview

This project consists of two main components:

1. **Flutter Mobile App** - A user-friendly mobile interface for accessing health advice
2. **Flask Backend** - A robust server that powers the voice-based AI health advisory system

The system is designed with accessibility in mind, allowing users to:
- Call a toll-free number and interact in their native language
- Get health advice through voice interaction
- Use the mobile app to get text-based health advice

## Features

- **Multilingual Support**: English, Hindi, Tamil, and Telugu
- **Voice-based Interaction**: Users can speak naturally to describe their health concerns
- **Automated Health Advice**: System provides relevant health suggestions based on symptoms described
- **Toll-free Access**: Accessible via a regular phone call without internet requirements
- **Mobile App Integration**: Additional interface option for those with smartphones

## Technical Architecture

### Flutter Mobile App
- Located in the `telehealth_mvp/` directory
- Provides a GUI for text-based interaction
- Connects to the backend API for health advice
- Includes direct call functionality to the toll-free number

### Flask Backend
- Located in the `backend/` directory
- Handles Twilio webhook integration for phone calls
- Processes voice inputs and converts speech to text
- Provides language detection and translation services
- Generates health advice based on user concerns
- Exposes API endpoints for the mobile app integration

## Setup Instructions

### Prerequisites
- Flutter SDK
- Python 3.8+
- Twilio account with a phone number

### Backend Setup
1. Navigate to the backend directory:
   ```
   cd backend
   ```
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Set up environment variables:
   ```
   cp .env.example .env
   ```
   Then edit the `.env` file with your Twilio credentials
6. Run the server:
   ```
   python run.py
   ```

### Flutter App Setup
1. Navigate to the Flutter app directory:
   ```
   cd telehealth_mvp
   ```
2. Install dependencies:
   ```
   flutter pub get
   ```
3. Update the API URL in `lib/main.dart` to point to your backend server
4. Run the app:
   ```
   flutter run
   ```

## Deployment Considerations

### Backend Deployment
- Deploy to a cloud provider (AWS, Google Cloud, etc.)
- Set up HTTPS with SSL certificates
- Configure Twilio webhooks to point to your deployed backend
- Implement proper logging and monitoring

### Mobile App Deployment
- Update API endpoints to production URLs
- Build release versions:
  ```
  flutter build apk --release
  flutter build ios --release
  ```
- Submit to app stores or distribute through appropriate channels

## For Rural Communities
- Consider offline capabilities for areas with limited internet
- Optimize app size for devices with limited storage
- Ensure voice prompts are clear and use simple language
- Provide educational resources about common health concerns

## Future Enhancements
- Add more regional languages
- Implement more sophisticated health advisory system
- Include emergency service connections
- Develop community health worker dashboards 