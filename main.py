from flask import Flask
import threading
import os
import requests
import random
import pyfiglet
import sys
import time
from random import randint
from user_agent import generate_user_agent as ua

# --- FLASK SERVER FOR RENDER ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

# Background thread taaki bot aur server dono chalein
threading.Thread(target=run).start()

# --- BOT LOGIC ---
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
ab = pyfiglet.figlet_format("TELEGRAM REPORT")
print('\033[1;32m' + ab)

def R(m, email, num):
    try:
        res = requests.get('https://telegram.org/support', headers={"User-Agent": ua()}).cookies
        stel = res.get('stel_ssid', '')
        data = f'message={m}&email={email}&phone={num}&setln='
        
        req = requests.post('https://telegram.org/support', data=data, headers={
            "Host": "telegram.org",
            "origin": "https://telegram.org",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": ua(),
            "referer": "https://telegram.org/support",
            "cookie": f"stel_ssid={stel}"
        }).text
        
        if "Thanks" in req:
            print(f'{G}[√] REPORT SUCCESS | FROM: {email}')
        else:
            print(f"{E}[!] Telegram limit or Error")
    except Exception as e:
        print(f"Connection Error: {e}")

# Render Dashboard se username uthayega
target_user = os.environ.get("TARGET_USERNAME", "@Telegram") 

m_text = f"""Hello sir/ma'am,
I would like to report a Telegram user who is engaging in suspicious and harmful activities. 
Their username is {target_user}. I believe they may be involved in scams and phishing.
Thank you."""

names = ["Rakesh","Aman","Neha","Rahul","Dev","Ankit","Karan","Mohit"]

print(f"{G}Starting Mass Report on: {target_user}...")

while True:
    num = f"+91{randint(7000000000, 9999999999)}"
    email = f'{random.choice(names).lower()}{randint(100, 9999)}@gmail.com'
    R(m_text, email, num)
    time.sleep(2) # 2 second ka gap taaki IP ban na ho
