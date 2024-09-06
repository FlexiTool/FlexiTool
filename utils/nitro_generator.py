import concurrent.futures
import json
import requests
import random
import string
import time
from datetime import datetime
import os
from pystyle import Colors

def main():
    clear()
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_error(message):
        print(f"Error: {message}")

    class DiscordNitroGenerator:
        def __init__(self):
            self.webhook_url = None
            self.threads_number = None
            self.username_webhook = "Your Webhook Username"
            self.avatar_webhook = "Your Webhook Avatar URL"
            self.color_webhook = 0x00ff00  # Green color

        def get_webhook_url(self):
            while True:
                webhook_input = input(f"{datetime.now().strftime('%H:%M:%S')} Enter Webhook URL (y/n): ")
                if webhook_input.lower() == 'y':
                    self.webhook_url = input(f"{datetime.now().strftime('%H:%M:%S')} Enter Webhook URL: ")
                    break
                elif webhook_input.lower() == 'n':
                    print("Webhook URL not provided.")
                    break
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")

        def get_threads_number(self):
            while True:
                try:
                    self.threads_number = int(input(f"{datetime.now().strftime('%H:%M:%S')} Enter threads number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        def send_webhook(self, nitro_url):
            payload = {
                "embeds": [
                    {
                        "title": "Nitro Valid !",
                        "description": f"**Nitro:**\n```{nitro_url}```",
                        "color": self.color_webhook,
                        "footer": {
                            "text": self.username_webhook,
                            "icon_url": self.avatar_webhook,
                        }
                    }
                ],
                "username": self.username_webhook,
                "avatar_url": self.avatar_webhook
            }

            headers = {
                "Content-Type": "application/json"
            }

            requests.post(self.webhook_url, json=payload, headers=headers)

        def check_nitro(self, nitro_code):
            nitro_url = f"https://discord.gift/{nitro_code}"
            response = requests.get(f"https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true", timeout=1)
            if response.status_code == 200:
                if self.webhook_url:
                    self.send_webhook(nitro_url)
                print(f"{datetime.now().strftime('%H:%M:%S')} Status: Valid  Nitro: {nitro_url}")
            else:
                print(f"{datetime.now().strftime('%H:%M:%S')} Status: Invalid Nitro: {nitro_url}")

        def generate_nitro(self):
            with concurrent.futures.ThreadPoolExecutor(max_workers=self.threads_number) as executor:
                while True:
                    nitro_code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
                    executor.submit(self.check_nitro, nitro_code)

if __name__ == "__main__":
    generator = DiscordNitroGenerator()
    generator.get_webhook_url()
    generator.get_threads_number()
    generator.generate_nitro()