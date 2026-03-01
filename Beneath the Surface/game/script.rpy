# --- 1. DEFINITIONS ---
# Characters and their Sprites
define y = Character("You")
image charSprite = ""

define p = Character("Police")

# Backgrounds
image firstScene = "#333"
image murderScene = "#800"
image glare = "#111"
image court = "#446"
image jail = "#222"
image fail = "#000"

# Audio
define audio.scary = "audio_placeholder.mp3"

# --- 2. GAME START ---
label start: 

    scene bloodScene
    with fade

    play scary   #bullet sound or smt like that depending how they die

    scene firstScene #idk first scene
    with fade

    "It's been a truly long day, hasn't it?  From missing the bus twice to dealing with your obnoxious boss, you really didn't seem to be able to catch a break the entire day."

    "You climb up the stairs to your apartment. Once you reach your doorstep, you twist your home key, expecting to hear a click from your houselock. You groan in exhaustion as you realise you may have forgotten to lock your door this morning." 


    play scary   #light flickering sound

    "As you flick the broken houselights on, you remind yourself to make that appointment with an electrician when suddenly..."
    
    "You freeze"

    scene murderScene

    "You have never seen something so graphic in your life."

    "A dark shadowed figure under the dim light standing over a body lying on the floor, drenched in deep blood."

    scene glare

    "The figure tilts their head towards you slowly, their face covered with a mask, but even so you feel the intensity of their gaze send chills down your spine."

    "Frozen in place, your mouth hangs open in a silent scream. "

    "They turn around and jump out of your window in the blink of an eye, disappearing into the city lights."   #we can use that he is nimble as one of the clues

    "You crumble to the ground, your knees no longer able to support you and let out a sob. "

    you "Noooo.. no no no non no."

menu:
    "Chase the guy": 
        jump chase_the_guy

    "Call the police": 
        jump call_police

    "Call the police then chase the guy": 
        jump do_both

label chase_the_guy: 
    "You start running."

    "??? is still in sight"

    "You're running as fast as you can and you feel the lactic acid starting to burn in your throat."

    "??? drops the knife."

    "The mysterious individual is disarmed, now it's a matter of what happens next"

    scene standoff
    with fade

    you "Who are you…?"

    "??? throws a punch"

    "you dodge"

    "falls over while throwing their punch"

    you "That's it, I'm calling the police."

    "The police arrived and arrested him on the spot, you were able to avenge your boyfriend with minimal harm"

    "The End"

    scene complete
    with fade

    pause 3.0

menu:
    "Restart?": 
        jump start

    "Give up?": 
        return

label call_police:
    play scary
    "Weeeeee woooooooo"
    
    p "... and you found this body just, there?"

    you "Yes, officer. He... he was my boyfriend. I can't believe anyone would do that."

    p "Did you get into an argument before this happened? "

    you "... "

    "The officer gave you a look you couldn't interpret. Sympathy? Or suspicion?"

    you "BUT I'M INNOCENT, I SWEAR! I LOVED HIM, AND I STILL DO. you sobbed"

    p "I'm sorry, but you were the only witness, and you had a motive. I have to detain you. "

    scene jail
    with fade

    pause 3.0

    scene court
    with fade

    "Judge" "... and you are now sentenced to 10 years in prison. "

    play scary  #this doomed sound

    hide charSprite #mc
    scene fail 
    with fade

    return

label do_both:
    p "911 What's your emergency?"
    you "My boyfriend. He's.. he's dead. I found him on the ground with a knife through his head. I have tracked the killer after it jumped out the window, I'm on his tail right now. "
    p "Alright sir, first I will need your address. "
    you "I am at 212 Bank Drive"
    P  "Help is on there way, sir" 
    "You dash out the door and onto the street, eyes just barely on your target weaving skillfully through the onslaught of traffic. "
    "Hes still in your view just around the corner…"
    "??? Stabs you"
    you "you stabbed"
    "You get stabbed while chasing the killer, although you had bravery, you forgot he still had a weapon."

    play scary  #this doomed sound
    hide charSprite #mc
    scene fail
    with fade
