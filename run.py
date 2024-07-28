
# Dictionary
word_choice = {
    'name' : ['Ella', 'Max', 'Whiskers', 'Daisy', 'Sparkle', 'Flash', 'Giggles', 'Bubbles', 'Snickers', 'Twinkle'],
    'place': ['jungle', 'amusement park','spaghetti factory', 'rollercoaster', 'library', 'spaceship', 'giant pillow forth', 'candy store', 'zoo','aquarium'],
    'liquid': ['river', 'pudding', 'chocolate', 'lemonade', 'milkshake', 'raibow', 'bubble', 'glitter', 'confetti', 'jelly'],
    'body': ['trunk', 'tail', 'paw', 'ear', 'nose', 'hoof', 'fin', 'wing', 'antenna', 'whisker'],
    'thing1': ['cereal bowl', 'treasure chest', 'ocean of pudding', 'circus tent', 'popcorn cloud', 'smoothie sea', 'cotton candy sky', 'giat pizza', 'pancake stack'],
    'sound': ['fart noises', 'chicken clucks', 'robot beeps', 'disco beats', 'alien whispers', 'rap verses', 'karaoke songs', 'banjp solos', 'quacking ducks'],
    'thing2': ['playgrounds', 'trees', 'sandcastles', 'ball pits', 'snow globes', 'race tracks', 'toy boxes', 'candy lands', 'swimming pools'],
    'action': ['dance moves', 'laugh', 'baloon animals', 'face paint', 'tickles', 'juggling', 'magic tricks', 'pranks', 'cartwheels'],
    'food': ['marshmallows', 'glitter', 'bananas', 'rainbows', 'kites', 'ice cream cones', 'sprinkles', 'cupcakes'],
    'place2': ['horizon', 'treasure chest', 'ocean of pudding', 'pancake stack', 'giant pizza', 'circus tent', 'popcorn cloud', 'smoothie sea', 'candy sky']
    
}



def start_game():
    while True:  # Start an infinite loop to show menu continuously
        print("Welcome to Story Bot!\n")
        print("I have 5 stories to choose from and YOU pick the words!")
        print("Here they are: \n")
        print("1. The Happy Elephant")
        print("2. The Speedy Mouse")
        print("3. The Curious Cat")
        print("4. The Funny Cow")
        print("5. End Game")

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
            print("\n\nSee you next time!")
            break  # Break out of the loop to end the game
        else:
            print("Please enter a valid option! \n\n")
            

def selectItem(key):
    items = word_choice[key]  # Get the list of items for the given key
    max_index = len(items)  # This is the maximum index we can select

    # Print the options for the user
    print(f"Select a '{key}' from the list below by entering the corresponding number:")
    for index, item in enumerate(items, start=1):
        print(f"{index}. {item}")

    while True:  # Start an infinite loop to keep asking until a valid input is given
        try:
            selection = int(input(f"Enter your choice (1-{max_index}): "))  # Ask user for input
            if 1 <= selection <= max_index:  # Check if the selection is within the valid range
                return items[selection - 1]  # Return the selected item
            else:
                print(f"Please enter a number between 1 and {max_index}.")  # Inform the user about the valid range
        except ValueError:
            print("Invalid input. Please enter a number.")  # Handle the case where input is not a number





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

    print(f"\n In the heart of a lush, green {place}, there lived a happy elephant named {name}.")
    print(f" She spent her days splashing in cool {liquid} waters, playfully spraying her friends with her {body}.")
    print(f"Every morning, as the sun peeked over the {thing1}, {name} would lead her herd through the forest,")
    print(f"trumpeting cheerful {sound} that echoed through the {thing2}.")
    print(f"The other animals adored her for her gentle {action} and her infectious {place2}.")
    print(f"One day, {name} discovered a hidden grove filled with the sweetest {food}.")
    
    


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

    print(f"In a quaint {place}, there lived a speedy mouse named {name}.")
    print(f"{name} was the fastest mouse in all the {place2}, darting through tall {thing2} and narrow {thing1} with incredible swiftness.")
    print(f"Every day, {name} challenged himself to new {action}, always seeking a faster route or a quicker turn.")
    print(f" One sunny afternoon, while zipping around the {place}, {name} noticed a distressed {liquid} tangled in a net.")



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

    print(f"In a charming little {place}, there lived a curious cat named {name}.")
    print(f"{name} had a sleek coat and bright green eyes that twinkled with mischief.")
    print(f"Every day, {name} would set off on grand adventures, exploring every nook and cranny {name} could find.")
    print(f"One misty morning, {name} stumbled upon an old, forgotten {thing2} hidden behind a dense thicket.")

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

    print(f"On a sunny {place} in the countryside, there lived a funny cow named {name}.")
    print(f"{name} had a knack for making everyone laugh with her silly {sound} and playful {body}.")
    print(f"She loved to wear a straw {thing1} she found in the barn, tipping it with her {body} in a comical greeting to anyone who passed by.")
    print(f"One day, while the farmer was painting the {thing2}, {name} decided to join in the fun.")
    print(f"She dipped her {food} in the paint bucket and began to swipe it across the {liquid}.")


start_game()