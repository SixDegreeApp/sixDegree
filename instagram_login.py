#The initial login?
payload = {
    "username": "ENTER_USERNAME_HERE",
    "password": "ENTER_PASSWORD_HERE",
    "csrf_token": "N5jvKWRKxWCUt2JZMo4dsKtjFgXqYX0a"
}

from lxml import html

session_requests = requests.session()
login_url = 'https://www.instagram.com/accounts/login/?hl=en'
result = session_requests.get(login_url)

tree = html.frontstring(result.text)
