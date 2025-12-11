# Telegram Multimodal Agent

A Telegram bot agent built for AWS Lambda, capable of handling text, voice, and image interactions using OpenAI, Qdrant, and ElevenLabs.

## Prerequisites

- Python 3.12+
- `uv` (recommended) or `pip`

## Setup

1. **Install Dependencies**
   ```bash
   uv sync
   # OR
   pip install .
   ```

2. **Environment Configuration**
   Create a `.env` file in the root directory with the following keys:
   ```env
   OPENAI_API_KEY=sk-...
   ELEVENLABS_API_KEY=...
   TELEGRAM_BOT_TOKEN=...
   MONGODB_CONNECTION_STRING=...
   QDRANT_API_KEY=...
   QDRANT_URL=...
   COMET_API_KEY=...
   ```

## Running Locally

To run the bot locally (polling mode):

```bash
# Set PYTHONPATH to include src
$env:PYTHONPATH="src"

# Run the local runner
python src/telegram_agent_aws/run_local.py
```

## Deployment

The project is designed to be deployed as an AWS Lambda function. The entry point is `telegram_agent_aws.infrastructure.lambda_function.lambda_handler`.
