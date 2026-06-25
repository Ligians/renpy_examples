init python:

   # Step 1. Create the gallery object.

   g = Gallery()
   g.navigation = True
   g.transition = dissolve

   g.locked_button = (Transform("extra/CGs/locked.png", zoom=0.2)) #this is the thumbnail image for ALL LOCKED gallery previews, found in the images folder

   # Step 2. Add buttons and images to the gallery.

   # A button that contains an image that automatically unlocks.

   #g.condition("persistent.unlock_1") #this is the requirement/condition that must be met for this gallery image to unlock

   # g.image("backgroundImageName1", "foregroundImageName1") #this creates a gallery image that overlaps a foreground on top of a bg, you can also use a single flattened image here

   # For each gallery image, you need to define:
   #
   # unique name/label g.button("ABCDEFG")
   # condition(s) g.condition("persistent.unlock_ABCDEFG")
   # final gallery image(s) g.image("ABCDEFG", "HIJKLMNOP")

   #this changes the full screen image

   g.button("betatesterty")
   g.condition("persistent.unlock_beta1")
   g.image("extra/CGs/betatesterty.png")

   g.button("cg1") #this is the name/label associated with your button for a particular image, can be modified
   g.condition("persistent.unlock_cg1")
   g.image("extra/CGs/cg1.png")

   g.button("cg2")
   g.condition("persistent.unlock_cg2")
   g.image("extra/CGs/cg2.png")



#### This is the code to add the gallery in your screens:

    add g.make_button("betatesterty", (im.FactorScale((im.MatrixColor("extra/CGs/betatesterty.png", im.matrix.saturation(0))), 0.2)), hover_border="gui/gamemenu/gui/galleryshadow.png", xalign=0.5, yalign=0.5)
    add g.make_button("cg1", (im.FactorScale("extra/CGs/cg1.png", 0.2)), hover_border="gui/gamemenu/gui/galleryshadow.png", xalign=0.5, yalign=0.5)
    add g.make_button("cg2", (im.FactorScale("extra/CGs/cg2.png", 0.2)), hover_border="gui/gamemenu/gui/galleryshadow.png", xalign=0.5, yalign=0.5)