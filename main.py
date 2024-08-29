import os
import sys
import socket
from pystyle import Colors, Cursor, System, Anime, Center, Colorate

sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from ip_info import get_ip_info
from get_ip import main as get_ip_main
from token_decrypt import decrypt_token
from token_checker import main as token_checker_main
from token_info import display_discord_info
from badge_changer import main as badge_changer_main
from status_rotator import status_changer
from server_info import server_lookup
from webhook_info import info_webhook
from webhook_spammer import webhookspam
from scrapper_proxy import get_proxies  
from email_info import main as email_info_main
from instagram_user_info import main as instagram_user_info_main  
from number_info import main as number_info_main 
from auto_login import main as auto_login_main
from token_generator import main as token_generator_main 
from website_info import main as website_info_main
from token_massdm import execute_mass_dm

from ToolBuilder import interfaces

class colors:
    red = '[38;2;255;0;0m'
    orange = '[38;2;255;165;0m'
    green = '[38;2;100;255;100m'
    black = '[38;2;0;0;0m'
    pink = '[38;2;255;0;255m'
    purple = '[38;2;113;41;255m'
    blue = '[38;2;92;120;255m'
    white = '[38;2;255;255;255m'
    gray = '[38;2;200;200;200m'
    light_gray = '[38;2;150;150;150m'

watermark = '''
___________.__                ._____________           .__   
\_   _____/|  |   ____ ___  __|__\__    ___/___   ____ |  |  
 |    __)  |  | _/ __ \\  \/  /  | |    | /  _ \ /  _ \|  |  
 |     \   |  |_\  ___/ >    <|  | |    |(  <_> |  <_> )  |__
 \___  /   |____/\___  >__/\_ \__| |____| \____/ \____/|____/
     \/              \/      \/                               
                               |_|                          
                    Press ENTER to continue  
                            '''

Cursor.HideCursor()
System.Title('Press ENTER to continue')
Anime.Fade(Center.Center(watermark), Colors.cyan_to_blue, Colorate.Vertical, interval=0.100, enter=True)

Cursor.ShowCursor()
System.Title('FlexiTool by @kazzou')

print(watermark
      .replace('█', colors.purple + '█')
      .replace('╗', colors.blue + '╗')
      .replace('║', colors.blue + '║')
      .replace('╝', colors.blue + '╝')
      .replace('═', colors.blue + '═')
      .replace('╔', colors.blue + '╔')
      + '\n' + colors.white)

def get_pc_name():
    """Retourne le nom de l'ordinateur"""
    return socket.gethostname()

def prompt_input(prompt_message):
    pc_name = get_pc_name()
    return input(f"╭─── {pc_name}@FlexiTool\n│\n╰─$ {prompt_message}")

def ip_info():
    ip = prompt_input("Enter IP address: ")
    print(f"Fetching information for IP: {ip}...")
    data = get_ip_info(ip)
    
    if data:
        print(f"IP Address: {data.get('ip')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country')}")
        print(f"Location: {data.get('loc')}")
        print(f"Organization: {data.get('org')}")
        print(f"Timezone: {data.get('timezone')}")
    else:
        print("No information found.")

def token_decrypt():
    import base64
    from pystyle import Colors
    
    clear()
    userid = prompt_input("Enter Discord ID: ")
    encoded_bytes = base64.b64encode(userid.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    print(f'\nFIRST PART : {encoded_str}')

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def token_info():
    clear()
    try:
        print("Token Info Fetcher")
        token_discord = prompt_input("Enter Discord token: ")
        display_discord_info(token_discord)
        clear()
    except Exception as e:
        print(f"Error: {e}")

def badge_changer():
    clear()
    badge_changer_main()

def status_rotator():
    clear()
    status_changer()

def server_info():
    clear()
    server_lookup()

def webhook_info():
    clear()
    webhook_url = prompt_input("Enter Webhook URL: ")
    info_webhook(webhook_url)

def webhook_spammer():
    clear()
    webhookspam() 

def scrapper_proxy():
    clear()
    print("Starting proxy scrapper...")
    get_proxies()
    print("Proxies have been scraped and saved to proxies.txt.")
    input("\nPress Enter to return to the menu...")

def email_info():
    clear()
    email_info_main()  
    input("\nPress Enter to return to the menu...")

def instagram_user_info():
    clear()
    instagram_user_info_main()
    input("\nPress Enter to return to the menu...")

def number_info():
    clear()
    number_info_main()  
    input("\nPress Enter to return to the menu...")

def auto_login():
    clear()
    auto_login_main()  
    input("\nPress Enter to return to the menu...")

def token_generator():
    clear()
    token_generator_main()  
    input("\nPress Enter to return to the menu...")

def website_info():
    clear()
    website_info_main()  
    input("\nPress Enter to return to the menu...")

ui = interfaces.AnySearch(
    title='FlexiTool',
    subtitles=[
        'Développé par @kazzou',
        'Version: 1.0.0'
    ],
    color=colors.green
)

ui.add_field('IP Info', ip_info)
ui.add_field('Get IP', get_ip_main)
ui.add_field('Token Decrypt', token_decrypt)
ui.add_field('Token Checker', token_checker_main)
ui.add_field('Token Info', token_info)
ui.add_field('Badge Changer', badge_changer)
ui.add_field('Status Rotator', status_rotator)
ui.add_field('Server Info', server_info)
ui.add_field('Webhook Info', webhook_info)
ui.add_field('Webhook Spammer', webhook_spammer)
ui.add_field('Scrapper Proxy', scrapper_proxy)
ui.add_field('Email Info', email_info)
ui.add_field('Instagram User Info', instagram_user_info)
ui.add_field('Number Info', number_info)
ui.add_field('Auto Login', auto_login)
ui.add_field('Token Generator', token_generator)
ui.add_field('Website Info', website_info)
ui.add_field('Token Massdm', execute_mass_dm)
ui.add_field('Discord Massreport', lambda: os.system('python utils/discord_massreport.py'))
ui.add_field('Quit', exit)

def main():
    while True:
        ui.menu()

if __name__ == "__main__":
    main()