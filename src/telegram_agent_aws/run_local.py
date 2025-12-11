import logging
import asyncio
from telegram import Update
from telegram.ext import Application, TypeHandler
from telegram_agent_aws.config import settings
from telegram_agent_aws.infrastructure.lambda_function import process_update

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def local_handler(update: Update, context):
    """
    Bridge function to forward updates from local polling to the Lambda-style processor.
    """
    try:
        # Convert the Update object to a dictionary (simulating JSON payload)
        update_data = update.to_dict()
        # Call the logic defined in lambda_function.py
        await process_update(update_data)
    except Exception as e:
        logger.error(f"Error processing update locally: {e}")

def main():
    print("Starting local Telegram bot poller...")
    
    # Initialize the Application with the bot token
    application = Application.builder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    # Register a "catch-all" handler that forwards EVERYTHING to our processor
    application.add_handler(TypeHandler(Update, local_handler))
    
    # Start polling
    application.run_polling()

if __name__ == "__main__":
    main()
