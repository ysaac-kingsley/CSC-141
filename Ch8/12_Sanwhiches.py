def make_which(*contents):
    print("Making the sanwhich with:")
    for content in contents:
        print(f"- {content}")

make_which('bacon', 'lettuce', 'tomatoes')

make_which('bacon', 'lettuce', 'tomatoes', 'mayo')

make_which('bacon', 'lettuce', 'tomatoes', 'mayo', 'turkey')