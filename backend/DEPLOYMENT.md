# Deploying to Google App Engine

This guide walks you through deploying the Rural TeleHealth Voice AI backend to Google App Engine.

## Prerequisites

1. A Google Cloud Platform (GCP) account
2. Google Cloud SDK installed on your computer
3. A Twilio account with a phone number

## Steps to Deploy

### 1. Set Up Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable billing for your project (required for App Engine)
4. Enable the App Engine API

### 2. Install Google Cloud SDK

If you haven't already installed the Google Cloud SDK, follow the [installation instructions](https://cloud.google.com/sdk/docs/install) for your operating system.

### 3. Configure Your App

1. Open the `app.yaml` file and update the environment variables with your actual Twilio credentials:
   ```yaml
   env_variables:
     SECRET_KEY: "your-actual-secret-key"
     TWILIO_ACCOUNT_SID: "your-actual-twilio-sid"
     TWILIO_AUTH_TOKEN: "your-actual-twilio-token"
     TWILIO_PHONE_NUMBER: "your-actual-twilio-number"
   ```

### 4. Deploy to App Engine

1. Open a terminal and navigate to your project's backend directory:
   ```
   cd path/to/your/backend
   ```

2. Initialize your Google Cloud project:
   ```
   gcloud init
   ```
   
   Follow the prompts to select your project and set up your configuration.

3. Deploy your application:
   ```
   gcloud app deploy
   ```

4. After deployment completes, view your application:
   ```
   gcloud app browse
   ```

### 5. Configure Twilio Webhooks

1. Go to the [Twilio Console](https://www.twilio.com/console)
2. Navigate to Phone Numbers → Manage → Active Numbers
3. Select your phone number
4. Under "Voice & Fax", set the webhook URL for incoming calls to:
   ```
   https://your-app-id.appspot.com/call/incoming
   ```
   Where `your-app-id` is your Google App Engine application ID.
5. Set the HTTP method to POST
6. Save your changes

## Free Tier Limitations

Google App Engine's free tier includes:

- 28 instance hours per day (enough for one F1 instance running continuously)
- 5GB of storage
- 1GB of outbound data per day

This should be sufficient for testing and low-volume usage, but be aware that exceeding these limits will incur charges.

## Monitoring Your Application

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Select your project
3. Navigate to App Engine → Dashboard to view your application's performance
4. For logs, go to Logging → Logs Explorer

## Troubleshooting

If you encounter issues:

1. Check the application logs in the Google Cloud Console
2. Verify your environment variables are set correctly
3. Make sure you've enabled billing for your project
4. Ensure your Twilio webhook URLs are correctly configured

## Additional Resources

- [Google App Engine Documentation](https://cloud.google.com/appengine/docs)
- [Twilio Documentation](https://www.twilio.com/docs/voice)
- [Google Cloud SDK Documentation](https://cloud.google.com/sdk/docs) 