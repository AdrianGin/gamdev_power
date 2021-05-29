# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Employee 1")
image bg black = "#000000"
image bg white = "#FFFFFF"

default Mode = 0

# The game starts here.
label start:

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
 
    show bg black
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


label hello_world:
    scene bg club
    e "We at club"
    return


label day1:
    "Please organise these folders"
   # screen button_example
    call screen send_detective_screen

    "Okay, we'll send [detective] to [city]."

screen change_mode:
    frame:
        button:
            action Call("ChangeMode")
            if Mode == 0:
                text _("Light Mode") style "button_text"
            else:
                text _("Dark Mode") style "button_text"

screen dark_mode:
    modal False
    frame:
        modal False
        xfill True
        yfill True
        align (0.5, 0.5)
        background Solid("#000000")

        button:
            action Call("ChangeMode")
            text _("Mode Change") style "button_text"

label ChangeMode:
    if Mode == 0:
        show bg white
        $ Mode = 1
    else:
        show bg black
        $ Mode = 0
    return

screen light_mode:
    modal False
    frame:
        modal False
        xfill True
        yfill True
        align (0.5, 0.5)
        background Solid("#FFFFFF")        

        button:
            action ToggleScreen("light_mode")
            text _("Mode Change") style "button_text"

screen button_example():
    frame:
        xalign 0.5 ypos 50
        button:
            action ToggleScreen("light_mode")
            text _("Click me.") style "button_text"



        

screen send_detective_screen:

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "Ivy"
            child "sylvie green smile.png"
            droppable False
            dragged detective_dragged
            xpos 100 ypos 100
        drag:
            drag_name "Zack"
            child "File.png"
            droppable False
            dragged detective_dragged
            xpos 150 ypos 100

        # The cities they can go to.
        drag:
            drag_name "London"
            child "Folder1.png"
            draggable False
            xpos 450 ypos 140
        drag:
            drag_name "Paris"
            draggable False
            child "Folder1.png"
            xpos 500 ypos 280

