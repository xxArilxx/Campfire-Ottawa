# --- 1. DEFINITIONS ---
# Characters and their Sprites
define y = Character("You")
image charSprite = "#73ac60"
define p = Character("Police")

# Backgrounds
image entering = "entering.png"
image murderScene = "murderScene.png"
image glare = "glare.png"
image outside = "#947"
image court = "#446"
image jail = "#222"
image fail = "#000"

# Audio
define audio.door = "door_open.mp3"
define audio.lightBuzz = "light_buzzing.mp3"
define audio.keyTurn = "key.mp3"

#temp
define audio.scary = "door_open.mp3"

# --- 2. GAME START ---
label start: 
    scene entering
    with fade

    "It's been a truly long day, hasn't it?  From missing the bus twice to dealing with your obnoxious boss, you really didn't seem to be able to catch a break the entire day."
    "It seemed the only sign of a good day was when your grilled cheese was toasted perfectly and you found $5 on the street on your way to the bus stop."
    "Sighing, you climb up the stairs to your apartment. "
    
    play sound keyTurn

    "Once you reach your doorstep, you twist your home key, expecting to hear a click from your houselock. You groan in exhaustion as you realise you may have forgotten to lock your door this morning." 

    play sound door
    play music lightBuzz

    "As you flick the broken houselights on, you remind yourself to make that appointment with an electrician when suddenly..."
    "You freeze dead in your tracks."

    scene murderScene

    "You have never seen something so hauntingly graphic in your life."
    "A dark shadowed figure under the dim light standing over a body lying on the floor, blade impaled in their skull."
    "You feel your eyes water as tears stream your cheeks at the sight of the lifeless body of your boyfriend."

    scene glare

    "The figure tilts their head towards you slowly, their face covered with a mask, but even so you feel the intensity of their gaze send chills down your spine."
    "Frozen in place, your mouth hangs open in a silent scream. "
    "They turn around and jump out of your open window in the blink of an eye, disappearing into the city lights." 
    "Your knees weaken and you crumble to the ground, sobbing."
    y "Noooo... no no no no no..."

    menu:
        "Chase the murderer": 
            stop lightBuzz
            scene outside
            jump chase_the_guy

        "Call the police": 
            stop lightBuzz
            scene outside
            jump call_police

        "Call the police then chase the guy": 
            stop lightBuzz
            scene outside
            jump do_both

label chase_the_guy: 
    "You jump out the window and start running after the shadowy figure. Your vision was still blurry from the tears in your eyes."
    "You're running as fast as you can after them and you feel the lactic acid starting to burn in your throat."
    "Luckily for you, you happened to be on the track and field team since you were a child and quickly caught up to them. "
    "The mysterious individual notices you catching up to them and turns around sharply, and attempts to stab you in the gut but you quickly evade."
    "They swing their blade several times in your direction, cackling louder and as maniacally as a psych ward escapee. "
    "The figure suddenly drops their blade and quaking like a zombie, rendering them disarmed and vulnerable, leaving you an opening for attack. "
    "You tackle them to the ground destroying the mask on their face as the pieces of it detach from one another. "
    y "No... it can't be..."
    y "...Dad?"
    "Your sweet, innocent father; the light of your childhood, the hero that saved you from the abuse your mother constantly ensued on you."
    "Your father giggles and screams, a huge grin on his face as he kicked furiously in your grasp. He looked like a human possessed by a malevolent psychotic demon. "
    "You'd never seen this side of him before even though you'd been together your whole life. You can't help but imagine what he had to go through so you could live today."

    menu: 
        "Call the police on him": 
            jump police_on_dad

        "Talk to him": 
            jump talk

label police_on_dad: 
    "You pull out your phone and dial 911."
    y "I'd like to speak with the police. I'm at Lake Park and I've currently got a murderer in my hands."
    "Operator" "Got it. The nearest officers will arrive in a few minutes, hang tight."
    "The officers arrive faster than you expected and they carefully handcuff your father, still grinning unnaturally, as the police car drove away into the horizon."
    jump after_confront
            
label talk: 
    y "Dad... please... tell me why you did it..."
    y "Tell me why you killed him!"
    "He doesn't seem to hear you. If anything he seemed to react to the sound of your voice."
    "His eyes widen. His body stops moving and he stands in his place like a mannequin. "
    "Just when you think he had calmed down, he pulls out a small pistol from his pocket and shot himself in the head."
    y "NO!!"
    "Screaming, you start bawling. What a horrible day it was!"

    scene fail
    with fade
    jump after_confront

label after_confront: 
    "You head back to your apartment. You sigh for what seems like the millionth time and twist the door handle."
    "...were your eyes deceiving you... or did your boyfriend's body disappear...?"
    "You're terribly confused but decide to quickly wash up, go to sleep, and worry about it tomorrow."
    
    pause 3.0
    
    "█████" "Phew, how exhilarating! ██████████ ███████, did you enjoy my performance?"
    "██████████ ███████" "Yes, yes spectacular performance, █████! You've set a great model for the rest of our actors."
    "██████████ ███████" "Let the games... begin...!"

    scene complete
    with fade
    return

label no_confront: 
    "██████████ ███████" "█████ picked the wrong way to act if ██████████████ didn't chase after the murderer for revenge..."
    "██████████ ███████" "Dear audience... where are you all headed? Don't you want to see my creative vision for ██████████████? No! Stop! Come back!"
    "..."
    "██████████ ███████" "My child, my beautiful, imbecile of a child... it's time you learn the ways of this world. If ██████ hadn't interfered you would've been long ready."
    "██████████ ███████" "I'll reset everything again and again and again until you become ███ ████ ██ █████ and nothing will be able to stop me this time."

    menu:
        "Replay?": 
            jump start

        "End?": 
            return

label call_police:
    play sound scary
    
    p "... and you found this body just, there?"
    y "Yes, officer. He... he was my boyfriend. I can't believe anyone would do that."
    p "Did you get into an argument before this happened? "
    y "... "
    "The officer gave you a look you couldn't interpret. Sympathy? Or suspicion?"
    y "BUT I'M INNOCENT, I SWEAR! I LOVED HIM, AND I STILL DO!"
    p "I'm sorry, but you were the only witness, and you had a motive. I have to detain you. "

    scene jail
    with fade
    pause 3.0

    scene court
    with fade

    "Judge" "... and you are now sentenced to 10 years in prison. "

    play sound scary  #this doomed sound
    hide charSprite #mc

    hide charSprite #mc
    scene fail
    with fade

    jump no_confront

label do_both:
    p "911 What's your emergency?"
    y "My boyfriend. He's.. he's dead. I found him on the ground with a knife through his head. I have tracked the killer after it jumped out the window, I'm on his tail right now. "
    p "Alright, first I will need your address. "
    y "I am at 212 Bank Drive. Please hurry!"
    p  "Help is on there way." 
    "You dash out the window and onto the street, eyes just barely on your target weaving skillfully through the onslaught of traffic. "
    "He's still in your view just around the corner..."
    "Splat!"
    "You look down at your abdomen."
    "You get stabbed while chasing the killer, although you had bravery, you forgot he still had a weapon."

    hide charSprite #mc
    scene fail
    with fade

    jump no_confront