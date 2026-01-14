import os
import requests
import random
import time
from random import randint
from user_agent import generate_user_agent as ua

def report_bot():
    # Target username Secret se uthayega
    target = os.environ.get('TARGET_USERNAME', '@Telegram')
    
    names = ["Rakesh", "Aman", "Neha", "Rahul", "Dev", "Ankit", "Karan", "Mohit"]
    
    print(f"--- Mass Reporting Started on {target} ---")

    while True:
        try:
            email = f'{random.choice(names).lower()}{randint(1000, 9999)}@gmail.com'
            phone = f"+91{randint(7000000000, 9999999999)}"
            
            msg = f"Hello Telegram Support, I want to report {target} for scamming and spreading harmful content. Please take action."

            # Session create karna (Real browser feel)
            session = requests.Session()
            res = session.get('https://telegram.org/support', headers={"User-Agent": ua()})
            stel = res.cookies.get('stel_ssid', '')

            data = {
                'message': msg,
                'email': email,
                'phone': phone,
                'setln': ''
            }

            headers = {
                "User-Agent": ua(),
                "Referer": "https://telegram.org/support",
                "Origin": "https://telegram.org"
            }

            response = session.post('https://telegram.org/support', data=data, headers=headers)

            if "Thanks" in response.text:
                print(f"[√] Success: Report sent from {email}")
            else:
                print("[!] Error: Rate limited. Waiting 30 seconds...")
                time.sleep(30) # Block hone par lamba wait

            # Har report ke baad random gap (Insaan jaisa behavior)
            time.sleep(randint(5, 15))

        except Exception as e:
            print(f"Network Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    report_bot()
    
