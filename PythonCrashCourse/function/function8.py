messages = ["You're cute", "You're ugly", "You look like a fuckable piece of meat"]
messages2 = []
unsent_message = ["Fuck you", "I love you", "I fucking hate you"]

def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(unsent_message, messages2):
    while unsent_message:
        sent_message = unsent_message.pop()
        print("Sending messages...\n")
        messages2.append(sent_message)
    
def show_sent_messages(messages2):
    for message2 in messages2:
        print(message2)

send_messages(unsent_message[:], messages2)
show_sent_messages(messages2)
show_messages(messages)

print(messages2, unsent_message)