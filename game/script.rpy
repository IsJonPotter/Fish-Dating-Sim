# The script of the game goes in this file.

# Declare sprite variables
image Crush:
    "Girl.png"

image Truckkun:
    "Truck-kun.png"

image Isaac:
    "Isaac.png"

image Clamantha:
    "Clamantha.png"

image Dr Shrump:
    "DrShrimp.png"

image Whitefish:
    "BeatenUpFish.png"

image Kole:
    "Kole_neautral_speaking_01.png"

image Blobby:
    "Blobby_HAPPY.png"

image Jawshua:
    "Jawshua.png"

image CGisaac:
    "CG_ISAAC.png"

image CGkole:
    "CG_KOLE.png"

image Whitefish1:
    "GenericFish.png"    

image Host:
    "Krilliam.png"
#$ kolePoints = 0;
#$ isaacPoints = 0;

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define c = Character("Crush")
define m = Character("MC")
define cl = Character("Clamantha")
define di = Character("Dr Shrimp")
define d = Character("Dr Shrump")
define i = Character("Isaac")
define who = Character("???")
define wf = Character("Whitefish")
define k = Character("Kole")
define bd = Character("Blind date")
define j = Character("Jawshua")
define b = Character("Blobby")
define an = Character("Announcer")
define cr = Character("Crowd")

# The game starts here.

default kolePoints = 0
default isaacPoints = 0
label start:
# Intro

    stop music  fadeout 1.0
    # Scene 1 - Confession
    scene bg lake

    "On a busy afternoon near the pier beach in Lake Well, "
    #----neutral smiling girl
    show Crush

    "a girl in a pink dress is standing near the entrance of the pier as if she is waiting for someone to show up. "

    "And that someone is me."

    m "(She's really here.)"

    "'Bzzz bzzz'"

    "I got a message on my phone. I checked and saw that my friend messaged me “Good luck!”."

    "Today I'm going to finally ask her out! The girl in the pink dress is the prettiest girl I've ever seen."

    "I first saw her with friends walking by every weekend near the pier while I was helping my family unload the fish we caught here in the lake.
    We've made a couple of eye contacts before and we would always look away."

    "My heart would beat so fast every time that happens. I’ve heard before that when you and the other person look away after an eye contact it usually means both are interested in each other."

    "I have made sure I’ve showered and dressed neatly for this day! I hope I don’t smell like fish.
    Oh my god, I’m so nervous. No, I can’t sweat right now after the effort I put in. It’s time to go up to her."

    m "{i}Gulp{/i}. H-hi!"

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

    c "Oh, I'm sorry but I am not into fishy smelling guys... I appreciate your feelings though…"

    "All of a sudden my heart stops and I start to feel as if there's something in my throat."

    m "B-but I showered before coming here!"

    c "Yeah, no, I'm sorry, I'm just not interested in you."

    m "..."

    m "(Ack! I felt as if something punched the soul out of my body and I'm left speechless from the shock.)"

    #---add girl with uncomfortable face image

    "The girl in the pink dress looks uncomfortable while looking away.
    I don't know how long I was quiet for but this sure made it awkward for the both of us."

    "(...I gotta say something.)"

    m "O-oh okay, y-yeah, it's no problem. Thanks for your time coming here..."

    c "Yeah, thanks for telling me. But hey, no worries, I'm sure there are plenty of fish in the sea! Oh, no pun intended."

    scene bg black

    stop music

    "'BAM!'"
    scene bg white
    
    m "(Huh?)"

    scene bg lake
    show Crush:
        xalign 0.2
        yalign 0.5
        zoom 0.5


    "(I'm somehow flying up in the air away from her?)"

    "Next thing I notice, she has her hands covering her mouth with her eyes wide open for some reason."
    
    show Truckkun:
        xalign 0.5

    "I looked in another direction and finally realized I got hit by that truck."

    scene bg white
    "And then I plunge into the Lake Well."

    scene bg sea dark

    "(Oh no, I gotta get out of the water!)"

    "..."

    "(My body can't move.)"

    "(Is it from the hit?)"

    scene bg sea

    play music sad

    "..."

    "(Huh, it's kind of pretty peaceful here...)"

    "(I do recall that Lake Well can grant you a wish if you did something but I don't remember what.) "

    scene bg sea light

    "(My body is getting cold…I guess this is it.)"

    "(At the very least my wish is …)"


    scene bg white

    "(My mind is starting to fade and I let my eyes rest.)"

    "..."


    "..."


    "..."


    # Scene 2 - Truck-kun's Wrath

    #play music main fadein 2.0 fadeout 2.0

    m "(Hm? Where am I?)"

    scene bg infirmary

    "I slowly open my eyes and find myself at a kind of weird infirmary it looks like. Am I still alive?"

    show Clamantha:
        xalign 0.5
        yalign 0.5
        zoom 1.2

    m "(A clam?)"

    who "Omg, you woke up! Let me call the Doctor."

    who "Don't try to move too much! Let me call the Doctor."

    m "(The Clam talks? Why does it have a bow?)"

    "The clam goes to call the doctor."

    who "Here they are, Doctor Shrimp. They just woke up after being crushed by a U.S.O."

    m "(U.S.O.?"
    #clam and doctor shows up left and right on the screen
    show Clamantha:
        xalign 0.1
        yalign 0.5
        zoom 0.8

    show Dr Shrump:
        zoom 1.35
        xalign 0.75
        yalign 1.0

    m "(And now a shrimp shows up?)"

    di "Thank you, Clamantha, for calling me right up."
    hide Clamantha
    show Dr Shrump:
        zoom 1.40
        xalign 0.5
    di "How are you feeling? Do you have any headache? Physical pain?"

    m "No… I don't feel anything weird."
    
    m "(Which is in fact weirder, why am I in a fish body?)"

    "Dr.Shrimp checks my eyes and other places on my head."
    #doc on the right
    show Dr Shrump:
        zoom 1.35
        xalign 0.9
        yalign 1.0

    di "You don't have anything life threathening but come visit me if you experience any sort of pain. You are free to go."
    #clam on the left
    show Clamantha:
        xalign 0.1
        yalign 0.5
        zoom 0.8   

    cl "Oh, thank you so much Dr.Shrimp!"

    d "It's actually Dr. Shrump. you're welcome."

    "I was getting up from the bed when suddenly someone crashed into the room."

    # Scene 3 - Infirmary room - Isaac

    play music isaac fadein 2.0

    hide Clamantha
    hide Dr Shrump

    who  "I-I'M SO SORRwwYYYY!!!!!!!!!!!"

    who "I-I-I didn't know this would happen! If else I wouldn't have-"

    show Clamantha:
        xalign 0.1
        yalign 0.5
        zoom 0.9

    show Isaac:
        xalign 0.9
        yalign 0.6

    cl  "Oh gosh, not this weirdo again..."

    m "(Who's this guy? He looks familiar...)"

    m "The guy starts explaining how he used a massive weird thing to call the U.S.O. that dove into the water and crashed into me."

    m "Wait a minute..."

    m "What if the U.S.O. is the same thing that crushed my real human self?"

    "..."

    m "(Nah no way.)"

    m "(This little guy seems harmless.)"

    cl "Come on mc, don't listen to this nerdy-nonsense."

    who "W-wait but I really needed to explain this!"

    cl "Yeah, yeah, whatever."

    hide Clamantha
    hide Isaac

    scene bg white

    "Whoosh"

    scene bg hallway
    play music main
    show Clamantha:
        yalign 0.5
        xalign 0.5
        zoom 1.0



    "Me and Clamantha got out of the infirmary."

    cl "Listen up mc, I just need to make a lil more preparations, but the thing we talked about earlier still stands."

    cl "Go ahead to the classroom, I'll join you in a bit. I need to drop something off first."

    m "Oookay?"

    "(I wonder what she is talking about.)"

    "Clamantha leaves."

    "(Wait, where is my classroom?)"

    "(Clamanthaaaaa, come back!)"

    # Scene 4 - School yard - Kole

    scene schoolyard
    "..."

    "This doesn’t look like it will lead to my classroom."

    "I ended up being what it seems to be the schoolyard with all the rock and reefs surrounding the building here."

    m "Hmmm… yep. I’m lost. I have no idea where my classroom is. Time to turn back."

    "EEK!"
    play music kole fadein 7.0
    "(What was that sound?)"

    "HELP!"

    "(Sounds like someone is in trouble.)"

    "I swim as fast as I can to where the voice is."

    m "HEY, someone needs help?"

    who "CRAP. Someone is coming, let’s get going."

    "(I hear whispers over there.)"

    "I swim as fast as I can until I see the back of a fish facing another one on the ground."

    "I tried to brake by flapping my fins but due to the water resistance I’m guess I’m still not used to this fish body."

    "Because I can't stop I'm going crash into the fish with a black cardigan."

    m "Hey you! Watch out!"

    "‘THUD!’"

    m "Ow, my head..."

    "I hit head first at the other fish and I see it’s only us three."
    show Whitefish:
        xalign 1.0
        yalign 0.5
    show Kole:
        zoom 1.20    
        
    "The fish with a black cardigan with sleeves rolled up a bit is an orange goldfish and the one sitting on the ground is a whitefish who is covered in bruises."

    "I look back and forth between the two of them."



    m "..."


    who "..."

    who "Are you for real?"

    m "N-no, I'm so sorry! I'll get up now!"

    show Kole:
        zoom 1.0
        xalign 0.25


    hide Whitefish

    "I look away from the goldfish’s scary eyes while brushing off the dirt off me."

    "(What's up with this guy? Is he some sort of mafia boss?)"

    "(This is bad... I didn’t expect to come across a school bully...)"


    who "I don't want a single word to go out of your mouth about this. If not, you’ll be introduced to my fists."

    show Whitefish:
        xalign 0.75
        yalign 0.5
        
    who "K-Kole."

    show Kole:
        zoom 1.0
        xalign 0.30

    "Kole turns to the whitefish."

    "(So his name is Kole.)"

    m "Why are you so violent about it? That guy looks pretty weak on their own."

    k "What are you talking about? You really are responding this time,huh? Last time you sure looked like a scared little betta fish. You are not scared this time?"

    "(Oh no I have his attention. Have I met this guy before? Oopsies...)"

    m "Ahem, alright. I won't say anything about this. But I still think you shouldn't be hitting people for free at school."

    m "(Ack, why did I say that? I’m going to be beaten up!)"

    k "Yeah yeah yeah, as if you knew anything about me."

    "Kole rolls his eyes and turns back to the whitefish."

    "(Now is my chance to get away!)"
    show Kole:
        zoom 1.0
        xalign 0.28
    k "If you’re still quiet and have nothing to do– huh? They ran off again."

# Scene 5 -  Classroom
    play music main
    scene bg hallway

    "Pant, pant."

    "(I think I’m far away enough. Ugh, that poor whitefish...)"

    "(Where are the teachers or security guards around?)"

    "(Wait, where am I now?)"

    cl "Where were you this whole time?"

    m "Huh?"

    "I turn and see the familiar clam silhouette."

    show Clamantha:
        yalign 0.5
        xalign 0.5
        zoom 1.0
    

    cl "Didn’t I tell you to go ahead without me? Why weren’t you here before me?"

    m "Ha ha ha."

    cl "...What’s with that nervous chuckle. Don’t tell me you got yourself in trouble again?"

    m "Funny thing you say..."

    cl "Oh no, tell me what happened inside the classroom. Luckily we have independent study before our next class."


    m "Alright."

    "We go inside the classroom and I begin to tell her the tales of my adventure after we splitted up."

    scene bg classroom

    show Clamantha:
        yalign 0.5
        xalign 0.5


    cl "..."

    "She looks like she’s processing everything of what I told her."

    cl "You don’t remember who that goldfish is?"

    m "Ahaha, it sounded like I met one of them before."

    # play music kole

    cl "The goldfish you met is named Kole, he transferred here a while ago."

    cl "One day, you were late for class because you overslept. "

    cl "You swam around a corner with your breakfast in your mouth still and bumped into Kole. "

    cl "Afterwards you said you were so scared of his angry face that you blanked out and didn’t remember anymore how you got here. "

    cl "We then later found out he is the new transfer student to the other classroom."

    m "..."

    "(What kind of story is that?)"

    cl "As for the whitefish, they are a goner. Forget about them. Rumor has it that Kole transferred here because he beat all the students up in their previous school. So I recommend steering clear away from them. "

    "(Yikes! You don’t have to tell me.)"

    play music main

    cl "So anyway, do you even remember what we were talking about before you became unconscious?"

    m "I’m sorry, I don’t."

    "(Obviously I don’t.)"

    cl "That's what I thought. You looked kinda confused when I mentioned the plan earlier."

#--smiling Clam
    cl "Weeeellll, it’s about the blind dates I suggested that I will set up."

    m "For who?"

    cl "Obviously, you."

    "(Wait, what?)"

    cl "You keep falling for the fishes for their looks and then you get heartbroken from rejections!"

    m "Hahaha, for real?"

    "I bursted out laughing silently on how superficial this body’s owner – oh wait."

    hide Clamantha

    play music sad fadein 1.0 fadeout 2.0

    scene bg lake
    show Crush

    "Memories of my crush flashes through my eyes and I can’t help but to feel bad again about her comment about my smell."

    hide Crush

    play music main fadein 1.0

    scene bg classroom
    show Clamantha:
        yalign 0.5
        xalign 0.5

    "My eyes begin to become blurry from tearing up underwater somehow."

    "Clamantha noticed my sudden silence after my laughter."

    cl "Yes for real, did you really forget? Oh no, did you just remember it?"

    cl "Look, I know a few good fishes out here who you will get along with for sure! So please, at least try to meet them. You don’t have to date them immediately."

    "(All my life I have been chasing people with good looks and they always turn out not who I thought they were. I mean what do I have to lose? I’m here now so might as well try this time.)"

    m "Okay. Set me up for a blind date."

    cl "Really!? Great! I’ll make sure to set up very soon before the prom this coming month."

    "Clamanta looks very excited to be playing as the matchmaker."

    m "Wait, prom? We have a prom here?"

    cl "Yes, remember? This year’s prom will have The Hook show up."

    m "What is The Hook?"

    "(Sounds kind of ominous.)"

    cl "Well, The Hook are the organizers hired by the school. Two fish are chosen by The Hook and they get ascended."

    "(...)"

    m "Ascended? Where? To the surface?"

    cl "No, the pair get to sit on the hook together, you’ll be lifted up with pretty lights on you while everyone cheers."

    m "That’s it?"

    cl "Yep, what’s even more special about that is that legend says if you were chosen and ascended, it will bless you with a successful romance or the pair who are already dating will stay together forever. Kyaaaa!"

    "The clam jumps up and down on her chair like a schoolgirl who is squealing at a romantic ending in a novel."

    "(A blessing huh. I guess I could use one.)"

    m "How do you get “chosen” by this “Hook”?"

    cl "You see, that’s what the mystery is. No one really knows. Some say it’s random, some say it chooses the most opposite pair, the colorful pair, it’s different every year."

    m "What about the fishiest smell pair?"

    cl "Hahaha, that’s a funny joke. You can’t smell here."

    "(Huh, that’s kind of a relief to know.)"

    cl "Anyways, don’t forget to meet your blind dates. I’ll let you know when and where."

    m "Alright, do you already have a date by the way?"

    cl "Hehehe, I do in fact! It’s a surprise for now."

    hide clamantha
    scene schoolyard


    "And so begins a new life in a fish body. "

    "I learnt that this is a boarding school and I have my own room! Sweet! "

    "The fish school isn’t so difficult since I used to learn about fishes while working with my family.
    They have similar school subjects here like on the surface though it’s mostly about the world of underwater and stuff. "

    "It wasn’t easy at first but I am getting used to this body and the diet as a fish."

    scene bg black

    "..."

# Scene 6 - Blind dates - begin

    scene schoolyard

    "It has been a week since I said yes to blind dates to Clamantha. "

    show Clamantha:
        yalign 0.5
        xalign 0.5

    cl "Allright, MC! Back to work we go, becoming the hook ruler is not going to be made by its own." 
    
    cl "I've set up 3 blind dates for you to try!"

    "And my first meet up will be in class 1A. "

    hide Clamantha
#-----------Blind date - Jawshua
    scene bg classroom

    "I entered this empty classroom that Clam noted for me."

    "(Oh, someone is here already. They are sitting at the other side where the window is.)"

    "As I come closer, their figure is getting bigger each time I notice."

    "(Wait, this is not just a big fish.)"

    show Jawshua:
        yalign 0.45
        


    bd "Yo."

    "(IT’S A SHARK???)"

    show Jawshua:
        yalign 0.45
        xalign 0.5

    m "H-Hi-hi, you must be m-m-my b-blind d-date?"

    "(I didn’t know there are sharks that can live in freshwater.)"

    bd "Yeah, you must mine too."
    bd "Oh, don’t mind my outfit. I had to come here straight after practice."

    bd "Can’t keep my date waiting of course."

    m "That’s v-very t-thoughtful of you."
    "The shark pulls down his shade a bit with eyes of concern."

    bd "Yeah, the name’s Jawshua. You feeling alright by the way? You cold?"

    m "N-No! I’m…just nervous for this meeting! Hahaha."

    "(Nervous to be eaten! Why did Clamantha get me a shark? I’m going to have a conversation with her after this.)"

    m "Anyway Jawshua, n-nice to meet you. Shall we continue?"

    "We both give a short introduction of ourselves like which class we are from and what are our interests."

    "Jawshua is in his final year and he’s on the school’s basketball team. He got recruited by someone in the league and will leave for them after the prom. "

    j "Just gonna cut to the chase. You look like you wanna find love without spending too much time and I think I’m perfect for you.
    I expect that if we go together to The Hook, we will get married after we finish highschool, move to the ocean and after that have 5 kids. "
    
    j "You agree?"

    m "....."

    "(My mind went blank after what I just heard out of his jaw...)"

    m "Um...I don’t think I can’t live in the ocean."

    "(An ocean is hella scary for me to go. I’ll definitely die! And besides…)"

    m "We just only met, could we take it slow perhaps?"

    j " Slow? Nah, I have my life planned already and I gotta keep on moving. Sorry buddy, I’m afraid this is where we stop."

    m "Oh, is that so?"

    "(Whew, I’m glad it’s over!)"

    hide Jawshua

    "Jawshua gets up and grabs his basketball which I still don’t know why brought it along."

    "We say goodbye to each other and I’m left alone in the classroom."

    "(Hmmm...now what. I’m free at the moment. What do people do after a blind date doesn’t work out?)"

    # play music kole fadein 2.0 fadeout 2.0

    show Kole at right
    show Whitefish1:
        xzoom -1
        xalign 0.7
        yalign 0.5

    "I turned to look out the hallway window and saw two fish swimming by, one of them is the familiar goldfish again with the same whitefish that was with him last week."
    hide Kole
    hide Whitefish1
    "I quickly look away fearing making eye contact with them."


    play music main

    "(Aaahhhh, what do I do? Is he going to beat up that whitefish again?)"

# Choices
#   [+1 Isaac]  Stay in and avoid making eye contact longer. --> go Love Interest Isaac - scene 1
#   [+1 Kole]    Help the whitefish.                         --> go to Love Interest Kole - scene 1

    menu:
        "Stay in and avoid making eye contact longer":
            jump isaac_1

        "Help the whitefish":
            jump kole_1


    label isaac_1:
        "(Nuh-uh! Not getting there again!)"

        "That fish seems like a really bad guy."

        "When I turn around a sudden funny face scares me."

        play music isaac fadein 1.0

        show isaac:
            zoom 1.5

        who "HEY!"

        "(THAT SCARED THE SHIT OUT OF ME!)"

        "I look at him in shock."

        "(What is this guy doing? His amphibian face is very close to mine.)"

        who "UM I- I CouLdN'T REallY aPoloGi–"

        m "Wait up. Collect yourself together, figure out what you want to say and say it."

        who "Allright, sorry."

        "The guy takes a step backwards, a deep breath and makes an actual sentence."

        who " Sorry, I can't recall introducing myself. The name's Isaac Newt-On, I am not really a resident of this lake, I come from a far more mysterious land. The SUR-FACE!"

        "Isaac spread his arms up open to bedazzle the word 'SUR-FACE'."

        "(???)"

        "(Does he think he's cool because of that?)"

        m "So what?"

        "The guy looks completely devastated."

        i "HOW DOESN'T IT SHOCK YOU?"

        m "I mean, why would it? I also come from the sur– (wait…)"

        i "You also what?"

        "I feel interrogated right now."

        "(Dammit why did I mention it??)"

        i "Do you have any information about it?"

        "Errr, I have no idea what you are talking about!"

        i "Are you playing dumb right now?"

        "Wait, maybe this guy can help me get out!"

        "Yeah...If I told you a secret, would you NOT tell everyone else?"

        "Do you even think anybody would believe me? In their eyes I am just a Surface-Nerd."

        "{i}sighs*{/i} Fine, I'll tell you. I am… actually a human, I live on the surface. I don't know how, nor why I woke up into this weird world. The only thing I remember was being rejected by my crush at the local lake and flying away."

        "Um, I know how sounding crazy feels like, and most of the time I am the one who's doing it. Buuuut… As a Surface-Nerd I am finding it quite hard to believe you."

        "Okay nevermind, I knew it was gonna be useless."

        "I was getting up and getting closer to the door, when Isaac talked."

        "Let's say I believe you."

        "Tell me something only a human would know."

        "I pause for a moment and declare my answer."

        menu:
            "This is useless, I am just talking to a fever dream Axolotl.":
                $ isaacPoints = isaacPoints - 1
                jump isaac_1_fever

            "This guy wants a human only secret? Fair enough.":
                $ isaacPoints = isaacPoints + 1
                jump isaac_1_secret

        # -----------choice 1/2 —<isaacpoint -1> (This is useless, I am just talking to a fever dream Axolotl.)
        label isaac_1_fever:

            m "Oh I don’t know, pfft, we invented cars?"

            i "C-carS? What is that?"

            m "Oh, we made them so it can transport us from one location to another!"

            i "Sooo, it is like how Remoras suck on sharks to go places?"

            m "YEs, but without the sucking… and the sharks."

            "The axolotl squints its eye in deep thought."

            i "Interesting concept…how would you withstand the water resistance and its friction? Wouldn’t you need to hold on to something?"

            m"Wellllll kind of no, you’ll be sitting and driving the vehicle if you’re the driver. Sometimes you can sit in other people’s car too."

            i "Fascinating... Ahem, I have concluded that I will believe you for now based on the concept of 'cars' is foreign to me."

            m "Greaaaaat."

            "I look at the hallway window and the goldfish isn’t there anymore."

            "(Here’s my chance!)"

            m "Hey, so it was a fun talk. I have to go now. Bye!"

            i "Wai– and they are gone."

            jump end_choice_1

        #------------choice 2/2 <isaacpoint +1> (This guy wants a human only secret? Fair enough. )
        label isaac_1_secret:

            "(Let’s see… he’s an axolotl. An aquatic salamander creature from the surface.)"

            m "Ok, I’m pretty sure you know humans breathe only air and they can’t live underwater."

            i "Duh, that’s why we don’t see them here always."

            m "Did you knooooow….."

            "(Oh no, I’m drawing blank here. Quick! Check my surroundings. Think of something!)"

            "And then I see his eyes and then windows. I noticed the reflection of my face."

            "(OH!)"

            m "Did you know humans have eyelids?"

            i "........"

            m "........"

            i " OH MY GOD, YOU ARE A HUMAN! I MEAN YOU WERE A HUMAN. Of course, no one here has seen a human before but you somehow know!"

            "I can see the axolotl’s starry eyes which made me think it’s very cute."

            m "Ha ha yeah, now you believe me?"

            "Isaac starts rambling on this profound secret."

            m "And did you know axolotl DO NOT have eyelids?"

            i "{i}Gasp{/i} I DIDN’T REALIZE MYSELF! Tell me, HUMAN! I must research you!"

            m "Well…"

            "(Oh, the goldfish already gone. This is my chance)"

            m "Maybe next time? I have to go somewhere. Bye!"

            i "Oh no, please wai– aaaand they’re gone."

            jump end_choice_1


# Love interest Kole - scene 1
    label kole_1:

        play music kole fadein 4.0

        "(Arrgghh, why are there no teachers around to deal with this.)"

        "I still feel bad that I left that little guy behind for my selfish escape."

        show Kole at right
        show Whitefish1:
            xzoom -1
            xalign 0.7
            yalign 0.5

        "(Oh, I got an idea. I’ll get in between them and make a big commotion so that somebody can come and Kole can’t take him further away.)"

        "(Ok, I’m gonna do it.)"

        "(With lots of anxiety and adrenaline running in me I got up and swam in between them."

        show Kole: 
            xalign 0.6

        show Whitefish1:
            xzoom -1
            xalign 0.2
            yalign 0.5

        "(Yes! They're further apart now!)"
        
        k "Hey, what are you doing?"

        m "UMM ! I HAVE A QUESTION TO YOU, KOLE."

        "(I hope I’m loud enough.)"

        k "Oh, and what is it? I can hear you just fine, you know."

        "I caught the whitefish student’s attention and signal them with my eyes to hurry and leave while they still can."

        "The whitefish guy looks confused."

        m "DO YOU HAVE A THING IN BEATING UP STUDENTS, KOLE?"

        "Kole’s eyebrows furrow."

        "(Uh oh, hurry, dude. Go!)"

        k "What exactly are you trying to do?"

        "Kole gets up really close to me."

        "(Ugh, is he still not leaving? I have no other choice.)"

        m "Y-YEAH, I SAW YOU WITH HIM THE OTHER WEEK. HE WAS UNCONSCIOUS ON THE GROUND COVERED IN --."

        k "HEY–"

        wf "WAIT, STOP!!"

        m "H-huh?"

        "The whitefish stood between us with fins stretched out."

        wf "Stop it! Kole didn’t do anything to me!"

        wf "He was just looking out for us smaller fish against the bigger fish bullies!"

        "(Oh no, I was wrong this whole time!?)"

        m "But then why did you look so nervous when you went to him? I bet he made you his lackey, didn’t he?"

        wf "No no, I went to him to thank him for standing up for me against those mean fish bullies."

        "(Now that I think about it, there was another slightly bigger fish unconscious in the scene when I arrived and Kole was next to that fish and not the whitefish.)"

        k "Like I said, I wasn’t there to help you. They were in my way and they just happened to annoy me, hmp!"

        "Kole crossed his arm fins and looked away with a pout on his face."

        m "Then why did you yell help?"

        wf "I did but I fainted afterwards. Kole had to take on three other big fishes which I think it’s going to go horribly. That’s why I yelled for help."

        wf "But who knew he was so strong!"

        "(I can see the twinkles in his eyes from admiration.)"

        k "I’m not that strong, they’re just weak for a big fish."

        m "..."

        k "What? If you got something then say it. I don’t like that stare."

        "(All this time it was all a misunderstanding…He was actually a pretty nice fish… Oh no! It finally hit me, I really want to crawl in a cave!)"

        "I got to say something but I’m too incredibly embarrassed after what I just yelled out loud."

        menu:
            "Apologize":
                $ kolePoints = kolePoints + 1
                jump kole_1_sorry

            "Stay awkwardly silent":
                $ kolePoints = kolePoints - 1
                jump kole_1_silent

    #------------choice 1/2 <Kolepoint +1> I apologize.
        label kole_1_sorry:
            hide Whitefish1

            show Kole:
                xalign 0.4
            
            m "...- -rry."

            k"Hm? What did you just say?"

            m "I’M SO SORRY! I-."

            k "Whoa, you don’t have to scream again."

            m "I’m so sorry, to you two. Kole, I was being rude to you the most. There are no excuses for what I have done."

            wf "Yeah, I appreciate how you were trying to protect me but I’m more glad it’s been cleared up."

            m "Yeah, and Kole… not gonna lie, you are very cool for standing up against those bullies even though I wasn’t there to witness it."

            k "W-wha- it was nothing."

            show Kole:
                xalign 0.6
                yalign 0.5

            "(Oh, he looked away again...Is that a blush I see?)"

            show Whitefish1:
                xzoom -1
                xalign 0.4
                yalign 0.5

            k "If that’s all, then let’s go, you said you will get me a drink as a thank you."

            wf "Oh, uh yes! Bye, now."

            hide Kole
            hide Whitefish1

            "And so the two fish left to the direction of the cafeteria to get drinks and I went ahead to see Clam to talk about how Jawshua is not it."

            jump end_choice_1

    #------------choice 2/2 <Kolepoint -1> Stay awkwardly silent
        label kole_1_silent:

            m "(Erm...Well, this is awkward…)"

            k "Yeah, if that’s all then we’re gonna go."

            m "Um, I-"

            "(Oh, they already left… I feel like I missed my chance to say something there.)"

            "I then went to see Clam to talk about how my bind date went and what an interesting choice she picked for me."

            jump end_choice_1
        #-----------------------------------end

label end_choice_1:
#---------Blind date - Blob
    play music main fadeout 1.0
    scene bg black
    "A few days later."

    "It has been probably 4-5 days since my first blind date and Clam said she found a rare pearl for me."

    "He's indeed a 'rare pearl'..."

    scene bg cafetaria
    "I’m sitting in front of my second date in the cafeteria."

    "I think my date is called… Blobby?"

    show Blobby:
        xalign 0.5
        yalign 0.5


    m "..."
    "I seriously need a word with Clam."
    m "...So what do you like to do for a hobby?"

    b "Blobbliolblobloblblubloblibloblblob"

    m "Okay… that sounds fun."

    b "Blobloblob."
    m "Okay so… How did you get to know Clamantha?"

    b "Blobbloblboblobbliol lblobloboblbol blobbliblobbylbolblobloblobloblobly blolbublboltob botokbitkbloy."

    "(I did not catch any of that)"

    m "Cool!"

    b "Blobloblobolbo?"

    m "{i}sighs{/i} I am sorry but I cannot understand a single word that is coming out of your mouth. Seriously, why did Clamantha set up a date between us?"

    b "Blob blob..."

    m "(I’m reaching my limit here.)"

    "We continue our date till I finish my portion of the food and drink fast."

    m "Hey…Blobby, it has been a nice lunch with you but I’m afraid I don’t see the future of us because of … our language barrier."

    b "Blob?"

    m "Yeah, I’m sorry. I…I remembered I have errands to do."

    b "Bloblob…"

    m "Thank you for being so understanding. I’ll be going now. Bye!"

    "I exited the the classroom feeling exhausted aftertrying really hard to understand at least his non-verbal language."

    "Can everyone else hear what he says? Am I the only one who can’t hear him?"

    "Well I’m free now. Where should I go to be alone for a bit to regain my energy?"
#Choose where to go next
#   [School yard] → Kole’s scene 2

#   [Classroom] → Isaac’s scene 2

    menu:
        "Choose where to go next"

        "School yard":
            jump kole_2

        "Classroom":
            jump isaac_2


# Love Interest Isaac - scene 2
    label isaac_2:

        scene bg classroom

        "I decide to go to my classroom, on my way there I find a familiar face."

        play music isaac fadein 2.0
        show isaac

        m "Oh! It's you."

        i "It’s not 'you'. The name’s Isaac Newt-on. "

        m "It's quite weird to refer to yourself by your full name y'know?"

        i "Sorry. I just love to have a full name. I don’t think I know your name either."

        "(This guy doesn't look like it, but he is quite narcissistic about himself.)"

        "I told him my name."

        m "So, Isaac The Almighty Newt-On, why don't you take me to see the USO that crushed me and almost caused such a pretty fish like me to die?"

        i "Err…"

        "Isaac pushes up his glasses."

        menu:
            "Are you showing me what you did or not?":
                $ isaacPoints = isaacPoints + 1
                jump isaac_2_show

            "Nevermind, shouldn't have asked a weirdo":
                $ isaacPoints = isaacPoints - 1
                jump isaac_2_weirdo

    #—---------choice 1/2 <isaac point +1> Are you showing me what you did or not?
        label isaac_2_show:

            i "I’m afraid it’s no longer here anymore."

            m "What do you mean?"

            i "It disappeared! It was here for a few days and then a mysterious hook took it away!"

            i"What a phenomenon I say. It was a legendary event to see it unfold! I have never seen such a massive hook before in my life. Not even on the Surface!"

            "Again with the sparkly eyes."

            "(Hook, huh? It must have been some locals up there who took care of the truck afterwards.)"

            "..."

            "(I hope it wasn’t too traumatizing for that girl when it happens, I hope things are ok up there.)"

            i "What’s wrong? You look sad. *gasp* Do you know something about that hook?"

            m "Well it’s a bit of a long story…"

            "I told Isaac what that hook was for and that USO was another type of human-made vehicle that hit me."

            i "...My, I’m glad the USO isn’t abandoned. It gets to return to the surface…"

            "Somehow that lowers Isaac’s mood."

            m "Yeah…"

            m "Hey, how did you become so obsessed with the humans and the Surface?"

            i "Oh!"

            "He’s back all smiling again."

            i "You see, I was born from the Surface! I don’t exactly remember about my family members of my kind but I did have a human child who took care of me."

            i "She was a very nice kid, who would always come and play with me behind an invisible wall. But one day, the human child decided to free me into this place. I didn’t need to be free, I was quite content there. Ever since then, I’ve been obsessed with trying to go back but nothing yet.  Hahaha."

            "(...)"

            i "Oh no, I’m making you sad, you’re crying."

            "Isaac wipes my tears away."

            i "There There, no need to be sad for me. I am completely capable of returning home."

            m "I-I’m not crying. *sniff* That kid is dumb for putting you in here. You’re so great and nice. *sniff*"

            "Isaac's cheeks grows rosy red with a smile after the nice compliment I gave him."

            "And we talk further more about the surface world, my life, his life and the humans who took care of him are like."

            "We became closer and I ended up joining his Surface research. "

            "Before I realized it’s already prom day."

            jump end_choice_2

    #--------choice 2/2 <isaac point -1> Nevermind, shouldn't have asked a weirdo.

        label isaac_2_weirdo:

            i "nono wait!"

            "I ignored the pink nerd and continued my way to the classroom, halfway through he stopped following me."

            "I sat at my desk, the last one next to the window and grabbed a nearby book."

            "Before I realized it’s already prom day."

            jump end_choice_2
#



# Love interest Kole - scene 2
    label kole_2:

        scene schoolyard

        "I chose to come to the schoolyard for fresh air… or fresher water in this case."

        "(Ahh, peace and quiet.)"

        "(It’s now 2 blind dates and I’m already losing hope that I will actually find someone…)"

        "My mind wandered around until I noticed Kole in the distance walking around the corner of the building."

        play music kole fadein 2.0

        show Kole

        "It looks like he’s carrying something small in his fins."

        "(What's he up to?)"

        "I followed him to the back of the building."

        "(What is he doing with that snail there?)"

        k "Here, eat up."

        "(He’s… feeding the snail.)"

        "(...Somehow that gesture of him feeding the snail is…making my heart feel fuzzy.)"

        "‘Krrzz krzz’"

        "(Ah! My dorsal fin brushed some of the pebbles below me and it made a little crunch noises.)"

        k "Who’s there?"

        "..."

        k "I can see your fin, you know."

        "(Dang it)"

        "I came out and waved a bit."

        m "Heyyy."

        k "Oh, it’s you again. Are you going to bother me again? Like you just followed me here?"

        m "N-no, I wouldn’t dare to. It just happens to be like that."

        k "Ah I see, so what do you want from me this time?"

        "(I can hear from his sarcasm that he doesn’t believe me.)"

        m "Ah no, I was just at the schoolyard over there until I noticed you went over here."

        m "I remembered that I never got to apologize for bumping into you when we met for the first time…I’m sorry."

        k "O-oh, is that so. I don’t even remember."

        "Kole is looking away with eyebrows furrowing a little bit while petting the snail. "

        "(Oh, as I got closer I noticed a bandage on the snail’s shell.)"

        "I swim closer towards them."

        m "Oh no, did that snail get injured? Is it ok?"

        play music main fadein 2.5

        "I got closer to have a closer look at the snail with its bandage."

        k "...too close.."

        m "Hm?"

        show Kole:
            zoom 2.0
            xalign 0.4
            yalign 0.15


        "I looked up and didn’t notice until now that my face is really close next to his face when we’re looking at the snail together."
        
        "Actually, up this close he’s actually a very pretty goldfish.
        His golden orange scales are so healthy and shiny looking."

        k" Your face is too close…"

        "Kole looks a bit uncomfortable."

        m "Ah! My bad!"

        show Kole:
            zoom 1.0
            xalign 0.4
            yalign 0.5

        "We both look away in the opposite directions."

        "‘Babump babump babump’"

        "(Badum? Is my heart seriously beating over a goldfish?? My face feels a bit warm. N-no, we were just in each other’s personal space that made us uncomfortable, that’s all…Yeah.)"

        "I take a peek at Kole’s face carefully. "

        "He has his fin curled in that covers a bit of his face."

        "(Is he feeling shy as well? …That’s kind of cute.)"

        "I somehow have the urge to say something to tease him. Should I?"

        menu:
            "Complement Kole’s scales":
                $ kolePoints = kolePoints - 1
                jump kole_2_compliment

            "Avoid and talk about the snail":
                $ kolePoints = kolePoints + 1
                jump kole_2_snail

    #----------choice 1/2 <kolepoint -1> Complement Kole’s scales
    label kole_2_compliment:

            m "Y-your scales are so very shiny looking, Kole."

            k "Huh? Oh, uh, thanks."

            m "How do you get them healthy and shiny?"

            "Kole said he didn’t do much for his scales. We then talked about what our diet is like and if Kole comes here often for the snail."

            "Turns out he found the snail’s shell was damaged but since then it has been healing well."

            "Since this encounter we have become closer as friends and visited behind the building to check on the snail together everyday."

            "And then before I realized it, it’s already Prom day."

            jump end_choice_2

    #----------choice 2/2 <kolepoint +1> Avoid and talk about the snail
    label kole_2_snail:

            m "Ahem, have you been taking care of this snail for a while? Is that allowed in school?"

            k "Not really, I found this snail about 2-3 weeks ago near the school’s garbage disposal area with its shell damaged."

            k "Luckily it wasn’t that bad, it might have been a strong current that made it fall and broke a bit of its shell. But the school doesn’t check in the back that often and it’s healing quite well."

            k "Heh, you should have seen how it’s trying to get away from the bandage but it’s still slow."

            "Kole has a big smile recounting the story of how he first met the snail."

            "I couldn’t help but smile too because of his infectious smile. "

            "‘Babump babump’"

            m "You…have a cute smi–"

            "I stopped myself from saying something so embarrassing."

            k "!?"

            "Kole looked at me with eyes open from what I was about to say."

            m "I-I mean snail! You have a cute snail! Becauuuuuse you’re so gentle to it and it looks like it likes you a lot!"

            "(Waahh, what a lame excuse!! Someone give me a shell to go inside to!)"

            k "..."

            k "Pfft"

            "(Hm?)"

            "(He laughed.)"

            "I’m in awe and I couldn’t help but laugh at the silly situation too."

            "Since this encounter we have gotten to know each other more and we would come behind the building to check on the snail together everyday. "

        

            jump end_choice_2



# Scene 7 - Prom

label end_choice_2:
    play music main fadein 1.0 fadeout 2.0

    scene bg hallway
    "Before I realized it’s already prom day."

    "I went on my third blind date before but it wasn’t that memorable and we didn’t click with each other. It was some generic fish."

    show Clamantha:
        xalign 0.5
        yalign 0.5

    "Clamantha was sad that her date canceled on her but then found a new one already."

    show Clamantha:
        xalign 0.2
        yalign 0.5
    show Blobby:
        xalign 0.8
        yalign 0.5

    "To my surprise it was Blobby! "

    "Turns out Blobby agreed to the blind date to make Clamantha happy and then confessed his love for her after our date." 
    
    "Clamantha is overjoyed and will happily go to the prom with him. "

    "I can sort of understand what Blobby is talking about thanks to Clamantha explaining to me that he just has a heavy accent from the deep water."
    cl "It will take some time to get used to."

    "That makes sense."
    "How did Blobby survive in the freshwater? I don’t know. Blob is still full of mystery like all the other deepsea creatures."

    "The three of us went together to keep me company and decided we should enjoy our last day of school before we set out in the world."

    cl "LET'S GOOOOO."

    play music prom fadein 2.0 fadeout 6.0

    scene bg prom
   
    "We entered a extremely big and well decorated place."

    "(Whoa, I never thought fish could party like this. In the stage there’s a band of fish and other crustaceans playing what you can find in a lake. Like mussel shells as drums, used fishing lines connected to bottle caps, and other creative combinations thrown by the humans used as instruments.)"

    "(It really makes you feel ashamed for being an irresponsible human in the past for a moment…)"

    "We danced and snacked while talking to other fishes around us."
    hide clamantha
    hide Blobby

    "(Hmm… I don’t see them. They’ve been kind of in my mind recently.)"

    stop music

    "And then the music stopped."

    show Host:
        xalign 0.5 
        yalign 0.5

    an "Hello, ladies and gentlefish! I hope everyone is having fun tonight!"

    "The crowd cheers."

    an "We are thrilled to have The Hook this year thanks to our organizers, a-claws to them!"

    cr "Whoo!"

    an "Now…the moment we have been waiting for! Ready for the drums."

    an "This year The Hook’s chosen… “Best Shell and Fish” are!"

    hide Host

    "‘Durururururuururururururururururu…’"

    an "Blobby and Clamantha! Congrats! Come on up!"

    show Clamantha:
        xalign 0.2
        yalign 0.5
    show Blobby:
        xalign 0.8
        yalign 0.5

    play music prom

    "Spotlights from flashlights light the two of them."

    "Clamantha starts to tear up and Blobby hugs her."

    m "Congrats you two! Now go up!"

    hide Blobby

    show Clamantha:
        xalign 0.5
        yalign 0.5

    cl "Oh, it would have been better if you were chosen instead of me."

    m "Oh, don’t. I’m happy for you. I don’t need anyone to make me happy. Now go, hurry. They’re calling for you."

    cl "Thank you."

    hide Clamantha

    "Up they go, they stand on the stage with everyone clapping their… fins and claws."

    show Host:
        xalign 0.09
        yalign 0.5

    an "Here you go, congrats on winning The Hook’s… coupon for dinner for two at The Boat!"

    "The announcer hands in paper to the couple."
    show Blobby:
        zoom 0.6
        xalign 0.99
        yalign 0.5    
    show Clamantha:
        zoom 0.6
        xalign 0.7
        yalign 0.5
    cl "Wait, what about the legend about blessing you a successful romance?"

    an "Ahhh, due to the USO accident, The Hook is in a hospital so this the best we can provide as a replacement. I’m sure you’ll have a wonderful time at The Boat!"

    cr "..."

    an "Anyways. Next, we will have some slow dancing~ Enjoy~!"

    #[music]

    "Everyone who is in pair starts to turn to each other and start slow dancing."

    "(Hmm… I still haven't seen them.)"

    "And then I go somewhere where there’s less crowd."

    hide Clamantha
    hide Blobby
    hide Host

    "..."

    if isaacPoints >= 2:
        jump isaac_ending
    elif kolePoints >= 2:
        jump kole_ending
    else:
        jump neutral_ending

    #Ending Isaac Route:
    label isaac_ending:
        scene bg prom

        "A familiar silhouette approaches you."

        m "Thought you wouldn't come."

        "I say while I turn around to see a shy amphibian next to me."

        show isaac

        i "Thought I might take a look at my fish culture."

        i "You know? Talking to you made me realize that I may have gotten too distracted with the surface that I forgot I actually need to live a little bit more here, on the water."

        m "Really? I thought I made you more curious about what's outside. Glad you are enjoying life here better."

        i "Mc? I-I would like to ask you something."

        m "Yeah, whatever you want Isaac."

        i "I-If yOU w-wEre to HMmm err-"

        m "Compose yourself."

        i "IF YOU WERE TO STAY HERE FOREVER,,, WOULD IT BE OKAY FOR US TO UM TO ERRRR"

        m "be friends? Sure thing!"

        i "yeah… Glad to hear that."

        hide isaac

        "We continue to watch Clamantha and Blobby be the center  of the party."

        "Suddenly, Isaac turns determined. "

        show isaac

        i "ACTUALLY! I was talking more.. romantic thing to it….."

        "(Oh…)"

        "(OH!)"

        "I smile at him, he is really blushing. He can look cute sometimes."

        m "Sure~"

        "I grin, his cheeks look like a tomato. "

        show CGisaac #---ending image of Isaac

        "Maybe I was a fool and there really are more fish in the sea, it really took me a whole trip to the bottom of the lake to realize that."

        jump end

    # Ending Kole Route:
    label kole_ending:
        scene bg prom
        "Kole is standing quite far away from the party where there isn't much fish around."
        
        "I went to him."
        
        m "Hey, what are you doing here?"

        show Kole

        k "Nothing really, just watching out that those bullies don't overstep my friend again."

        m "Oh, so you admit that you DID help that whitefish out at that time."

        k "...Shut up. I said they were just annoying."
        
        "Kole looks away to hide his smile."

        m "Aren't you going to go dancing?"
        
        k "It isn't really my thing."

        m "It isn't mine either, but we can give it a try. And make fun of eachother as we do."

        "Kole gave some thought while trying to hide his shyness behind his fin and then I noticed a little tap behind me."

        who "Excuse me, would you like to dance with me?"

        m "Oh um..."

        k "Sorry, this fish is already taken."

        show Kole:
            zoom 1.5
            xalign 0.5
            yalign 0.3


        "Kole grabs my fin and put his back in front of the other fish ."

        "The other fish left with disappointment to go ask another fish out."

        "Kole wraps lightly around under my fins and I put my arm fins on Kole's shoulders."

        "(Was he always this strong?). "

        "(How?)"

        k "Ouch. You sure are a horrible dancer, huh?"

        "(Uh Oh, I didn't think it was possible that I managed to step on his fin the pebbles underwater--hey!) "

        m "And you are a pretty good liar, you don't dance that bad."

        "Kole smirks."

        k "I said dancing was not my thing, not that I danced poorly."

        m "Yeah yeah, liar."

        "You leaned into Kole's chest and slowered your peace."

        show CGkole #Kole's ending image

        "Maybe I was a fool and there really are more fish in the sea. Well in the lake in this this case."
        "It really took me a whole trip to the bottom of the lake to realize that."

        jump end
    # Neutral Ending
    # (IsaacPoints == KolePoints OR both < 2 points)
    label neutral_ending:

        "Neutral end."

        jump end
    #   ~~~~~~~END~~~~~~

label end:

#----game ends
return
