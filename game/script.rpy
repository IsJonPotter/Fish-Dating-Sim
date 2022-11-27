# The script of the game goes in this file.

# Declare sprite variables
image Crush:
    "Girl.png"

image Isaac:
    "Isaac.png"

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Crush")
define m = Character("MC")


# The game starts here.

label start:

    # Scene 1 - Confession

    scene bg lake

    show Crush

    "On a peaceful afternoon near the pier beach in Lake Well,
    a girl in a pink dress is standing near the entrance of the pier as if she is waiting for someone to show up.
    And that someone happened to be me."

    m "(She's really here.)"

    "'Bzzz bzzz'"

    "I got a message on my phone. I checked and saw that my friend messaged me “Good luck!”."

    "Today I'm going to finally ask her out! The girl in the pink dress is the prettiest girl I've ever seen."

    "I first saw her with friends walking by every weekend near the pier while I was helping my family unload the fish we caught here in the lake.
    We've made a couple of eye contacts before and we would always look away."

    "I first saw her with friends walking by every weekend near the pier while I was helping my family unload the fish we caught here in the lake.
    We've made a couple of eye contacts before and we would always look away."

    "I have made sure I've showered and dressed neatly for this day! I hope I don't smell like fish.
    Oh my god, I'm so nervous. No, I can't sweat right now after the effort I put in. It's time to go up to her."

    m "Gulp. H-hi!"

    "The girl turned around where the voice came from."

    c "Oh, I've seen you before. Are you the guy who fishes on that boat over there?"

    "The girl pointed out the boat that is owned by my family."

    c "Wait, are you the one who my friend set me up to come here? What's up?"

    "She smiles at me with her head tilted as if curious."

    "'Ba-dum ba-dum'"

    m "(Calm down, heart)"

    "I told her how she has been on my mind since the first time I saw her. "

    "..."

    m "(I did it!)"

    "..."

    c "Oh, I'm sorry but I am not into fishy smelling guys... I appreciate your feelings tho…"

    "All of a sudden my heart stops and I start to feel as if there's something in my throat."

    m "B-but I showered before coming here!"

    c "Yeah, no, I'm sorry, I'm just not interested in you."

    m "..."

    m "(Ack! I felt as if something punched the soul out of my body and I'm left speechless from the shock.)"

    "The girl in the pink dress looks uncomfortable while looking away.
    I don't know how long I was quiet for but this sure made it awkward for the both of us."

    "...I gotta say something."

    m "O-oh okay, y-yeah, it's no problem. Thanks for your time coming here..."

    c "Yeah, thanks for telling me. But hey, no worries, I'm sure there are plenty of fish in the sea! Oh, no pun intended."

    hide Crush

    scene bg black

    "‘BAM!’"

    "(Huh?)"

    "(I’m somehow flying up in the air away from her?)"
    "Next thing I notice, she has her hands covering her mouth with her eyes wide open for some reason. I looked in another direction and finally realized I got hit by that truck. "

    "And then I plunge into the Lake Well."

    scene bg sea dark

    "(Oh no, I gotta get out of the water!)"

    "…"

    "(My body can’t move.)"

    "(Is it from the hit?)"

    scene bg sea

    "…"

    "(Wow, it’s kind of pretty peaceful here.)"

    "(I do recall that Lake Well can grant you a wish if you did something but I don’t remember what.) "

    scene bg sea light

    "(My body is getting cold…I guess this is it.)"

    "(At the very least my wish is …)"

    scene bg white

    "(My mind is starting to fade and I let my eyes closed to sleep.)"


    # This ends the game.

    return
