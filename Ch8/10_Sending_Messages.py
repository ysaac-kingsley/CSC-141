unsent_txt = ['Lmk!', 'Omg!', 'Wya?', 'Hiii:)']
sent_txt = []



def send_messages(messages):
    for message in messages:
        print(message)

    while unsent_txt:
        word = unsent_txt.pop()
        sent_txt.append(word)



send_messages(unsent_txt)

print(unsent_txt)
print(sent_txt)