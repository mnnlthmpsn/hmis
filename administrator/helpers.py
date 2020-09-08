import random, string
import datetime
from .models import Logs

def generate_ID():
    """
    STAFF ID GENERATOR
    """
    key = ''
    for i in range(5):
        key += random.choice(string.digits)
    return key

def send_to_staff(ID, password, email):
    print(f"Sending staff ID:{ID} and password:{password} to {email}")

def get_all_staff(model):
    all_staff = model.objects.all()
    return all_staff

def create_log_entry(user, action):
    log_action = f"{user} {action}"
    log = Logs.objects.create(action=log_action)
    log.save()
