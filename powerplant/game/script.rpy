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


label init_game:
    python:
        File1 = item_location(0, 300,300, "file white.png")
        Folder1 = item_location(0, 200,120, "folder white.png")

        File2 = item_location(1, 300,100, "file t2.png")
        Folder2 = item_location(1, 200,350, "folder t2.png")

        l1_files = [File1, File2]
        l2_folders = [Folder1, Folder2]
    return


label day1:
    
    "Please organise these folders"
   # screen button_example
    default day1Complete = False

    while day1Complete == False:
        call screen level1(l1_files, l2_folders)
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

        

