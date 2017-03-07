import requests
from config import mailgun

def send_failure_message(item):
    return requests.post(
        mailgun['url'],
        auth=("api", mailgun['key']),
        data={"from": "Mailgun Sandbox <postmaster@sandbox24b0fe09016643cbadc6d2c24b650484.mailgun.org>",
              "to": "Marius <mariusvach@googlemail.com>",
              "subject": "%s is probably down!" % item[0],
              "text": "%s failed our tests. It may be down!" % item[0]})
