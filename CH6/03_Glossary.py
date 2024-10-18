glossary = {
    'variable': 'Box that contains info.', 'dictionary': 'Box that contains key pairs of info.',
    'method': 'Base py functions within classes unseen.', 'bug':'An issue or error in code.',
    'API': 'Things that allow applictions to work with each other.'
    }
words = ['variable', 'dictionary', 'method', 'bug', 'API']

for n in words:
    print(f"{n.title()}: {glossary[n]}\n")