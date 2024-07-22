from flask import Flask, request, jsonify
from email_generator import EmailGenerator
from typing import List
import json
import yaml

with open("config.yaml", "r") as config:
    config = yaml.safe_load(config)


# Initialize Flask application
app = Flask(__name__)

# Create an instance of EmailGenerator
email_generator = EmailGenerator(**config)

# Define the Flask route for generating emails
@app.route('/generate_email', methods=['POST'])
def generate_email():
    data = request.json
    topic = data.get('topic')
    description = data.get('description')

    # Validate the required fields
    if not topic or not description:
        return jsonify({"error": "Topic and description are required."}), 400

    # Generate the email and return the result
    response = email_generator.generate(topic, description)
    return jsonify(response), 200

# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000, debug=True)
