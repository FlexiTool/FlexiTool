import subprocess
from emailrep import EmailRep
import re
from pystyle import Colors

def handle_error(error_message):
    print(f"Error: {error_message}")

def check_email_with_holehe(email):
    try:

        output = subprocess.check_output(["C:\\Program Files\\Holehe\\holehe.exe", email]).decode("utf-8")
        output_lines = output.splitlines()
        print(f"\nRésultats pour l'email : {email}\n")
        for line in output_lines:
            match = re.match(r"\[\+\] Email used: .* on (.*)", line)
            if match:
                print(match.group(1))
    except Exception as e:
        handle_error(f"Erreur d'exécution : {str(e)}")

def get_email_information_with_emailrep(email):
    api = EmailRep()
    try:
        response = api.query(email)
        if response:
            print(f"\nRésultats de EmailRep :")
            print(f"Email: {email}")
            if 'reputation' in response:
                print(f"Réputation: {response['reputation']}")
            else:
                print(f"Réputation: N/A")
                
            if 'details' in response:
                print(f"Détails: {response['details']}")
                if 'sources' in response['details']:
                    print(f"Sources: {response['details']['sources']}")
                else:
                    print(f"Sources: N/A")
                print(f"Date de création du compte: {response['details'].get('date_creation', 'N/A')}")
                print(f"Dernière fois vu: {response['details'].get('last_seen', 'N/A')}")
                print(f"Jours depuis la dernière fois vu: {response['details'].get('days_since_last_seen', 'N/A')}")
                print(f"Statut de liste noire: {response['details'].get('blacklisted', 'N/A')}")
                print(f"Statut de malveillance: {response['details'].get('malicious_activity', 'N/A')}")
            else:
                print(f"Détails: N/A")
        else:
            print(f"Aucune information trouvée pour {email}")
    except Exception as e:
        handle_error(f"Erreur de requête : {str(e)}")

def main():
    email = input(f"Entrez l'adresse email : ")
    check_email_with_holehe(email)
    get_email_information_with_emailrep(email)

if __name__ == "__main__":
    main()