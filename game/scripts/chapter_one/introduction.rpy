image peeb happy = "peeb/happy.png"
image peeb sad = "peeb/sad.png"
image peeb angy = "peeb/angy.png"

image bg maya_room = "bg Maya_2.png"

define peeb = Character("Peeb", color = "#a12216")
define pov = Character("[povname]", image = "llama normal")

define povname = "llama"

label start:
    scene bg chapter_one
    with Fade(0.5, 3.0, 0.5)

    $ renpy.pause(3.0, hard=False)

    scene bg c1_netherlands_1
    with Fade(0.5, 0.0, 0.5)

    play music "audio/BokuNoSenpaiNieuw.wav"

    "When you received the news that your family had to move to another continent, you couldn't help but feel sad about it."
    "Everything that was once yours, your friends, your relatives, all would be far from you."
    "You're forced to stay where you knew you didn't belong for who knows how long."

    scene black

    "You were resentful."
    # stop music fadeout 1.0

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