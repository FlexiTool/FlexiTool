
try:
    import os
    import sys
    import socket
    import time
    import base64
    from pystyle import Colors, Cursor, System, Anime, Center, Colorate
    from rich.console import Console
except ModuleNotFoundError:
    os.system('pip install os')
    os.system('pip install sys')
    os.system('pip install socket')
    os.system('pip install time')
    os.system('pip install base64')
    os.system('pip install pystyle')
    os.system('pip install rich.console')


console = Console()

# Append the path to the utils directory where your utility modules are located.
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

# Import utility modules
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
from email_tracker import track_emails
from discord_bot_server_nuker import nuke_server

# Function to setup system properties like window size and title
def setup():
    System.Size(120, 30)
    System.Title("FlexiTool - Advanced Python Utility by @kazzou")
    Cursor.HideCursor()

# Intro animation using pystyle
def launch_animation():
    intro_text = '''
                                                                                                  
              █████▒██▓    ▓█████ ▒██   ██▒ ██▓      ▄▄▄█████▓ ▒█████   ▒█████   ██▓    
            ▓██   ▒▓██▒    ▓█   ▀ ▒▒ █ █ ▒░▓██▒      ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    
            ▒████ ░▒██░    ▒███   ░░  █   ░▒██▒      ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    
            ░▓█▒  ░▒██░    ▒▓█  ▄  ░ █ █ ▒ ░██░      ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    
            ░▒█░   ░██████▒░▒████▒▒██▒ ▒██▒░██░        ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒
             ▒ ░   ░ ▒░▓  ░░░ ▒░ ░▒▒ ░ ░▓ ░░▓          ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░
             ░     ░ ░ ▒  ░ ░ ░  ░░░   ░▒ ░ ▒ ░          ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░
             ░ ░     ░ ░      ░    ░    ░   ▒ ░        ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   
                       ░  ░   ░  ░ ░    ░   ░                     ░ ░      ░ ░      ░  ░
                                                                             
                                                                                                   
                                    Press ENTER to start the tool...                                                                
    '''
    Anime.Fade(Center.Center(intro_text), Colors.rainbow, Colorate.Vertical, interval=0.05, enter=True)

# Clear screen function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get the computer's name
def get_pc_name():
    return socket.gethostname()

# Stylized prompt for user input
def prompt_input(prompt_message):
    pc_name = get_pc_name()
    return input(f"{Colors.green}╭─── {pc_name}@FlexiTool\n{Colors.gray}│\n{Colors.green}╰─$ {prompt_message}{Colors.white}")

# Function to display IP info
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
    input("\nPress Enter to return to the menu...")
        
# Function to decrypt a Discord token
def token_decrypt():
    clear_screen()
    userid = prompt_input("Enter Discord ID: ")
    encoded_bytes = base64.b64encode(userid.encode("utf-8"))
    encoded_str = str(encoded_bytes, "utf-8")
    print(f'\nFIRST PART: {encoded_str}')
    input("\nPress Enter to return to the menu...")
    

# Function to display Discord token info
def token_info():
    clear_screen()
    try:
        print("Token Info Fetcher")
        token_discord = prompt_input("Enter Discord token: ")
        display_discord_info(token_discord)
        clear_screen()
    except Exception as e:
        print(f"Error: {e}")
    input("\nPress Enter to return to the menu...")
        

# Function to change Discord badges
def badge_changer():
    clear_screen()
    badge_changer_main()
    input("\nPress Enter to return to the menu...")
    

# Function to rotate Discord statuses
def status_rotator():
    clear_screen()
    status_changer()
    input("\nPress Enter to return to the menu...")
    

# Function to lookup server info
def server_info():
    clear_screen()
    server_lookup()
    input("\nPress Enter to return to the menu...")
    

# Function to get webhook info
def webhook_info():
    clear_screen()
    webhook_url = prompt_input("Enter Webhook URL: ")
    info_webhook(webhook_url)
    input("\nPress Enter to return to the menu...")

# Function to spam a webhook
def webhook_spammer():
    clear_screen()
    webhookspam()
    input("\nPress Enter to return to the menu...")

# Function to scrape proxies
def scrapper_proxy():
    clear_screen()
    print("Starting proxy scrapper...")
    get_proxies()
    print("Proxies have been scraped and saved to proxies.txt.")
    input("\nPress Enter to return to the menu...")

# Function to get email info
def email_info():
    clear_screen()
    email_info_main()  
    input("\nPress Enter to return to the menu...")

# Function to get Instagram user info
def instagram_user_info():
    clear_screen()
    instagram_user_info_main()
    input("\nPress Enter to return to the menu...")

# Function to get phone number info
def number_info():
    clear_screen()
    number_info_main()  
    input("\nPress Enter to return to the menu...")

# Function for auto-login
def auto_login():
    clear_screen()
    auto_login_main()  
    input("\nPress Enter to return to the menu...")

# Function to generate tokens
def token_generator():
    clear_screen()
    token_generator_main()  
    input("\nPress Enter to return to the menu...")

# Function to get website info
def website_info():
    clear_screen()
    website_info_main()  
    input("\nPress Enter to return to the menu...")

# Function to send mass DM with token
def execute_mass_dm():
    clear_screen()
    # Assuming the execute_mass_dm function is correctly implemented in token_massdm module
    token = prompt_input("Enter token: ")
    message = prompt_input("Enter the message to send: ")
    execute_mass_dm(token, message)
    input("\nPress Enter to return to the menu...")
#1.1 VERSION NEW COMMANDS :    
def email_tracker():
    clear_screen()
    track_emails()
    input("\nPress Enter to return to the menu...")


def discord_bot_server_nuker():
    clear_screen()
    nuke_server()
    input("\nPress Enter to return to the menu...")

console = Console()

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get the computer's name
def get_pc_name():
    return socket.gethostname()

# Stylized prompt for user input
def prompt_input(prompt_message):
    pc_name = get_pc_name()
    return input(f"{Colors.green}╭─── {pc_name}@FlexiTool\n{Colors.gray}│\n{Colors.green}╰─$ {prompt_message}{Colors.white}")




# Function to display the menu
def display_menu():
    logo = r"""
███████╗██╗     ███████╗██╗  ██╗██╗        ████████╗ ██████╗  ██████╗ ██╗     
██╔════╝██║     ██╔════╝╚██╗██╔╝██║        ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
█████╗  ██║     █████╗   ╚███╔╝ ██║           ██║   ██║   ██║██║   ██║██║     
██╔══╝  ██║     ██╔══╝   ██╔██╗ ██║           ██║   ██║   ██║██║   ██║██║     
██║     ███████╗███████╗██╔╝ ██╗██║           ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝           ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                               
    """
    console.print(logo, style="bold green")  # Print the logo in green and left-aligned


    menu = """

    [I] Info                 github.com/FlexiTool/FlexiTool
    [S] Site
    Main Functions                   
    ──────────────────────────────────────────────────────
    [1] IP Info                     [2] Token Decrypt
    [3] Token Checker               [4] Token Info                  
    [5] Badge Changer               [6] Status Rotator                         
    [7] Server Info                 [8] Webhook Info              
    [9] Webhook Spammer             [10] Scrapper Proxy             
    [11] Email Info                 [12] Instagram User Info                     
    [13] Number Info                [14] Auto Login                         
    [15] Token Generator            [16] Website Info                        
    [17] Token Massdm               [18] Email Tracker                        
    [19] Discord Bot Server Nuker   [20] Quit                      

    """

    clear_screen()  # Clean the screen before displaying the menu
    console.print(logo, style="bold green")  # Display the logo in green
    console.print(menu, style="bold white")

    choice = prompt_input("Choose an option: ").lower()
    
    if choice == "i":
        print("Information about the tool: By Kazzou")
        input("\nPress Enter to return to the menu...")
    elif choice == "s":
        print("Visit the website: https://github.com/FlexiTool/FlexiTool")
        input("\nPress Enter to return to the menu...")
    elif choice in map(str, range(1, 21)):
        main_menu_options[int(choice)]()
    else:
        print(f"{Colors.red}Invalid option! Please try again.{Colors.white}")
        time.sleep(1)

# Mapping of main menu choices to corresponding functions
main_menu_options = {
    1: ip_info,
    2: token_decrypt,
    3: token_checker_main,
    4: token_info,
    5: badge_changer,
    6: status_rotator,
    7: server_info,
    8: webhook_info,
    9: webhook_spammer,
    10: scrapper_proxy,
    11: email_info,
    12: instagram_user_info,
    13: number_info,
    14: auto_login,
    15: token_generator,
    16: website_info,
    17: execute_mass_dm,
    18: email_tracker,
    19: discord_bot_server_nuker,
    20: sys.exit,
}

# Main function
def main():
    setup()
    launch_animation()  # Run the color-changing animation at launch
    while True:
        display_menu()

if __name__ == "__main__":
    main()