import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# The account sid and auth token is taken from twilio.com/console
# and set the environment variables.
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client_SMS = Client(account_sid, auth_token)

# Change the phone numbers
message = client_SMS.messages \
    .create(
    body="Your irrigation Pi is starting working.",
    from_='+1XXXXXXXXXX',
    to='1XXXXXXXXXX'
)

# print(message.sid)
