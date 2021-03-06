import random
import time
from colorama import Back, Fore, Style


# This function identifies which ascii images to display and prints
# it checks for numbers from the computer output, or tex for the player input
def draw_art(image):
    if image == 'rock' or image == 0:
        print(Fore.RED + Back.BLACK + r'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
image by wynand1004 on GitHub
                                       ''')
        print(Style.RESET_ALL)

    elif image == 'spock' or image == 1:
        print(Fore.YELLOW + Back.BLACK + r'''
    :                                  :
   :  RRVIttIti+==iiii++iii++=;:,       :
   : IBMMMMWWWWMMMMMBXXVVYYIi=;:,        :
   : tBBMMMWWWMMMMMMBXXXVYIti;;;:,,      :
   t YXIXBMMWMMBMBBRXVIi+==;::;::::       ,
  ;t IVYt+=+iIIVMBYi=:,,,=i+=;:::::,      ;;
  YX=YVIt+=,,:=VWBt;::::=,,:::;;;:;:     ;;;
  VMiXRttItIVRBBWRi:.tXXVVYItiIi==;:   ;;;;
  =XIBWMMMBBBMRMBXi;,tXXRRXXXVYYt+;;: ;;;;;
   =iBWWMMBBMBBWBY;;;,YXRRRRXXVIi;;;:;,;;;=
    iXMMMMMWWBMWMY+;=+IXRRXXVYIi;:;;:,,;;=
    iBRBBMMMMYYXV+:,:;+XRXXVIt+;;:;++::;;;
    =MRRRBMMBBYtt;::::;+VXVIi=;;;:;=+;;;;=
     XBRBBBBBMMBRRVItttYYYYt=;;;;;;==:;=
      VRRRRRBRRRRXRVYYIttiti=::;:::=;=
       YRRRRXXVIIYIiitt+++ii=:;:::;==
       +XRRXIIIIYVVI;i+=;=tt=;::::;:;
        tRRXXVYti++==;;;=iYt;:::::,;;
         IXRRXVVVVYYItiitIIi=:::;,::;
          tVXRRRBBRXVYYYIti;::::,::::
           YVYVYYYYYItti+=:,,,,,:::::;
Found at https://asciiart.website/index.php?art=television/star%20trek
''')
        print(Style.RESET_ALL)
    elif image == 'paper' or image == 2:
        print(Fore.RED + Back.BLACK + r'''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
image by wynand1004 on GitHub
                              ''')
        print(Style.RESET_ALL)

    elif image == 'lizard' or image == 3:
        print(Fore.GREEN + Back.BLACK + r'''
              ____...---...___
___.....---"""        .       ""--..____
     .                  .            .
 .             _.--._       /|
        .    .'()..()`.    / /
            ( `-.__.-' )  ( (    .
   .         \        /    \ \
       .      \      /      ) )        .
            .' -.__.- `.-.-'_.'
 .        .'  /-____-\  `.-'       .
          \  /-.____.-\  /-.
           \ \`-.__.-'/ /\|\|           .
          .'  `.    .'  `.
          |/\/\|    |/\/\|
image by jro from AsciiArchives.com
                            ''')
        print(Style.RESET_ALL)

    elif image == 'scissors' or image == 4:
        print(Fore.RED + Back.BLACK + r'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
image by wynand1004 on GitHub''')
        print(Style.RESET_ALL)


# These 2 functions take numbers and return names or vice versa
def name_2_number(name):
    if name == 'rock':
        return 0
    elif name == 'spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4


def number_2_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'


# This function kicks off the game and validates inputs
def game_loop():
    # main game loop starting with answer validation
    run = True
    wins = 0
    loses = 0
    draws = 0
    while True:
        valid_inputs = ("rock", "paper", "scissors", "lizard", "spock")
        user = input("Select rock, paper, scissors, lizard, spock: ")

        if user not in valid_inputs:
            print("Please enter valid response.")

# Compare results, tell player result, and increase correct score
        else:
            user_input = name_2_number(user)
            computer = random.randint(0, 4)
            computer_input = number_2_name(computer)
            result = (user_input - computer) % 5

            if result == 0:
                print("You selected %s." % user)
                draw_art(user_input)
                time.sleep(.8)

                print("Your opponent selected %s" % computer_input)
                draw_art(computer_input)
                time.sleep(.8)
                draws += 1
                print("We're evenly matched! Lets go again!")

            elif result == 1 or result == 2:
                print("You selected %s." % user)
                draw_art(user_input)
                time.sleep(.8)

                print("Your opponent selected %s" % computer_input)
                draw_art(computer_input)
                time.sleep(.8)
                wins += 1
                print("You WIN")

            elif result == 3 or result == 4:
                print("You selected %s." % user)
                draw_art(user_input)
                time.sleep(.8)

                print("Your opponent selected %s" % computer_input)
                draw_art(computer_input)
                time.sleep(.8)
                loses += 1
                print("You've been bested!")

        run = False

# Check if the use wants to play again
        while not run:
            print(f"You're currently {wins}-{loses}-{draws}")
            replay = input("Play again?(Y/N): ")
            if replay == "Y":
                run = True
                break
            elif replay == "N":
                exit()
            else:
                print("please enter a valid response.")


game_loop()
