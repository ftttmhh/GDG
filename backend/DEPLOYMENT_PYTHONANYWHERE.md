# Deploying to PythonAnywhere (Free Tier)

This guide walks you through deploying your Rural TeleHealth Voice AI backend to PythonAnywhere's free tier, which doesn't require any billing information.

## Prerequisites

1. Create a free PythonAnywhere account at [pythonanywhere.com](https://www.pythonanywhere.com/)
2. A Twilio account with a phone number

## Deployment Steps

### 1. Create a PythonAnywhere Account

1. Go to [pythonanywhere.com](https://www.pythonanywhere.com/) and sign up for a free account
2. Complete the registration process

### 2. Upload Your Code

1. From your PythonAnywhere dashboard, click on "Files" in the top menu
2. Create a new directory for your project (e.g., "telehealth")
3. Navigate into your new directory
4. Click "Upload a file" and upload a zip of your backend code
   - Alternatively, you can use the Bash console to clone your repository if it's on GitHub

### 3. Set Up a Virtual Environment

1. Go to the "Consoles" tab and start a new Bash console
2. Navigate to your project directory:
   ```
   cd ~/telehealth
   ```
3. Create a virtual environment:
   ```
   mkvirtualenv --python=python3.9 telehealth-venv
   ```
4. Install your dependencies:
   ```
   pip install -r requirements.txt
   ```

### 4. Create a Web App

1. Go to the "Web" tab and click "Add a new web app"
2. Choose "Manual configuration"
3. Select Python 3.9
4. Enter your project path (e.g., `/home/yourusername/telehealth`)
5. Click "Next"

### 5. Configure WSGI File

1. Click on the WSGI configuration file link (e.g., `/var/www/yourusername_pythonanywhere_com_wsgi.py`)
2. Replace the contents with:
   ```python
   import sys
   import os
   
   # Add your project directory to the sys.path
   path = '/home/yourusername/telehealth'
   if path not in sys.path:
       sys.path.append(path)
   
   # Set environment variables
   os.environ['SECRET_KEY'] = 'your-secret-key'
   os.environ['TWILIO_ACCOUNT_SID'] = 'your-twilio-account-sid'
   os.environ['TWILIO_AUTH_TOKEN'] = 'your-twilio-auth-token'
   os.environ['TWILIO_PHONE_NUMBER'] = 'your-twilio-phone-number'
   
   # Import your app
   from run import app as application
   ```
3. Replace `yourusername` with your actual PythonAnywhere username and update the Twilio credentials
4. Save the file

### 6. Configure Virtual Environment

1. Go back to the "Web" tab
2. Under "Virtualenv", enter the path to your virtual environment:
   ```
   /home/yourusername/.virtualenvs/telehealth-venv
   ```
3. Click "Save"

### 7. Configure Static Files (Optional)

1. Under "Static Files", add the following if you have any static files:
   ```
   URL: /static/
   Directory: /home/yourusername/telehealth/app/static
   ```
2. Click "Save"

### 8. Reload Your Web App

1. Click the "Reload" button for your web app
2. Your app should now be live at `yourusername.pythonanywhere.com`

### 9. Configure Twilio Webhooks

1. Go to the [Twilio Console](https://www.twilio.com/console)
2. Navigate to Phone Numbers → Manage → Active Numbers
3. Select your phone number
4. Under "Voice & Fax", set the webhook URL for incoming calls to:
   ```
   https://yourusername.pythonanywhere.com/call/incoming
   ```
5. Set the HTTP method to POST
6. Save your changes

### 10. Update Your Flutter App

1. Open your Flutter app's main.dart file
2. Update the API URL to point to your PythonAnywhere URL:
   ```dart
   final String apiUrl = "https://yourusername.pythonanywhere.com/api";
   ```
3. Rebuild your Flutter app

## Free Tier Limitations

PythonAnywhere's free tier includes:

- One web app
- Custom domain not available (you'll use yourusername.pythonanywhere.com)
- 512MB storage
- Low CPU priority
- Limited outbound network access (whitelisted sites only, but Twilio is allowed)
- Web app is disabled after 3 months of inactivity (just log in to extend)

## Troubleshooting

If you encounter issues:

1. Check the error logs in the "Web" tab
2. Ensure your virtual environment is correctly set up
3. Verify your WSGI file points to the correct paths
4. Make sure Twilio webhooks are correctly configured
5. If you get a "DisallowedHost" error, add your PythonAnywhere domain to your ALLOWED_HOSTS setting

## Important Notes About PythonAnywhere Free Tier

1. **Whitelisted Sites**: The free tier only allows outbound connections to specific whitelisted sites. Twilio is among these sites, so your app should work with Twilio.

2. **Keep-alive Requirement**: To keep your free web app active, you need to log in at least once every 3 months.

3. **CPU Quota**: The free tier has limited CPU time, which might affect performance during heavy usage.

## Additional Resources

- [PythonAnywhere Help Pages](https://help.pythonanywhere.com/)
- [Twilio Documentation](https://www.twilio.com/docs/voice)
- [Flask on PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/) 