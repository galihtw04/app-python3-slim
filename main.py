from flask import Flask, request, render_template
import logging

# Create a Flask application instance
sample = Flask(__name__)

# Set up logging
logging.basicConfig(filename='./logs/app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

@sample.route("/")
def main():
    # Log the request
    sample.logger.info('Main route accessed')
    return render_template("index.html")

    if __name__ == "__main__":
    # Log that the app is starting
       sample.logger.info('Starting the Flask app')
       sample.run(host="0.0.0.0", port=8080)
