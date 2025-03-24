from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    # Configure app
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', 'dev'),
        TWILIO_ACCOUNT_SID=os.environ.get('TWILIO_ACCOUNT_SID'),
        TWILIO_AUTH_TOKEN=os.environ.get('TWILIO_AUTH_TOKEN'),
        TWILIO_PHONE_NUMBER=os.environ.get('TWILIO_PHONE_NUMBER'),
    )
    
    # Fix for PythonAnywhere hosting - handle proxies correctly
    app.wsgi_app = ProxyFix(app.wsgi_app)
    
    # Register blueprints
    from app.routes import call_routes, api_routes
    app.register_blueprint(call_routes.bp)
    app.register_blueprint(api_routes.bp)
    
    return app

# Import ProxyFix for handling proxy servers (like PythonAnywhere)
from werkzeug.middleware.proxy_fix import ProxyFix 