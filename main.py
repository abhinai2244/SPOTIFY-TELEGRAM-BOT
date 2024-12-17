from telethon import TelegramClient
from decouple import config

# Load BOT_TOKEN from .env file
BOT_TOKEN = config('BOT_TOKEN')

# Set up the Telethon client
CLIENT = TelegramClient('bot', api_id='your_api_id', api_hash='your_api_hash')  # Replace with your API ID and hash

# Main execution
if __name__ == '__main__':
    print('[BOT] Starting...')
    
    # Use the bot token to start the client
    CLIENT.start(bot_token=BOT_TOKEN)
    CLIENT.run_until_disconnected()

    print(f"Bot started with token: {BOT_TOKEN}")  # This will print the bot token if .env is loaded correctly
