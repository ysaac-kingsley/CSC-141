favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 'ysaac': '',
 'chance':'cobalt',
 'cheech': ''
}

for k,v in favorite_languages.items():
    if v == "":
        print(f"Please take the favorite languages poll {k.title()}.\n")
    else:
        print(f"Thank you for taking the favorite languages poll {k.title()}\n" )