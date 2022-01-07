from twilio.rest import Client
import keys

client = Client(keys.sid, keys.token)

message = client.messages.create(
    body = "Hi This is sathwik",
    from_=keys.twilio_number,
    to=keys.my_number
)


print(message.body)