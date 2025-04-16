# VIBATO AI Voice Agent

An intelligent voice call analyzer for inbound communication system, specialized in explaining AI solutions for businesses.

## Features

- Receives and processes Twilio webhook requests
- Analyzes call data to determine customer intent
- Generates appropriate responses in TwiML format
- Tracks customer interest and business information
- Integrates with n8n for workflow automation

## Tech Stack

- Python/Flask
- Twilio
- Vercel (Deployment)
- n8n (Workflow Automation)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/vibato-voice-agent.git
cd vibato-voice-agent
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file with your Twilio credentials:

```
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=your_phone_number
```

## Deployment

The project is deployed on Vercel and connected to this GitHub repository. Any push to the main branch will trigger an automatic deployment.

## Environment Variables

The following environment variables need to be set in Vercel:

- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`
- `TWILIO_PHONE_NUMBER`

## API Endpoints

- `POST /api/analyze`: Main endpoint for call analysis and response generation

## License

MIT
