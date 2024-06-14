# # The script of the game goes in this file.

# # Declare characters used by this game. The color argument colorizes the
# # name of the character.

# define e = Character("Eileen")
# define p = Character("Peeb", color = "#F5610A")

# # The game starts here.

# label start:

#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.

#     scene bg maya
    
#     show bg maya
#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.

#     show peeb happy

#     # These display lines of dialogue.

#     p "Hullo Im Peeb"

#     p "Praise Peeb"

#     # This ends the game.

#     return

image peeb happy = "peeb/happy.png"
image peeb sad = "peeb/sad.png"
image peeb angy = "peeb/angy.png"

image bg maya_room = "bg Maya_2.png"

define peeb = Character("Peeb", color = "#a12216")
define pov = Character("[povname]", image = "llama normal")

define povname = "llama"

label start:
    # python:
    #     povname = renpy.input("What's your name?")
    #     povname = povname.strip()

    #     if not povname:
    #         povname = "Mats"

    scene bg maya_room

    play music "audio/CocoAccordeon.wav" loop
    
    show peeb happy

    peeb "*peeb noises*"

    hide peeb
    show llama normal

    pov "what are u up to peeb"

    hide llama
    show peeb happy

    peeb "Oh hi, how the hell did you get in by the way?"

    peeb "I locked the door"

    hide peeb
    show llama normal

    pov "yeah u did"

    hide llama
    show peeb angy
    stop music

    peeb "..."

    hide peeb
    show llama normal

    pov "..."

    play music "audio/ButTheniThought.wav" loop
    pov "so anyways, i thought to invite u to come with me?"

    hide llama
    show peeb happy

    peeb "Where are you going?"

    hide peeb
    show llama normal

    pov "i was going to this 'new' country sometime soon"

    pov "its like the mayaverse republic or something..."

    pov "we could take the train down to it, i think its only an hour or two away"

    pov "i dont think we need anything to get in, theres like no border patrol"

    hide llama
    show peeb happy

    peeb "Oh, okay, that sounds a bit adventurous, wouldn't you think?"

    hide peeb
    show llama normal

    pov "yeah"

    pov "but id wanna go with u"

    hide llama
    show peeb happy

    peeb "..."

    peeb "That's a bit flattering, don't you think?"

    hide peeb
    show llama normal

    pov "maybe, idk"

    pov "i just wanted to invite u, thats all"

    pov "we can go later or right now if ud want"

    hide llama
    show peeb happy

    peeb "Sounds good then, we can go now"

    return