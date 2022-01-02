#from twilio.rest import Client

# Your Account SID from twilio.com/console
#account_sid = "AC452c9ffe312cd38c51a9296e6511fa9e"
## Your Auth Token from twilio.com/console
#auth_token  = "b43d05a3a2202bc8a106d76d4d76eddb"
#
#client = Client(account_sid, auth_token)
#
#message = client.messages.create(
#    to="+524775643957", 
#    from_="+17279105507",
#    body="Has sido invitado al evento Tamales, para participar accede al siguiente enlace goevents.tech")
#
#print(message.sid)

# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC452c9ffe312cd38c51a9296e6511fa9e" #os.environ['AC452c9ffe312cd38c51a9296e6511fa9e']
auth_token = "b43d05a3a2202bc8a106d76d4d76eddb" #os.environ['b43d05a3a2202bc8a106d76d4d76eddb']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Fuiste invitado al Evento Tamales participa en el siguiente enlace goevents.tech',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+5214775808404')

print(message.sid)
