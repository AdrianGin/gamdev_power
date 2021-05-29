# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Employee 1")
image bg black = "#000000"
image bg white = "#FFFFFF"

# The game starts here.
label start:
    python:
        initLevels()

  #  jump init_game
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
 
    # show bg black
    show screen change_mode
    #show screen light_mode
   # show eileen happy

    # These display lines of dialogue.

    e "Welcome to your first day at the power plant"

    e "To save power, we implemented light and dark mode."

    e "Now get to work!"

    # This ends the game.

    jump day1

    return



label day1:
    
    "Please organise these folders"
   # screen button_example
    default day1Complete = False

    $ l1_files = const_l1_files
    $ l1_folders = const_l1_folders

    while day1Complete == False:
        call screen level1(l1_files, l1_folders)
        if _return == Incorrect:
            "BAD"
        
        if _return == Correct:
            "Correct!"

        if len(l1_files) == 0:
            $ day1Complete = _return
    
    "Done!"

screen change_mode():
    default BgCol = 1
    zorder 0
    frame:
        yfill True
        xfill True

        if BgCol == 1:
            background "#FFFFFF"
        else:
            background "#000000"

        button:
            background "#FFFFFF"
            xalign 0.95 yalign 0.7
            action [ToggleScreenVariable("BgCol", 1,0)]
            if BgCol == 0:
                text _("Light Mode") style "button_text"
            else:
                text _("Dark Mode") style "button_text"

        

