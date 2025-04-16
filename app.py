from flask import Flask, request, jsonify
from twilio.twiml.voice_response import VoiceResponse
from twilio.rest import Client
from call_analyzer import CallAnalyzer
from response_generator import ResponseGenerator
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)
call_analyzer = CallAnalyzer()
response_generator = ResponseGenerator()

# Initialize Twilio client
twilio_client = Client(
    os.getenv('TWILIO_ACCOUNT_SID'),
    os.getenv('TWILIO_AUTH_TOKEN')
)

@app.route("/api/analyze", methods=['POST'])
def analyze():
    # Get call data from n8n
    call_data = request.json
    
    # Analyze the call
    analysis = call_analyzer.analyze(call_data)
    
    # Generate appropriate response
    response = response_generator.generate_response(analysis)
    
    # Return both the analysis and the TwiML response
    return jsonify({
        "analysis": analysis,
        "twiml": str(response)
    })

# This is needed for Vercel
@app.route("/")
def home():
    return "VIBATO AI Voice Agent is running!"

# This is needed for Vercel
if __name__ == "__main__":
    app.run(debug=True) 