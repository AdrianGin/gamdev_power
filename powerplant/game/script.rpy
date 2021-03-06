# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Edwy = Character("EMPLOYEE 420205A")

image bg black = "#000000"
image bg white = "#FFFFFF"
image countdown = DynamicDisplayable(show_countdown)

# The game starts here.
label start:
    python:
        initGame()

  #  jump init_game
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
 
    # show bg black
    show screen change_mode
    show screen user_interface_health
    
    # This ends the game.
    jump day1
   # jump day2
  #  jump day3

    return

label reset_level:
    $ player_data.resetPower()
    return

label day1Intro:
    play music ["audio/Audio_M_01_State01_Loop.wav",
     "audio/Audio_M_01_State02_Loop.wav", "audio/Audio_M_01_State03_Loop.wav",
      "audio/Audio_M_01_State04_Loop.wav", "audio/Audio_M_01_State05_Loop.wav", "audio/Audio_M_01_State06_Loop.wav"] fadeout 4.0 fadein 4.0
    return





label day1:
    call reset_level from _call_reset_level_2
    call day1Intro from _call_day1Intro

    show screen day1Instructions
    pause
    hide screen day1Instructions

   # screen button_example
    default dayComplete = False

    $ files = copy.deepcopy(const_l1_files)
    $ folders = copy.deepcopy(const_l1_folders)

    while dayComplete == False:
        call screen level1(files, folders)

        if _return == Incorrect:
            call InCorrect from _call_InCorrect
        
        if _return == Correct:
            call Correct from _call_Correct

        call doFailCheck from _call_doFailCheck_2
        if player_data.isMeltDown == True:
            jump doMeltdown
            return

        if AreFilesAllMoved(files) == 0:
            $ dayComplete = _return
            jump day2
    
label end1:
    jump day2
    return

label day2:
    call reset_level from _call_reset_level_3
    call day2Intro from _call_day2Intro
    show screen day2Instructions
    pause
    hide screen day2Instructions

    Edwy "Hi mate,
        I don't know if you're using the new dark mode display, but I prefer to call it the new crap mode display.
        I can barely see any files or folders. I've to switch from dark to bright mode like a maniac if I want to do my daily tasks properly.
        It's like I'm in a nightclub.
        Sorry about the mess on the desktop.
        Cheers"

    default day2Complete = False

    $ files = copy.deepcopy(const_l2_files)
    $ folders = copy.deepcopy(const_l2_folders)

    while day2Complete == False:
        call screen level1(files, folders)

        if _return == Incorrect:
            call InCorrect from _call_InCorrect_3
        
        if _return == Correct:
            call Correct from _call_Correct_3

        call doFailCheck from _call_doFailCheck_3
        if player_data.isMeltDown == True:
            jump doMeltdown
            return

        if AreFilesAllMoved(files) == 0:
            $ day2Complete = _return
            jump day3

    return


label day2Intro:
    play music ["audio/Audio_M_01_State02_Loop.wav"] fadeout 4.0 fadein 4.0
    return   


label day3:
    call reset_level from _call_reset_level_4
    call day3Intro from _call_day3Intro
    show screen day3Instructions
    pause
    hide screen day3Instructions


    Edwy "Hi mate,
Aren't you tired of dragging and dropping?
I've discovered a path to make things more interesting for us.
What I need are the confidential files. Save them to disk and I'll collect it later
Cheers"

    default day3Complete = False

    $ files = copy.deepcopy(const_l3_files)
    $ folders = copy.deepcopy(const_l3_folders)

    while day3Complete == False:
        call screen level1(files, folders)

        if _return == Incorrect:
            call InCorrect from _call_InCorrect_4
        
        if _return == Correct:
            call Correct from _call_Correct_4

        call doFailCheck from _call_doFailCheck_4
        if player_data.isMeltDown == True:
            jump doMeltdown
            return
        
        if CountOptionalFiles(files) == 0:
            $ player_data.isHelp = True

        if AreFilesAllMoved(files) == 0:
            $ day3Complete = _return
            jump end3



    jump end3
    return

label end3:
    if player_data.isHelp == True:
        jump day5_help
    else:
        jump day5_comp
    return

label day3Intro:
    play music ["audio/Audio_M_01_State03_Loop.wav"] fadeout 4.0 fadein 4.0
    return   


label doFailCheck:
    scene end
    if player_data.meltdownLevel > 100:
        $ player_data.isMeltDown = True

    if player_data.enemyPosition <= 0:
        $ player_data.isEnemyCaptured = True

    return

label doMeltdown:   
    scene end
    show screen reactorBlow
    "You failed"
    return

label youGotCaptured:
    scene end
    show screen caputuredByEnemy   
    "You failed"
    return


screen user_interface_health():
    frame:
        xalign 0.96 yalign 0.96
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
                value StaticValue(player_data.availablePower, 600) 

            if player_data.enemyTimerStarted == True :
                null height 10
                label "Incoming Security Personnel"
                bar:
                    value StaticValue(player_data.enemyPosition, 100) 

            timer 2.0 action Function(PowerTimerCallback, player_data) repeat True
            timer 0.5 action Function(EnemyTimerCallback, player_data) repeat True

            timer 6.0 action Function(SoundCheckCallback, player_data) repeat True

screen change_mode():
    default BgCol = 1
    zorder 0
    frame:
        yfill True
        xfill True

        if player_data.isLightMode == True and player_data.availablePower > 0:
            background "#FFFFFF"
        else:
            background "#000000"

        button:
            background "#FFFFFF"
            xalign 0.95 yalign 0.7
            action [Function(SetLightMode)]
            if player_data.isLightMode == True:
                text _("Light Mode") style "button_text"
            else:
                text _("Dark Mode") style "button_text"



label InCorrect():
    play sound "audio/Audio_SFX_UI_Incorrect_01.wav"
    $ player_data.meltdownLevel = player_data.meltdownLevel + 5
    return

label Correct():
    play sound "audio/Audio_SFX_UI_Correct_01.wav"
    return