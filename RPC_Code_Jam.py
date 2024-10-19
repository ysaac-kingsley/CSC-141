import random
import time
user = {}
active_game = True

name = input('Welcome to Rock Paper Scissors!\nWhat is your name?\n')
uname = input('What is your username going to be?\n')
user[name] = uname


while active_game:
    randomnum = random.randint(1,3)
    opt = input('Type rock, paper, or scissors to make your choice.\nTo end type exit.\n')
    if opt == 'exit':
        active_game = False
    if randomnum == 1:

        if randomnum == 1 and opt.lower() == 'rock':
            print('You chose' + opt)
            time.sleep(1)
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(1)
            print(f"{user[name]} tied...¯\_(ツ)_/¯")
        elif randomnum == 1 and opt.lower() == 'scissors':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(1)
            print(f"{user[name]} lost :*(")
            time.sleep(1)
            print(' /$$        /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$$$$$$ ')
            print('| $$       /$$__  $$ /$$__  $$| $$_____/| $$__  $$| $$__  $$')
            print('| $$      | $$  \ $$| $$  \__/| $$      | $$  \ $$| $$  \ $$')
            print('| $$      | $$  | $$|  $$$$$$ | $$$$$   | $$$$$$$/| $$$$$$$/')
            print('| $$      | $$  | $$ \____  $$| $$__/   | $$__  $$| $$__  $$')
            print('| $$      | $$  | $$ /$$  \ $$| $$      | $$  \ $$| $$  \ $$')
            print('| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$| $$  | $$')
            print('|________/ \______/  \______/ |________/|__/  |__/|__/  |__/')
        elif randomnum == 1 and opt.lower == 'paper':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(1)
            print(f"{user[name]} won!")
            time.sleep(1)
            print(' /$$     /$$                        /$$      /$$')
            print('|  $$   /$$/                       | $$  /$ | $$')
            print(' \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$  /$$$$$$  /$$$$$$$')
            print('  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$ /$$__  $$| $$__  $$')
            print('   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$  \ $$| $$  \ $$')
            print('    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$  | $$')
            print('    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$  | $$')
            print('    |__/  \______/  \______/       |__/     \__/ \______/ |__/  |__/')
        else:
            print('That is not an option. >:|')
    elif randomnum == 2:

        if randomnum == 2 and opt.lower() == 'paper':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(1)
            print(f"{user[name]} tied...¯\_(ツ)_/¯")
        elif randomnum == 2 and opt.lower() == 'scissors':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(1)
            print(f"{user[name]} won!")
            time.sleep(1)
            print(' /$$     /$$                        /$$      /$$')
            print('|  $$   /$$/                       | $$  /$ | $$')
            print(' \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$  /$$$$$$  /$$$$$$$')
            print('  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$ /$$__  $$| $$__  $$')
            print('   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$  \ $$| $$  \ $$')
            print('    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$  | $$')
            print('    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$  | $$')
            print('    |__/  \______/  \______/       |__/     \__/ \______/ |__/  |__/')
        elif randomnum == 2 and opt.lower() == 'rock':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(1)
            print(f"{user[name]} lost :*(")
            time.sleep(1)
            print(' /$$        /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$$$$$$ ')
            print('| $$       /$$__  $$ /$$__  $$| $$_____/| $$__  $$| $$__  $$')
            print('| $$      | $$  \ $$| $$  \__/| $$      | $$  \ $$| $$  \ $$')
            print('| $$      | $$  | $$|  $$$$$$ | $$$$$   | $$$$$$$/| $$$$$$$/')
            print('| $$      | $$  | $$ \____  $$| $$__/   | $$__  $$| $$__  $$')
            print('| $$      | $$  | $$ /$$  \ $$| $$      | $$  \ $$| $$  \ $$')
            print('| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$| $$  | $$')
            print('|________/ \______/  \______/ |________/|__/  |__/|__/  |__/')
        else:
            print('That is not an option. >:|')
    elif randomnum == 3:

        if randomnum == 3 and opt.lower() == 'scissors':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(1)
            print(f"{user[name]} tied...¯\_(ツ)_/¯")
        elif randomnum == 3 and opt.lower() == 'rock':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(1)
            print(f"{user[name]} won!")
            time.sleep(1)
            print(' /$$     /$$                        /$$      /$$')
            print('|  $$   /$$/                       | $$  /$ | $$')
            print(' \  $$ /$$//$$$$$$  /$$   /$$      | $$ /$$$| $$  /$$$$$$  /$$$$$$$')
            print('  \  $$$$//$$__  $$| $$  | $$      | $$/$$ $$ $$ /$$__  $$| $$__  $$')
            print('   \  $$/| $$  \ $$| $$  | $$      | $$$$_  $$$$| $$  \ $$| $$  \ $$')
            print('    | $$ | $$  | $$| $$  | $$      | $$$/ \  $$$| $$  | $$| $$  | $$')
            print('    | $$ |  $$$$$$/|  $$$$$$/      | $$/   \  $$|  $$$$$$/| $$  | $$')
            print('    |__/  \______/  \______/       |__/     \__/ \______/ |__/  |__/')

        elif randomnum == 3 and opt.lower() == 'paper':
            print('You chose ' + opt)
            time.sleep(1)
            print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
            time.sleep(1)
            print('Your opponent chose...')
            time.sleep(1)
            print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
            time.sleep(1)
            print(f"{user[name]} lost :*(")
            time.sleep(1)
            print(' /$$        /$$$$$$   /$$$$$$  /$$$$$$$$ /$$$$$$$  /$$$$$$$ ')
            print('| $$       /$$__  $$ /$$__  $$| $$_____/| $$__  $$| $$__  $$')
            print('| $$      | $$  \ $$| $$  \__/| $$      | $$  \ $$| $$  \ $$')
            print('| $$      | $$  | $$|  $$$$$$ | $$$$$   | $$$$$$$/| $$$$$$$/')
            print('| $$      | $$  | $$ \____  $$| $$__/   | $$__  $$| $$__  $$')
            print('| $$      | $$  | $$ /$$  \ $$| $$      | $$  \ $$| $$  \ $$')
            print('| $$$$$$$$|  $$$$$$/|  $$$$$$/| $$$$$$$$| $$  | $$| $$  | $$')
            print('|________/ \______/  \______/ |________/|__/  |__/|__/  |__/')
        
        else:
            print('That is not an option. >:|')
    elif opt == 'exit':
        active_game = False
