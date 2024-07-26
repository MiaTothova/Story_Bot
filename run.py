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
    print("Welcome to Story Bot!\n")
    print("I have 4 stories to choose from and YOU pick the words!")
    print("Here they are: \n")
    print("1. The Happy Elephant")
    print("2. The Speedy Mouse")
    print("3. The Curious Cat")
    print("1. The Funny Cow")

start_game()


def elephant_story():
    name = selectItem = ('name')
    place = selectItem = ('place')
    liquid = selectItem = ('liquid')
    body = selectItem = ('body')
    thing1 = selectItem = ('thing1')
    sound = selectItem = ('sound')
    thing2 = selectItem = ('thing2')
    action = selectItem = ('action')
    food= selectItem = ('food')
    place2 = selectItem = ('place2')

    print(f"\n In the heart of a lush, green {place}, there lived a happy elephant named {name}.")
    print(f" She spent her days splashing in cool {liquid} waters, playfully spraying her friends with her {body}.")
    print(f"Every morning, as the sun peeked over the {thing1}, {name} would lead her herd through the forest,")
    print(f"trumpeting cheerful {sound} that echoed through the {thing2}.")
    print(f"The other animals adored her for her gentle {action} and her infectious {place2}.")
    print(f"One day, {name} discovered a hidden grove filled with the sweetest {food}.")
    
    


def mouse_story():
    name = selectItem = ('name')
    place = selectItem = ('place')
    liquid = selectItem = ('liquid')
    body = selectItem = ('body')
    thing1 = selectItem = ('thing1')
    sound = selectItem = ('sound')
    thing2 = selectItem = ('thing2')
    action = selectItem = ('action')
    food= selectItem = ('food')
    place2 = selectItem = ('place2')

    print(f"In a quaint {place}, there lived a speedy mouse named {name}.")
    print(f"{name} was the fastest mouse in all the {place2}, darting through tall {thing2} and narrow {thing1} with incredible swiftness.")
    print(f"Every day, {name} challenged himself to new {action}, always seeking a faster route or a quicker turn.")
    print(f" One sunny afternoon, while zipping around the {place}, {name} noticed a distressed {liquid} tangled in a net.")



def cat_story():
    name = selectItem = ('name')
    place = selectItem = ('place')
    liquid = selectItem = ('liquid')
    body = selectItem = ('body')
    thing1 = selectItem = ('thing1')
    sound = selectItem = ('sound')
    thing2 = selectItem = ('thing2')
    action = selectItem = ('action')
    food= selectItem = ('food')
    place2 = selectItem = ('place2')

    print(f"In a charming little {place}, there lived a curious cat named {name}.")
    print(f"{name} had a sleek coat of {thing} and bright green {body} that twinkled with {food}.")
    print(f"Every day, {name} would set off on grand {place2}, exploring every nook and cranny {name} could find.")
    print(f"One misty morning, {name} stumbled upon an old, forgotten {thing2} hidden behind a dense thicket.")
    


def cow_story():
    name = selectItem = ('name')
    place = selectItem = ('place')
    liquid = selectItem = ('liquid')
    body = selectItem = ('body')
    thing1 = selectItem = ('thing1')
    sound = selectItem = ('sound')
    thing2 = selectItem = ('thing2')
    action = selectItem = ('action')
    food= selectItem = ('food')
    place2 = selectItem = ('place2')

    print(f"On a sunny {place} in the countryside, there lived a funny cow named {name}.")
    print(f"{name} had a knack for making everyone laugh with her silly {sound} and playful {body}.")
    print(f"She loved to wear a straw {thing} she found in the barn, tipping it with her {body} in a comical greeting to anyone who passed by.")
    print(f"One day, while the farmer was painting the {thing2}, {name} decided to join in the fun.")
    print(f"She dipped her {food} in the paint bucket and began to swipe it across the {liquid}.")
