import time
from colorama import Fore, Style

# Dictionary
word_choice = {
    'name' : ['Ella', 'Max', 'Whiskers', 'Daisy', 'Sparkle', 'Flash', 'Giggles', 'Bubbles', 'Snickers', 'Twinkle'],
    'place': ['jungle', 'amusement park','spaghetti factory', 'rollercoaster', 'library', 'spaceship', 'giant pillow forth', 'candy store', 'zoo','aquarium'],
    'liquid': ['river', 'pudding', 'chocolate', 'lemonade', 'milkshake', 'rainbow', 'bubble', 'glitter', 'confetti', 'jelly'],
    'body': ['trunk', 'tail', 'paw', 'ear', 'nose', 'hoof', 'fin', 'wing', 'antenna', 'whisker'],
    'thing1': ['cereal bowl', 'treasure chest', 'ocean of pudding', 'circus tent', 'popcorn cloud', 'smoothie sea', 'cotton candy sky', 'giant pizza', 'pancake stack'],
    'sound': ['fart noises', 'chicken clucks', 'robot beeps', 'disco beats', 'alien whispers', 'rap verses', 'karaoke songs', 'banjo solos', 'quacking ducks'],
    'thing2': ['playgrounds', 'trees', 'sandcastles', 'ball pits', 'snow globes', 'race tracks', 'toy boxes', 'candy lands', 'swimming pools'],
    'action': ['dance moves', 'laugh', 'balloon animals', 'face paint', 'tickles', 'juggling', 'magic tricks', 'pranks', 'cartwheels'],
    'food': ['marshmallows', 'glitter', 'bananas', 'rainbows', 'kites', 'ice cream cones', 'sprinkles', 'cupcakes'],
    'place2': ['horizon', 'treasure chest', 'ocean of pudding', 'pancake stack', 'giant pizza', 'circus tent', 'popcorn cloud', 'smoothie sea', 'candy sky']
    
}


def welcome():
     print(f"{Fore.YELLOW}Welcome to Story Bot!{Style.RESET_ALL}\n")
     time.sleep(2)
     user = input("Please enter your name : \n")
     print(f"Hi {Fore.YELLOW}{user}{Style.RESET_ALL}! Let's pick a story. \n \n")
     time.sleep(2)


def start_game():
    welcome()
    while True:  # Start an infinite loop to show menu continuously
        print(f"{Fore.YELLOW}I have 4 stories to choose from and YOU pick the words!{Style.RESET_ALL}\n")
        time.sleep(2)
        print(f"{Fore.YELLOW}Here they are:{Style.RESET_ALL} \n")
        print("1. The Happy Elephant")
        print("2. The Speedy Mouse")
        print("3. The Curious Cat")
        print("4. The Funny Cow")
        print("5. End Game \n")

        choice = input("Choose a story by entering a number, or end the game by entering 5: ")
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
            print(f"{Fore.RED}Please enter a valid option!{Style.RESET_ALL}\n\n")
            

def selectItem(key):
    items = word_choice[key]  # Get the list of items for the given key
    max_index = len(items)  # This is the maximum index we can select

    # Print the options for the user
    print(f"{Fore.YELLOW}Select a '{key}' from the list below by entering the corresponding number:{Style.RESET_ALL}")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    while True:  # Start an infinite loop to keep asking until a valid input is given
        try:
            selection = int(input(f"Enter your choice (1-{max_index}): "))  # Ask user for input
            if 1 <= selection <= max_index:  # Check if the selection is within the valid range
                return items[selection - 1]  # Return the selected item
            else:
                print(f"{Fore.RED}Please enter a number between 1 and {max_index}.{Style.RESET_ALL}")  # Inform the user about the valid range
        except ValueError:
            print(f"{Fore.RED}Invalid input. Please enter a number.{Style.RESET_ALL}")  # Handle the case where input is not a number





def elephant_story():
    # selectItem prints selected words into the story
    name = selectItem('name')
    place = selectItem('place')
    liquid = selectItem('liquid')
    body = selectItem ('body')
    thing1 = selectItem('thing1')
    sound = selectItem('sound')
    thing2 = selectItem('thing2')
    action = selectItem('action')
    food= selectItem('food')
    place2 = selectItem('place2')

    time.sleep(1)
    print(f"\n{Fore.YELLOW}Loading.............................{Style.RESET_ALL}")
    time.sleep(2)

    print(f"\n In the heart of a lush, green {Fore.GREEN}{place}{Style.RESET_ALL}, there lived a happy elephant named {Fore.GREEN}{name}{Style.RESET_ALL}.")
    print(f"She spent her days splashing in cool {Fore.GREEN}{liquid}{Style.RESET_ALL} waters, playfully spraying her friends with her {Fore.GREEN}{body}{Style.RESET_ALL}.")
    print(f"Every morning, as the sun peeked over the {Fore.GREEN}{thing1}{Style.RESET_ALL}, {Fore.GREEN}{name}{Style.RESET_ALL} would lead her herd through the forest,")
    print(f"trumpeting cheerful {Fore.GREEN}{sound}{Style.RESET_ALL} that echoed through the {Fore.GREEN}{thing2}{Style.RESET_ALL}.")
    print(f"The other animals adored her for her gentle {Fore.GREEN}{action}{Style.RESET_ALL} and her infectious {Fore.GREEN}{place2}{Style.RESET_ALL}.")
    print(f"One day, {Fore.GREEN}{name}{Style.RESET_ALL} discovered a hidden grove filled with the sweetest {Fore.GREEN}{food}{Style.RESET_ALL}.\n\n")

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
    print(f"\n{Fore.YELLOW}Loading.............................{Style.RESET_ALL}")
    time.sleep(2)

    print(f"\n In a quaint {Fore.GREEN}{place}{Style.RESET_ALL}, there lived a speedy mouse named {Fore.GREEN}{name}.{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} was the fastest mouse in all the {Fore.GREEN}{place2}{Style.RESET_ALL}, darting through tall {Fore.GREEN}{thing2}{Style.RESET_ALL} and narrow {Fore.GREEN}{thing1}{Style.RESET_ALL} with incredible swiftness.")
    print(f"Every day, {Fore.GREEN}{name}{Style.RESET_ALL} challenged himself to new {Fore.GREEN}{action}{Style.RESET_ALL}, always seeking a faster route or a quicker turn.")
    print(f"One sunny afternoon, while zipping around the {Fore.GREEN}{place}{Style.RESET_ALL}, {Fore.GREEN}{name}{Style.RESET_ALL} noticed a distressed {Fore.GREEN}{liquid}{Style.RESET_ALL} tangled in a net.\n\n")

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
    food= selectItem('food')
    place2 = selectItem('place2')

    time.sleep(1)
    print(f"\n{Fore.YELLOW}Loading.............................{Style.RESET_ALL}")
    time.sleep(2)

    print(f"\n In a charming little {Fore.GREEN}{place}{Style.RESET_ALL}, there lived a curious cat named {Fore.GREEN}{name}{Style.RESET_ALL}.")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} had a sleek coat and bright green eyes that twinkled with mischief.")  
    print(f"Every day, {Fore.GREEN}{name}{Style.RESET_ALL} would set off on grand adventures, exploring every nook and cranny {Fore.GREEN}{name}{Style.RESET_ALL} could find.") 
    print(f"One misty morning, {Fore.GREEN}{name}{Style.RESET_ALL} stumbled upon an old, forgotten {Fore.GREEN}{thing2}{Style.RESET_ALL} hidden behind a dense thicket.\n\n")

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
    food= selectItem('food')
    place2 = selectItem('place2')

    time.sleep(1)
    print(f"\n{Fore.YELLOW}Loading.............................{Style.RESET_ALL}")
    time.sleep(2)

    print(f"\n On a sunny {Fore.GREEN}{place}{Style.RESET_ALL} in the countryside, there lived a funny cow named {Fore.GREEN}{name}{Style.RESET_ALL}.")
    print(f"{Fore.GREEN}{name}{Style.RESET_ALL} had a knack for making everyone laugh with her silly {Fore.GREEN}{sound}{Style.RESET_ALL} and playful {Fore.GREEN}{body}{Style.RESET_ALL}.")
    print(f"She loved to wear a straw {Fore.GREEN}{thing1}{Style.RESET_ALL} she found in the barn, tipping it with her {Fore.GREEN}{body}{Style.RESET_ALL} in a comical greeting to anyone who passed by.")
    print(f"One day, while the farmer was painting the {Fore.GREEN}{thing2}{Style.RESET_ALL}, {Fore.GREEN}{name}{Style.RESET_ALL} decided to join in the fun.")
    print(f"She dipped her {Fore.GREEN}{food}{Style.RESET_ALL} in the paint bucket and began to swipe it across the {Fore.GREEN}{liquid}{Style.RESET_ALL}. \n\n")

    time.sleep(10)

start_game()