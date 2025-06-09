# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Matthew", color="#f4c473")
image Battler Smirking Hand = "Battler Smirking Hand.png"
image Battler Blinking Hand = "Battler Blinking Hand.png"
transform double_size:
    zoom 2.0

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    play music "Fishy Aroma.flac"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    "The spring winds come in, and the taste of summer is in the air."
    "This day is a perfect day to go and visit the museum."
    "For some reason you see..."
    "I cannot resist the museum."
    "Every day I dream about going there and seeing what they have to offer"
    show Battler Blinking Hand at double_size
    m "Ahhh What a Nice Day is is today!"
    hide Battler Blinking Hand
    "I had a look at my phone"
    show Battler Smirking Hand

    m "Once you add a story, pictures, and music, you can release it to the world!"
    # This ends the game.

    return
