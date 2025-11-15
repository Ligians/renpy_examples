# Creating composites with Live Composite: https://www.renpy.org/doc/html/displayables.html#dynamic-displayables


image character normal = (Transform(Composite(
    (1177, 1739), #this is the size of the sprite
    (0, 0), "images/sprites/characterName/bases/normal.png",
    (0, 0), "blinking01", #these are the eyes (check the code for the blinking animation below)
    (0, 0), "images/sprites/characterName/eyebrows/001.png",
    (0, 0), "images/sprites/characterName/lips/001.png",
    ), zoom=0.5)) #You can use the zoom to adjust the size of the sprite on screen.

image character sad = (Transform(Composite(
    (1177, 1739),
    (0, 0), "images/sprites/characterName/bases/normal.png",
    (0, 0), "blinking02",
    (0, 0), "images/sprites/characterName/eyebrows/003.png",
    (0, 0), "images/sprites/characterName/lips/002.png",
    ), zoom=0.5))

image blinking01:
    "images/sprites/characterName/eyes/001.png" #This is the opened eye. You can have multiple stances of this code, one for each set of eyes you draw. Blinking widened eyes, blinking eyes looking to the right, blinking narrowed eyes, etc!
    choice: #the choice here served as a random timer. Sometimes, the char will blink after 8 seconds, sometimes after 4, and sometimes after 1. This makes it feel more natural.
        8
    choice:
        4
    choice:
        1
    "images/sprites/characterName/eyes/003.png" #this is the image of the eyes closed; it'll appear for .15 seconds, then the animation will go back to the beginning.
    .15
    repeat

image blinking02:
    "images/sprites/characterName/eyes/002.png"
    choice: 
        8
    choice:
        4
    choice:
        1
    "images/sprites/characterName/eyes/003.png" 
    .15
    repeat


# General good practices for creating sprites:

# This method is very useful cause it helps to keep the size of the game controlled while also giving you near limitless possible combinations to keep your expressions as..... expressive as possible xDD

# Still, I suggest creating a spreadsheet with all your expressions and what they look like. Believe you me, it'll make your work a lot easier on the long run! xD

# Good luck!