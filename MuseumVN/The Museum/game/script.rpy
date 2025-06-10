# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Matthew", color="#f4c473")
image Battler Smirking Hand = "Battler Smirking Hand.png"
image Battler Blinking Hand = "Battler Blinking Hand.png"
image Battler Frustrated 1 = "But_b11_aseru4.png"
image Battler Frustrated 2 = "But_b11_aseru5.png"
image Battler Serious = "But_b11_majime3.png"
image Battler Confused = "But_b22_komaru2.png"
image Battler Cry = "But_b22_naku2.png"
image Battler Laugh = "But_a21_warai1.png"

define w = Character("Museum Worker", color="#5a4313")
image Worker Neutral = "Kan_a11_def1.png"
image Worker Neutral 2 = "Kan_a11_def2.png"
image Worker Blinking = "Kan_a11_warai4.png"
image Worker Happy = "Kan_a11_warai3.png"

image Museum Dashboard = "museum-dashboard.png"

transform center_image:
    xalign 0.5
    yalign 0.5

image museum_entrance = At("images/bg/IMG_5957.png", center_image)
image museum_uketsuke = At("images/bg/IMG_5948.png", center_image)
image museum_stairs1 = At("images/bg/stairs.png", center_image)
image museum_stairs2 = At("images/bg/IMG_5953.png", center_image)
image museum_stairs3 = At("images/bg/IMG_5949.png", center_image)
image museum_lost1 = At("images/bg/IMG_5923.png", center_image)
image black_bg = At("images/bg/black_bg.jpg", center_image)

image museum_dino = At("images/bg/dinosaur.png", center_image)

image museum_squid = At("images/bg/IMG_5941.png", center_image)

transform double_size:
    zoom 2.0

transform zoom_out:
    zoom 0.2

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene museum_entrance:
        subpixel True
        yalign 1.0 
        linear 55  yalign 0.0
    play music "シューマン交響曲第一番的日常.mp3" volume 0.01

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    

    # These display lines of dialogue.
    "The spring winds come in, and the taste of summer is in the air."
    "This day is a perfect day to go and visit the museum."
    "For some reason you see..."
    "I cannot resist the museum."
    "Every day I dream about going there and seeing what they have to offer"
    show Battler Blinking Hand at double_size with moveinright
    voice "audio/Recording-cut.mp3"
    m "Ahhh What a nice day it is today!"
    hide Battler Blinking Hand
    "I had a look at my phone"
    show Battler Smirking Hand at double_size
    voice "audio/Recording (2)-cut.mp3"
    m "Woah it's already 12:00, the museum should be open by now."
    "The museum should just be around the corner."
    
    scene museum_uketsuke
    "I stepped inside of the museum and was greeted by an impressive entrance"
    show Battler Blinking Hand at double_size with dissolve
    voice "audio/Recording (3)-cut.mp3"
    m  "The entrance looks very grandiose! I wonder if there’s anyone inside at all today!"
    "Of course there is someone inside if the museum is open right...?"
    
    "The well-architected museum gave me a luxurious first impression"
    "Just imagining what kind of artefacts they have on display made me feel all excited"

    "I went further inside the museum"
    "Anyhow, I was greeted at the entrance by what appears to be a worker here"
    scene museum_uketsuke with fade

    voice "audio/Recording (4)-cut.mp3"
    w "Hello, and welcome to the Adelaide Museum, is there anything that I can be of assistance with today?"
    "I turned around to see who spoke"
    show Worker Neutral at left, double_size with dissolve
    show Battler Serious at right, double_size with dissolve
    voice "audio/Recording (5)-cut.mp3"
    w "Is there anything you need help with?"
    voice "audio/Recording (6)-cut.mp3"
    m "Not at the moment, I am super impressed with the interior of this museum however!"
    voice "audio/Recording (7)-cut.mp3"
    w "Ok, let me know if you require any assistance at all"
    hide Worker Neutral
    scene black_bg with fade
    "I decided to run full force into the museum, as I couldn't contain my excitement any longer"
    scene museum_stairs1 with fade
    show Battler Laugh at double_size
    "I wonder if my precious triceratops is in here?!?!?"
    scene museum_stairs2 with fade
    show Battler Frustrated 1 at double_size
    "However, I quickly realised that this attempt of navigating the museum was fragile"
    "I took a right"
    
    scene museum_stairs3 with fade
    show Battler Frustrated 2 at double_size
    "Then a left"
    show Battler Confused at double_size
    scene museum_lost1 with fade
    show Battler Cry at double_size
    "And before I knew it, I arrived at a place I have never seen before"
    "I thought this place is where the dinosaurs were..."
    "I had gotten lost"
    "I know that I am bad with directions, but somehow I am able to get lost inside of a museum."
    "It makes matters worse when you think that a museum is one of the best documented places"

    voice "audio/Recording (8)-cut.mp3"
    w "Hello, are you perchance lost at the moment?"
    show Battler Confused at right
    show Worker Neutral at left, double_size with dissolve
    "It was the same kind worker from before."
    "I was thinking to act like I am not lost for the sake of my pride"
    "But I decided that I couldn't keep up my bluff any longer"
    voice "audio/Recording (9)-cut.mp3"
    m "Embarrasingly so..."
    voice "audio/Recording (10)-cut.mp3"
    w "Has anyone shown you our brand new system which we have recently put at our museum?"
    
    "What are they talking about!? A brand new system"
    voice "audio/Recording (11)-cut.mp3"
    m "Not yet!"
    "I hope that this system is magical enough to fix my topographically agnostic problems which I suffer from"
    voice "audio/Recording (12)-cut.mp3"
    w "Well, give me your phone for a second"
    "I handed my phone like he requested."
    "Wait??? Isn't it bad to give your phone to someone you just met?"
    "Well, I might as well trust them as I do not have much other choices at the moment."
    voice "audio/Recording (13)-cut.mp3"
    w "Here, I installed our museum's new app on it, I also put our website in your web browser"
    "Woah this dude is cracked"
    "How did he unlock my phone and do all of that???"
    "I put the force majeure aside and decided to listen further"
    voice "audio/Recording (14)-cut.mp3"
    w "Using our app and website, I am sure that you'll be able to navigate our museum to the fullest."
    voice "audio/Recording (15)-cut.mp3"
    w "Our new system features a central database which any of the customers are free to access"
    voice "audio/Recording (16)-cut.mp3"
    w "If you have any aditional questions, you can always ask me"
    voice "audio/Recording (17)-cut.mp3"
    show Battler Smirking Hand
    m "Well, thank you for that, I'll be on my way then!"
    "I opened up at the app, and saw the one place I really wanted to see on there"
    "This app is able to accuractely map out the museum in front of me, showing me the exact directions to any exhibit"
    "I followed the directions until I finally arrived at the promised land."

    #End of the entrance scene!
    scene black_bg with fade
    "There's nothing quite like seeing the dinosaurs"
    "Seeing their massive dinosaur bones and experiencing the rich history behind it always make it so much more enjoyable"
    "Anyways, I need to actually get to the exhibition."
    "I followed the app, which led me to the correct spot"
    "In front of me.. everything was revealed"
    scene museum_dino:
        subpixel True
        yalign 1.0 
        linear 55  yalign 0.0

    voice "audio/Recording (18)-cut.mp3"
    m "Woah, this is the triceratops!"
    "I was astonished with how amazing this looked"
    "I looked at the precious triceratops, the very embodiment of time."
    "His tender gaze, the dinosaur that never stomped nor roared too loud."
    scene museum_dino:
        yalign 0.5
    voice "audio/Recording (19)-cut.mp3"
    m "I MISSED YOU!!!!"
    "I was about to jump out and hug the triceratops, but I decided to hold my urges back"
    "However, I noticed something odd. Now that I remember, I don't really know all too much about the triceratops"

    "I decided to open up the website on my laptop which I was carrying the whole time"
    "I found the triceratops page!"
    show Museum Dashboard:
        zoom 0.3
    "I was shocked, this page looks so amazing!"
    "It has so much details on here! Such as when the rampant beast was existent, and also other statistics such it’s top speed"
    "I didn't even know that it was able to achieve such a great speed!"
    "Also, this design is so modern! What an amazing job by the UI designers"
    "I shut the laptop in contempt"
    show Battler Smirking Hand at double_size, left
    voice "audio/Recording (20)-cut.mp3"
    m "Wow, what an amazing website!"
    "I shut the laptop in contempt"
    scene museum_dino:
        yalign 0.5
    "I feel like I truly learnt something new and incredible today about the history of dinosaurs."
    show Worker Happy at double_size, right
    voice "audio/Recording (21)-cut.mp3"
    w "How are you liking our new product so far?"
    show Battler Smirking Hand at double_size, left
    voice "audio/Recording (22)-cut.mp3"
    m "I am finding it utterly amazing, this has made my experience at this mueseum so much better"
    voice "audio/Recording (23)-cut.mp3"
    show Battler Serious with ease
    m "The ease of use of the system as well also makes it so much better for visitors like me!"
    voice "audio/Recording (24)-cut.mp3"
    show Battler Smirking Hand
    m "It really enchances the experience that you would traditionally get from a museum"
    show Worker Blinking at double_size
    voice "audio/Recording (25)-cut.mp3"
    w "Well, thank you for the kind words, I'll come back later and ask you how you feel after you've seen our other impressive displays"
    voice "audio/Recording (26)-cut.mp3"
    show Battler Blinking Hand
    m "Sounds good to me!"
    hide Worker Blinking
    "It seems like they left..."
    "Well, I would see another 'impressive display' if I knew exactly what the museum had to offer!?"
    "I just thought that museums was were dinosaurs lived, it appears that it's not only just for dinosaurs"
    "I opened up the app again, and I saw a truly impressive display using the in-built filtering system"
    "Without thinking, I gathered all of my belongings, and went straight to the Giant Squid!"


    #END OF DINO SCENE
    #START OF GIANT SQUID SCENE
    scene museum_stairs1 with fade
    "I started to head up the stairs to the exhibition just like the app said"
    scene museum_stairs2 with fade
    "After heading up a countless amount of stairs, I managed to navigate effectively to my next destination thanks to the app"
    scene museum_stairs3 with fade
    "It says to look down...."
    scene museum_squid:
        subpixel True
        yalign 1.0 
        linear 55  yalign 0.0
    play music "夜空は奏でるだろう.mp3" volume 0.15
    "I was taken aback by the sheer size of the giant squid"
    "The elegant fish, stuck in time yet still swimming around"
    "The massive tentacles, the small eyes, the huge head"
    "This display is unlike anything that I have seen before"
    "I have never seen such an amazing display in all my life visiting dinosaur exhibitions at museums."
    "I feel like a new neuron fired in my brain, unlocking a new passion for a new piece of history"
    voice "audio/Recording (27)-cut.mp3"
    m "This is way too cool!!"
    "I was inspired to learn more about this impressive display"
    "So, I open up the app that the kind worker installed onto my phone"
    "I easily navigated to the giant squid's page"
    voice "audio/Recording (28)-cut.mp3"
    m "Huh, apparently the Giant Squid is based off a specimen retrieved from New Zealand"
    voice "audio/Recording (29)-cut.mp3"
    m "If I had not read this, then I would assume that this is from South Australia!?"
    "My small world suddenly felt alot larger"
    "This app is truly amazing at giving me exactly all the details which I need to know"
    "Not to mention, the design and everything is so perfect!"
    "I also really like the quick feeds of information, such as how the Giant Squid was nearly 13 meters long!"
    voice "audio/Recording (30)-cut.mp3"
    m "That's like 6 me's stacked on-top of eachother!?"
    "Anyhow, I decided that I have spent enough time here, and decided to see some more parts of the museum"


    #Sightseeing part


    # This ends the game.
    scene black_bg with fade
    play music "透明な白い日常.mp3" volume 0.15
    "I decided to go back to the entrance of the museum"
    scene museum_entrance with fade
    voice "audio/Recording (31)-cut.mp3"
    w "Hello again, how was your visit at the museum today?"
    voice "audio/Recording (32)-cut.mp3"
    m "Well, I must say that it was utterly fantastic"
    voice "audio/Recording (33)-cut.mp3"
    m "All of your exhibits were amazing, and it opened up a new path to me that I have never even considered before"
    voice "audio/Recording (34)-cut.mp3"
    m "I used to only go to museums just for the triceratops and dinosaurs ever since I was 3"
    voice "audio/Recording (35)-cut.mp3"
    m "But I truly have to thank your new system for helping me discover a new passion in other fields."
    voice "audio/Recording (36)-cut.mp3"
    w "Why, thank you for the kind words, I'll be sure to let the development team know about how you felt"

    voice "audio/Recording (37)-cut.mp3"
    m "I have a question from my side, how is the new system for you?"
    voice "audio/Recording (38)-cut.mp3"
    w "Well, it is amazing, it accurately tracks all of the belongings for us, and where they are located in the museum"
    voice "audio/Recording (39)-cut.mp3"
    w "Working at a museum can be overwhelming, but this system helps us to manage the state of this museum so much better"
    voice "audio/Recording (40)-cut.mp3"
    w "It is also performant, I can't believe sometimes just how fast it is"
    voice "audio/Recording (41)-cut.mp3"
    w "It reminds me that we are in the 21st century"
    voice "audio/Recording (42)-cut.mp3"
    m "Wow, this system is truly incredible"
    voice "audio/Recording (43)-cut.mp3"
    w "One last thing! Our app features a way to view our images using AR, as we have vision capturing techniques here at the moment"
    voice "audio/Recording (44)-cut.mp3"
    w "That way, you can experience the museum anywhere!"
    voice "audio/Recording (45)-cut.mp3"
    m "OMG, I am going to try this out tonight then!"
    "I felt so impressed with the system at that point"
    "Are you telling me I can have this amazing experience anywhere?!"
    voice "audio/Recording (46)-cut.mp3"
    m "Well then, I am going to go home and give this a try!"
    voice "audio/Recording (47)-cut.mp3"
    w "Ok! Make sure to leave some feedback and come back again some time"


    scene black_bg with fade
    play music "ジムノペディ.mp3" volume 0.01
    "And so, I went home"
    "I opened up the app, and experienced the Giant Squid, magical Aborignal History, and also the Triceratops at home"
    "I have learnt so much today"
    "This system is truly incredible."
    return
