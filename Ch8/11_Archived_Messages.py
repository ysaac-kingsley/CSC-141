def send_messages(messages):
    for message in messages:
        print(message)

    while messages:
        word = messages.pop()
        sent_txt.append(word)

unsent_txt = ['Lmk!', 'Omg!', 'Wya?', 'Hiii:)']
sent_txt = []

send_messages(unsent_txt[:])

print(unsent_txt)
print(sent_txt)