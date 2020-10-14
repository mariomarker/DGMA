# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Brad")

define r = Character("Kay")

define t = Character("Wendy")

default beach = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene outside

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "Brad.png" to the images
    # directory.

    show Brad at left

    # These display lines of dialogue.

    menu:
        "You should really head to school...but"

        "Head to school":
            scene school
            show Brad at left
            show Kay at right
            e "Hey Kay!"
            show Kay happy
            r "Hey Brad!"
            e "So whats happening"
            r "Some girl is presenting something"
            scene classroom
            play music "Gym.ogg"

            show Wendy at left with easeinleft

            t "this is yaoi"

            show Wendy happy

            t "Yaoi is a blend of emotion and beauty involving two people whose love is looked down upon. The art tries to show all love is magical."

            show yaoiw behind Wendy

            t "in this piece by Cindy Chen it show tweek and Creg kissing eachother, Though there love may be looked down upon by some there love is stronger and cannot be broken"

            play sound "Awww.mp3"

            hide yaoiw with dissolve

            hide Wendy with dissolve

            scene school

            show Brad at left

            show Kay at right

            e "did you see that Kay!?"

            show Kay sad

            r "see what?"

            e "dude those girls drew picture of tweek and creg just for being gay! If we were gay we could get free pictures!"

            r "but I am ga-"

            e "Kay we should be gay so we can get free art!"

            show Kay

            r "W-wait you really mean it?"

            e "Yea dude then after we get those sweet drawings we can just break up"

            show Kay sad

            r "oh..."

            e "what do you say?"

            r "I guess I'm in..."

            show Brad mad

            e " HEY EVERYONE ME AND KAY ARE GAY!!!"

            r "ummm..."

            show Brad

            e  "Ok prefect I'll see you here tomorrow"

            hide Brad

            hide Kay

            show thenextday

            play sound "nextday.mp3"

            scene school
            show Brad at left
            show Wendy at right
            e "HEY WENDY!"
            show Wendy mad
            t "Yes?"
            e "Heard me and Kay are dating now?"
            t "Yes I heard..."
            e "And were both guys..."
            t "Yes I know..."
            e "So has anyone drawn artwork of me and Kay yet?"
            t "No why would they?"
            e "All the other girls drew art of tweek and creg"
            show Wendy lef
            t "Dude thats because tweek and creg are actually cute! You two are just boring self inserts in this shitty visual novel"
            hide Wendy
            show Brad mad
            e "God D#$!@ it!"
            show Kay at right
            r "What's wrong boyfriend?"

            e "no one is drawing artwork of us! Wendy says people think Tweek and Creg are cutier"

            r "Well I think you're cute"

            play sound "Awww.mp3"

            e "Well that doesn't solve anything now does it?! Lets just breakup this was a waste of time!"

            hide Brad

            show Kay sad

            r "Brad wait!"

            hide Kay

            scene bedroom

            show Brad

            r "I feel kinda bad for ditching Kay yesterday..."
            r "Maybe I should draw him something! Yea this whole thing started with us trying to get free artwork. I bet if I drew him something he'd forgive me"
            r "Maybe we could even keep dating..."

            menu:
                "Draw Kay something?"

                "Draw Yaoi":
                    scene school
                    show Brad at left
                    show Kay at right
                    e "Hey Kay! I wanted to appolgize for ditching you yesterday!"
                    r "oh um thats ok Brad I knew you were upset"
                    e "No it's not ok I was a bad boyfriend for ditching you."
                    r "boyfriend!? Wait does that mean we're still dating!?"
                    e "Heck yea! Now check out what I drew you!"
                    show yaoipaper1
                    play sound "Ha gay.mp3"
                    r "WOW SWEET!!! Great line work!"
                    e "Hehehe thank you!"
                    r "you're the best boyfriend a guy could have!"
                    "you got good Brad Ending!"
                    return
                "Just go to school":
                    scene school
                    show Brad at left
                    show Kay at right
                    e "Hey Kay! Sorry for ditching you yesterday!"
                    r "oh that's ok Brad I knew you were pretty disapointed that no one drew us. So I wanted to give you this."
                    e "Huh!? I present for me?"
                    show yaoipaper2
                    play sound "Ha gay.mp3"
                    e "AWWWWW That's so sweet! Thank you Kay!"
                    r "So are we still dating?..."
                    e "Heck yea! You're cool!"
                    r "sweet!"
                    "you got Good Michael Ending!"
                    return








            return

        "Ditch school":
            show cannda
            play music "cannda1.ogg"
            e "you were arested by canadian goverment for your crimes againts humanity"
            e "BAD ENDING"
            return

        "Fart":
            play sound "Fart.mp3"
            e "you Farted"
            jump home
    # this ends the game.

    e "you enjoyed yourself"

    menu:
        "what was your favourite thing you did?"

        "Swimming" if beach:
            e "you took a nice, long, swim."

        "walking":
            e "you had fun walking"

    label home:
        play sound "Fart.mp3"

        return






    play music "Gym.ogg"

    show Wendy at left with easeinleft

    t "this is yaoi"

    show Wendy happy

    t "Yaoi is a blend of emotion and beauty involving two people whose love is looked down upon. The art tries to show all love is magical."

    show yaoiw behind Wendy

    t "in this piece is about true love"

    hide yaoiw with dissolve

    hide Wendy with dissolve

    show Brad at left with easeinleft

    e "Hey Kay!"

    e "I drew you a photo want to see?"

    show Kay at right with easeinright

    r "You did!? Let me see!"

    show yaoi11

    r "lol you drew yaoi of us"

    e "I did! It's like the southpark episode"

    r "you're a dork"


    # This ends the game.

    return
