from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App Engine,
    # a webserver process such as Gunicorn will serve the app.
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port) 