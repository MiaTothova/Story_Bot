import time
from colorama import Fore, Style

# Dictionary
word_choice = {
    'name': ['Ella', 'Max', 'Whiskers', 'Daisy', 'Sparkle',
             'Flash', 'Giggles', 'Bubbles', 'Snickers', 'Twinkle'],
    'place': ['jungle', 'amusement park', 'spaghetti factory',
              'rollercoaster', 'library', 'spaceship', 'giant pillow forth',
              'candy store', 'zoo', 'aquarium'],
    'liquid': ['river', 'pudding', 'chocolate', 'lemonade', 'milkshake',
               'rainbow', 'bubble', 'glitter', 'confetti', 'jelly'],
    'body': ['trunk', 'tail', 'paw', 'ear', 'nose', 'hoof', 'fin', 'wing',
             'antenna', 'whisker'],
    'thing1': ['cereal bowl', 'treasure chest', 'ocean of pudding',
               'circus tent', 'popcorn cloud', 'smoothie sea',
               'cotton candy sky', 'giant pizza', 'pancake stack'],
    'sound': ['fart noises', 'chicken clucks', 'robot beeps', 'disco beats',
              'alien whispers', 'rap verses', 'karaoke songs', 'banjo solos',
              'quacking ducks'],
    'thing2': ['playgrounds', 'trees', 'sandcastles', 'ball pits',
               'snow globes', 'race tracks', 'toy boxes', 'candy lands',
               'swimming pools'],
    'action': ['dance moves', 'laugh', 'balloon animals', 'face paint',
               'tickles', 'juggling', 'magic tricks', 'pranks', 'cartwheels'],
    'food': ['marshmallows', 'glitter', 'bananas', 'rainbows', 'kites',
             'ice cream cones', 'sprinkles', 'cupcakes'],
    'place2': ['horizon', 'treasure chest', 'ocean of pudding',
               'pancake stack', 'giant pizza', 'circus tent', 'popcorn cloud',
               'smoothie sea', 'candy sky']
}


def welcome():
    print(r" ____  _                        ____        _")
    print(r"/ ___|| |_ ___  _ __ _   _     | __ )  ___ | |_ ")
    print(r"\___ \| __/ _ \| '__| | | |    |  _ \ / _ \| __|")
    print(r" ___) | || (_) | |  | |_| |    | |_) | (_) | |_ ")
    print(r"|____/ \__\___/|_|   \__, |    |____/ \___/ \__|")
    print(r"                    |___/                      ")

    print(f"{Fore.YELLOW}Welcome to Story Bot!{Style.RESET_ALL}\n")
    time.sleep(2)
    # user = input("What's your name? : \n")
    # print(f"Hi {Fore.YELLOW}{user}{Style.RESET_ALL}! Pick a story.\n \n")
    # time.sleep(2)
    while True:
        username = input("What's your name? (Letters only):\n").strip()
        if username.isalpha():
            return print(f"\n{Fore.YELLOW}Hi {username}!{Style.RESET_ALL}\n\n")
        print(f"{Fore.RED}Invalid input. Enter a name.{Style.RESET_ALL}")


def start_game():
    welcome()
    while True:  # Start an infinite loop to show menu continuously
        print(f"{Fore.YELLOW}I have 4 stories to choose from and")
        print(f"YOU pick the words!{Style.RESET_ALL}\n")
        time.sleep(2)
        print(f"{Fore.YELLOW}Here they are:{Style.RESET_ALL} \n")
        print("1. The Happy Elephant")
        print("2. The Speedy Mouse")
        print("3. The Curious Cat")
        print("4. The Funny Cow")
        print("5. End Game \n")

        choice = input("Pick a story by entering a number, press 5 to Quit:")
        if choice == "1":
            elephant_story()
        elif choice == "2":
            mouse_story()
        elif choice == "3":
            cat_story()
        elif choice == "4":
            cow_story()
        elif choice == "5":
            print(f"{Fore.YELLOW}\n\nSee you next time!{Style.RESET_ALL} ")
            break  # Break out of the loop to end the game
        else:
            print(f"{Fore.RED}Enter a valid option! {Style.RESET_ALL}\n\n")


def selectItem(key):
    items = word_choice[key]  # Get the list of items for the given key
    max_index = len(items)  # This is the maximum index we can select

    # Print the options for the user
    print(f"{Fore.YELLOW}Select a '{key}'from below: {Style.RESET_ALL}")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    while True:
        # Start an infinite loop to keep asking until a valid input is given
        try:
            selection = int(input(f"Enter your choice (1-{max_index}): "))
            # Ask user for input
            if 1 <= selection <= max_index:
                # Check if the selection is within the valid range
                return items[selection - 1]  # Return the selected item
            else:
                # Inform the user about the valid range
                print(f"{Fore.RED}Between 1 & {max_index}.{Style.RESET_ALL}")
        except ValueError:
            # Handle the case where input is not a number
            print(f"{Fore.RED}Invalid input.Enter a number.{Style.RESET_ALL}")


# selectItem print:s selected words into the story
def elephant_story():
    name = selectItem('name')
    place = selectItem('place')
    liquid = selectItem('liquid')
    body = selectItem('body')
    thing1 = selectItem('thing1')
    sound = selectItem('sound')
    thing2 = selectItem('thing2')
    action = selectItem('action')
    food = selectItem('food')
    place2 = selectItem('place2')

    time.sleep(1)
    print(f"\n{Fore.YELLOW}Loading......................{Style.RESET_ALL}\n")
    time.sleep(2)
    print(r" __              ")
    print(r"'. \                ")
    print(r"'- \               ")
    print(r" / /_         .---.")
    print(r"/ | \,.\/--.//    )")
    print(r"|  \//        )/  / ")
    print(r" \  ' ^ ^    /    )____.----..  6")
    print(r"  '.____.    .___/            \._) ")
    print(r"     .\/.                      )")
    print(r"      '\                       /")
    print(r"      _/ \/    ).        )    (")
    print(r"     /#  .!    |        /\    /")
    print(r"     \  C// #  /'-----''/ #  / ")
    print(r"  .   'C/ |    |    |   |    |mrf  ,")
    print(r"  \), .. .'OOO-'. ..'OOO'OOO-'. ..\(,")
    time.sleep(1)
    print("\n")
    print(f"In the heart of a lush,green {Fore.GREEN}{place}{Style.RESET_ALL}")
    print(f"there lived a happy elephant named")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL}. She spent her days splashing")
    print(f"in cool {Fore.GREEN}{liquid}{Style.RESET_ALL} waters, playfully")
    print(f"spraying her friends with her {Fore.GREEN}{body}{Style.RESET_ALL}")
    print("Every morning, as the sun peeked over the")
    print(f"{Fore.GREEN}{thing1}{Style.RESET_ALL}, she would lead her herd")
    print("through the forest, trumpeting cheerful")
    print(f"{Fore.GREEN}{sound}{Style.RESET_ALL} that echoed through the ")
    print(f"{Fore.GREEN}{thing2}{Style.RESET_ALL}. The other animals adored")
    print(f"her for her gentle {Fore.GREEN}{action}{Style.RESET_ALL}")
    print(f"and her infectious. {Fore.GREEN}{place2}{Style.RESET_ALL}")
    print(f"One day, {Fore.GREEN}{name}{Style.RESET_ALL} discovered")
    print(f"a hidden grove filled with the sweetest")
    print(f"{Fore.GREEN}{food}{Style.RESET_ALL}. She loved it!\n\n")

    time.sleep(10)


def mouse_story():
    name = selectItem('name')
    place = selectItem('place')
    liquid = selectItem('liquid')
    body = selectItem('body')
    thing1 = selectItem('thing1')
    sound = selectItem('sound')
    thing2 = selectItem('thing2')
    action = selectItem('action')
    food = selectItem('food')
    place2 = selectItem('place2')

    time.sleep(1)
    print(f"\n{Fore.YELLOW}Loading......................{Style.RESET_ALL}\n")
    time.sleep(2)
    print(r"    (q\_/p)")
    print(r"     /. .\ ")
    print(r"    =\_t_/=   __")
    print(r"     /   \   (")
    print(r"    ((   ))   )")
    print(r"    /\) (/\  /")
    print(r"jgs \  Y  /-'")
    print(r"     nn^nn")
    time.sleep(1)
    print("\n")
    print(f"In a quaint {Fore.GREEN}{place}{Style.RESET_ALL}, there lived")
    print("a speedy mouse named {Fore.GREEN}{name}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} was the fastest mouse")
    print(f"in all the {Fore.GREEN}{place2}{Style.RESET_ALL}, darting through")
    print(f"tall {Fore.GREEN}{thing2}{Style.RESET_ALL}")
    print(f"and narrow {Fore.GREEN}{thing1}{Style.RESET_ALL}")
    print("with incredible swiftness. Every day,")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} challenged")
    print(f"himself to new {Fore.GREEN}{action}{Style.RESET_ALL},")
    print("always seeking a faster route or a quicker turn.")
    print(f"One sunny afternoon, while zipping around the")
    print(f"{Fore.GREEN}{place}{Style.RESET_ALL},  being silly")
    print(f" {Fore.GREEN}{name}{Style.RESET_ALL} noticed a distressed")
    print(f"{Fore.GREEN}{liquid}{Style.RESET_ALL} tangled in a net.\n\n")

    time.sleep(10)


def cat_story():
    name = selectItem('name')
    place = selectItem('place')
    liquid = selectItem('liquid')
    body = selectItem('body')
    thing1 = selectItem('thing1')
    sound = selectItem('sound')
    thing2 = selectItem('thing2')
    action = selectItem('action')
    food = selectItem('food')
    place2 = selectItem('place2')

    time.sleep(1)
    print(f"\n{Fore.YELLOW}Loading......................{Style.RESET_ALL}\n")
    time.sleep(2)
    print(r"""("`-''-/").___..--''"`-._ """)
    print(r""" `6_ 6  )   `-.  (     ).`-.__.`) """)
    print(r""" (_Y_.)'  ._   )  `._ `. ``-..-' """)
    print(r"""   _..`--'_..-_/  /--'_. """)
    print(r"""  ((((.-''  ((((.'  (((.-' """)
    time.sleep(1)
    print("\n")
    print(f"In a charming little {Fore.GREEN}{place}{Style.RESET_ALL}, there")
    print(f"lived a curious cat named {Fore.GREEN}{name}{Style.RESET_ALL}.")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL}  had a sleek coat")
    print(f"and bright green eyes that twinkled with mischief.")
    print(f"Every day, {Fore.GREEN}{name}{Style.RESET_ALL} would set off")
    print(f"on grand adventures, exploring every nook and cranny")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} could find.One misty morning,")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} stumbled upon an old and")
    print(f"forgotten {Fore.GREEN}{thing2}{Style.RESET_ALL}. That was hidden")
    print("behind a dense thicket.\n\n")

    time.sleep(10)


def cow_story():
    name = selectItem('name')
    place = selectItem('place')
    liquid = selectItem('liquid')
    body = selectItem('body')
    thing1 = selectItem('thing1')
    sound = selectItem('sound')
    thing2 = selectItem('thing2')
    action = selectItem('action')
    food = selectItem('food')
    place2 = selectItem('place2')

    time.sleep(1)
    print(f"\n{Fore.YELLOW}Loading......................{Style.RESET_ALL}\n")
    time.sleep(2)
    print(r"              (      )")
    print(r"              ~(^^^^)~")
    print(r"               ) @@ \~_          |\ ")
    print(r"              /     | \        \~ /")
    print(r"             ( 0  0  ) \        | |")
    print(r"              ---___/~  \       | |")
    print(r"               /'__/ |   ~-_____/ |")
    print(r"o          _   ~----~      ___---~")
    print(r"  O       //     |         |")
    print(r"         ((~\  _|         -|")
    print(r"   o  O //-_ \/ |        ~  |")
    print(r"        ^   \_ /         ~  |")
    print(r"               |          ~ |")
    print(r"               |     /     ~ |")
    print(r"               |     (       |")
    print(r"                \     \      /\ ")
    print(r"               / -_____-\   \ ~~-~*")
    print(r"               |  /       \  \ ")
    print(r"               / /         / /")
    print(r"             /~  |       /~  |")
    print(r"             ~~~~        ~~~~")
    time.sleep(1)
    print("\n")
    print(f"On a sunny {Fore.GREEN}{place}{Style.RESET_ALL}")
    print("in the countryside, there lived a funny cow")
    print(f"named {Fore.GREEN}{name}{Style.RESET_ALL}.")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} had a knack for making")
    print(f"everyone laugh with her {Fore.GREEN}{sound}{Style.RESET_ALL}")
    print(f"and playful {Fore.GREEN}{body}{Style.RESET_ALL}. She loved to")
    print(f"wear a straw {Fore.GREEN}{thing1}{Style.RESET_ALL} she found in")
    print(f"barn, tipping it with her {Fore.GREEN}{body}{Style.RESET_ALL} in")
    print(f"a comical greeting to anyone who passed by. One day, while the")
    print(f"farmer was painting the {Fore.GREEN}{thing2}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} decided to join in the fun")
    print(f"She dipped her {Fore.GREEN}{food}{Style.RESET_ALL} in the paint")
    print(f"and swipped it on the {Fore.GREEN}{liquid}{Style.RESET_ALL}.\n\n")

    time.sleep(10)


start_game()
