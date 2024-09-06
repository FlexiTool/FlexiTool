import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

class EmailTracker:
    def __init__(self, email):
        self.email = email
        self.session = requests.Session()
        self.ua = UserAgent()

        self.sites = [
            self.Instagram,
            self.Twitter,
            self.Pinterest,
            self.Imgur,
            self.Patreon,
            self.Spotify,
            self.FireFox,
            self.LastPass,
            self.Archive,
            self.PornHub,
            self.Xnxx,
            self.Xvideo
        ]

    def track_emails(self):
        results = []
        for site in self.sites:
            result = site(self.email)
            results.append((site.__name__, result))
        return results
    
    def Instagram(self, email):
        try:
            session = requests.Session()
            headers = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Origin': 'https://www.instagram.com',
                'Connection': 'keep-alive',
                'Referer': 'https://www.instagram.com/'
            }

            data = {
                "email": email
            }

            response = session.get(
                "https://www.instagram.com/accounts/emailsignup/", 
                headers=headers
            )
            if response.status_code == 200:
                if 'csrftoken' in session.cookies:
                    token = session.cookies['csrftoken']
                else:
                    return "Error: Token Not Found."
            else:
                return f"Error: {response.status_code}"

            headers["x-csrftoken"] = token
            headers["Referer"] = "https://www.instagram.com/accounts/emailsignup/"

            response = session.post(
                url="https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/",
                headers=headers,
                data=data
            )
            if response.status_code == 200:
                if "Another account is using the same email." in response.text:
                    return True
                elif "email_is_taken" in response.text:
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        pass

    def Twitter(self, email):
        try:
            session = requests.Session()

            response = session.get(
                url = "https://api.twitter.com/i/users/email_available.json",
                params = {
                    "email": email
                }
            )
            if response.status_code == 200:
                if response.json()["taken"] == True:
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

        pass

    def Pinterest(self, email):
        try:
            session = requests.Session()
            response = session.get(
                "https://www.pinterest.com/_ngjs/resource/EmailExistsResource/get/",
                params={
                    "source_url": "/",
                    "data": '{"options": {"email": "' + email + '"}, "context": {}}'
                }
            )

            if response.status_code == 200:
                if response.json()["resource_response"]["message"] == "Invalid email.":
                    return False
                elif response.json()["resource_response"]["message"] == "ok":
                    if response.json()["resource_response"]["data"] == False:
                        return False
                    elif response.json()["resource_response"]["data"] == True:
                        return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        pass


    def Imgur(self, email):
        try:
            session = requests.Session()

            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'en,en-US;q=0.5',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Origin': 'https://imgur.com',
                'DNT': '1',
                'Connection': 'keep-alive',
                'TE': 'Trailers',
            }

            r = session.get("https://imgur.com/register?redirect=%2Fuser", headers=headers)

            headers["X-Requested-With"] = "XMLHttpRequest"

            data = {
                'email': email
            }

            response = session.post('https://imgur.com/signin/ajax_email_available', headers=headers, data=data)

            if response.status_code == 200:
                if response.json()['data']["available"] == True:
                    return False
                elif response.json()["data"]["available"] == False:
                    if "Invalid email domain" in response.text:
                        return False
                    else:
                        return True
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def Patreon(self, email):
        try:
            session = requests.Session()

            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'Origin': 'https://www.plurk.com',
                'DNT': '1',
                'Connection': 'keep-alive',
            }

            data = {
                'email': email
            }

            response = session.post('https://www.plurk.com/Users/isEmailFound', headers=headers, data=data)
            if response.status_code == 200:
                if "True" in response.text:
                    return True
                elif "False" in response.text:
                    return False
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def Spotify(self, email):
        try:
            session = requests.Session()
        
            headers = {
                'User-Agent': user_agent,
                'Accept': 'application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                'DNT': '1',
                'Connection': 'keep-alive',
            }
            
            params = {
                'validate': '1',
                'email': email,
            }

            response = session.get('https://spclient.wg.spotify.com/signup/public/v1/account',
                    headers=headers,
                    params=params)
            if response.status_code == 200:
                if response.json()["status"] == 1:
                    return False
                elif response.json()["status"] == 20:
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def FireFox(self, email):
        try:
            session = requests.Session()

            data = {
                "email": email
            }

            response = session.post(
                "https://api.accounts.firefox.com/v1/account/status",
                data=data
            )

            if response.status_code == 200:
                if "false" in response.text:
                    return False
                elif "true" in response.text:
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"

    def LastPass(self, email):
        try:
            session = requests.Session()
            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'en,en-US;q=0.5',
                'Referer': 'https://lastpass.com/',
                'X-Requested-With': 'XMLHttpRequest',
                'DNT': '1',
                'Connection': 'keep-alive',
                'TE': 'Trailers',
            }
            params = {
                'check': 'avail',
                'skipcontent': '1',
                'mistype': '1',
                'username': email,
            }
            
            response = session.get(
                'https://lastpass.com/create_account.php?check=avail&skipcontent=1&mistype=1&username='+str(email).replace("@", "%40"),       
                params=params,
                headers=headers)
            
            if response.status_code == 200:
                if "no" in response.text:
                    return True
                elif "emailinvalid" in response.text:
                    return False
                elif "ok" in response.text:
                    return False
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def Archive(self, email):
        try:
            session = requests.Session()

            headers = {
                'User-Agent': user_agent,
                'Accept': '*/*',
                'Accept-Language': 'en,en-US;q=0.5',
                'Content-Type': 'multipart/form-data; boundary=---------------------------',
                'Origin': 'https://archive.org',
                'Connection': 'keep-alive',
                'Referer': 'https://archive.org/account/signup',
                'Sec-GPC': '1',
                'TE': 'Trailers',
            }

            data = '-----------------------------\r\nContent-Disposition: form-data; name="input_name"\r\n\r\nusername\r\n-----------------------------\r\nContent-Disposition: form-data; name="input_value"\r\n\r\n' + email + \
                '\r\n-----------------------------\r\nContent-Disposition: form-data; name="input_validator"\r\n\r\ntrue\r\n-----------------------------\r\nContent-Disposition: form-data; name="submit_by_js"\r\n\r\ntrue\r\n-------------------------------\r\n'

            response = session.post('https://archive.org/account/signup', headers=headers, data=data)
            if response.status_code == 200:
                if "is already taken." in response.text:
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def PornHub(self, email):
        try:
            session = requests.Session()

            headers = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en,en-US;q=0.5',
                'DNT': '1',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
            }
            
            response = session.get("https://www.pornhub.com/signup", headers=headers)
            if response.status_code == 200:
                token = BeautifulSoup(response.content, features="html.parser").find(attrs={"name": "token"})

                if token is None:
                    return "Error: Token Not Found."
                
                token = token.get("value")
            else:
                return f"Error: {response.status_code}"

            params = {
                'token': token,
            }

            data = {
                'check_what': 'email',
                'email': email
            }

            response = session.post(
                'https://www.pornhub.com/user/create_account_check',
                headers=headers,
                params=params,
                data=data
            ) 
            if response.status_code == 200:
                if response.json()["error_message"] == "Email has been taken.":
                    return True
                elif "Email has been taken." in response.text:
                    return True
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def Xnxx(self, email):
        try:
            session = requests.Session()

            headers = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'en-en',
                'Host': 'www.xnxx.com',
                'Referer': 'https://www.google.com/',
                'Connection': 'keep-alive'
            }
            
            cookie = session.get('https://www.xnxx.com', headers=headers)

            if cookie.status_code == 200:
                if not cookie:
                    return "Error: Cookie Not Found."
            else:
                return f"Error: {cookie.status_code}"
            
            headers['Referer'] = 'https://www.xnxx.com/video-holehe/palenath_fucks_xnxx_with_holehe'
            headers['X-Requested-With'] = 'XMLHttpRequest'
            email = email.replace('@', '%40')

            response = session.get(f'https://www.xnxx.com/account/checkemail?email={email}', headers=headers, cookies=cookie.cookies)
            
            if response.status_code == 200:
                try:
                    if response.json()['message'] == "This email is already in use or its owner has excluded it from our website.":
                        return True
                    elif response.json()['message'] == "Invalid email address.": 
                        return False
                except:
                    pass
                if response.json()['result'] == "false":
                    return True
                elif response.json()['code'] == 1:
                    return True
                elif response.json()['result'] == "true":
                    return False
                elif response.json()['code'] == 0:
                    return False  
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except Exception as e:
            return f"Error: {e}"
        
    def Xvideo(self, email):
        try:
            session = requests.Session()

            headers = {
                'User-Agent': user_agent,
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'X-Requested-With': 'XMLHttpRequest',
                'Connection': 'keep-alive',
                'Referer': 'https://www.xvideos.com/',
            }

            params = {
                'email': email,
            }

            response = session.get('https://www.xvideos.com/account/checkemail', headers=headers, params=params)
            if response.status_code == 200:
                try:
                    if response.json()['message'] == "This email is already in use or its owner has excluded it from our website.": 
                        return True
                    elif response.json()['message'] == "Invalid email address.": 
                        return False
                except: 
                    pass    
                if response.json()['result'] == "false":
                    return True
                elif response.json()['code'] == 1:
                    return True
                elif response.json()['result'] == "true":
                    return False
                elif response.json()['code'] == 0:
                    return False
                else:
                    return False
            else:
                return f"Error: {response.status_code}"
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"
        except Exception as e:
            return f"Error: {e}"


def track_emails():
    while True:
        email = input("Enter email address: ")

        if not email:
            print("Error: Please enter a valid email address.")
            continue

        if not email.endswith(("@gmail.com", "@yahoo.com", "@hotmail.com", "@outlook.com", "@protonmail.com")):
            print("Error: Please enter a valid email address.")
            continue

        try:
            tracker = EmailTracker(email)
            results = tracker.track_emails()  # No need to pass 'email' again here
            for site, availability in results:
                print(f"{site}: {'Available' if availability else 'Not Available'}")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    track_emails()