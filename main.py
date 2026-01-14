import os
from telethon import TelegramClient, functions, types
import time

# Secrets se details uthayega
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']
target = os.environ['TARGET_USERNAME']

# Bot login setup
client = TelegramClient('session_name', api_id, api_hash)

async def main():
    print(f"Bot started! Reporting: {target}")
    while True:
        try:
            # Ye command Telegram ko asli report bhejti hai
            await client(functions.account.ReportPeerRequest(
                peer=target,
                reason=types.InputReportReasonSpam(),
                message='This user is spreading scams and phishing links.'
            ))
            print(f"Successfully Reported: {target}")
        except Exception as e:
            print(f"Error occurred: {e}")
            break # Agar block hai toh stop ho jayega
        
        time.sleep(60) # Har 1 minute mein 1 report (Safe limit)

with client:
    client.loop.run_until_complete(main())
    
