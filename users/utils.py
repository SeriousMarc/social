from django.conf import settings
from pyhunter import PyHunter
import clearbit

hunter = PyHunter(settings.HUNTER_API_KEY)
clearbit.key = settings.CLEARBIT_API_KEY


def is_email_valid(email):
    r = hunter.email_verifier(email)
    return all([
        r['result'] != 'undeliverable',
        not r['disposable'],
        r['smtp_server']
    ])


def user_enrichment(email):
    r = clearbit.Enrichment.find(email=email, stream=True)
    data = {}
    if r:
        first_name = r['person']['name']['givenName']
        last_name = r['person']['name']['familyName']
        if first_name and last_name:
            data.setdefault('first_name', first_name)
            data.setdefault('last_name', last_name)
    return data