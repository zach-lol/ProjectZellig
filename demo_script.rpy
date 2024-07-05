# image peeb happy = "peeb/happy.png"
# image peeb sad = "peeb/sad.png"
# image peeb angy = "peeb/angy.png"

# image bg maya_room = "bg Maya_2.png"
# image bg unpeeb = "other/bg Germany.jpg"

# define peeb = Character("Peeb", color = "#a12216")
# define pov = Character("[povname]", image = "llama normal")

# define povname = "llama"

label dont_start:
    # python:
    #     povname = renpy.input("What's your name?")
    #     povname = povname.strip()

    #     if not povname:
    #         povname = "Mats"
    # scene bg maya_room

    "In the beginning God created the heaven and the earth."
    "And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters."
    "And God said, Let there be light: and there was light."
    "And God saw the light, that it was good: and God divided the light from the darkness."
    "And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day."

    scene bg maya_room
    with Fade(0.5, 0.0, 0.5)

    play music "audio/CocoAccordeon.wav" loop
    
    show peeb happy

    peeb "*peeb noises*"

    hide peeb
    show llama normal

    pov "what are u up to peeb"

    hide llama
    show peeb happy

    peeb "Oh hi, how the hell did you get in by the way?"
    peeb "Oh hk;ijfdsnlkdffvkjay?"

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