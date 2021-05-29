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
        initPlayer()

  #  jump init_game
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
 
    # show bg black
    show screen change_mode
    show screen user_interface_health
    #show screen light_mode
   # show eileen happy

    # These display lines of dialogue.

    e "Welcome to your first day at the power plant"

    e "To save power, we implemented light and dark mode."

    e "Now get to work!"

    # This ends the game.

    call day1

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
            call InCorrect
        
        if _return == Correct:
            call Correct
            "Correct!"

        if len(l1_files) == 0:
            $ day1Complete = _return
            jump end1
    
label end1:
    "Done!"
    return

screen user_interface_health():
    frame:
        xalign 0.0 yalign 0.0
        xsize 200
        background "#FFFFFF00"
        vbox:
            spacing 0
            label "Meltdown Risk"
            bar:
                value StaticValue(player_data.meltdownLevel, 100)
            null height 10
            label "Remaining Power"
            bar:
                value StaticValue(player_data.availablePower, 100)                
        

screen change_mode():
    default BgCol = 1
    zorder 0
    frame:
        yfill True
        xfill True

        if player_data.isLightMode == True:
            background "#FFFFFF"
        else:
            background "#000000"

        button:
            background "#FFFFFF"
            xalign 0.95 yalign 0.7
            action [Call("SetLightMode", BgCol)]
            if player_data.isLightMode == True:
                text _("Light Mode") style "button_text"
            else:
                text _("Dark Mode") style "button_text"

label SetLightMode(currentLightMode):
    play sound "audio/Audio_SFX_UI_Select_01.wav"
    $ player_data.isLightMode = not player_data.isLightMode
    return


label EnterLightMode():
    play sound "audio/Audio_SFX_UI_Select_01.wav"
    return

label InCorrect():
    play sound "audio/Audio_SFX_UI_Incorrect_01.wav"
    $ player_data.meltdownLevel = player_data.meltdownLevel + 5
    return

label Correct():
    play sound "audio/Audio_SFX_UI_Correct_01.wav"
    return