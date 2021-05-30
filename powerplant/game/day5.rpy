label day5_comp:
    call reset_level
    call day5Intro
    show screen day5Comp_Instructions
    pause
    hide screen day5Comp_Instructions

    default day5Complete = False

    $ files = copy.deepcopy(const_l2_files)
    $ folders = copy.deepcopy(const_l2_folders)

    while day5Complete == False:
        call screen level1(files, folders)

        if _return == Incorrect:
            call InCorrect
        
        if _return == Correct:
            call Correct

        if len(files) == 0:
            $ day3Complete = _return
            jump end1

    "I never knew what happened to my colleague... nevermind."
    "Just another day at the office I guess."

    jump end1


label day5Intro:
    play music ["audio/Audio_M_01_State05_Loop.wav"] fadeout 4.0 fadein 4.0
    return   


label day5_help:
    
    call reset_level

    call day5Intro_help

    show screen day5Helped_Instructions
    pause
    hide screen day5Helped_Instructions

    Edwy "Hi mate,
        When you will read this I'll already be far away.
        The security unit are closing in on your position.
        Thanks for all.

        Oh I nearly forgot.. run through this sequence and we'll both be free:
            Save the Map and Secrets.
            Place everything into the bin

        Edwy"

    default day5_helpComplete = False
    
    $ player_data.enemyTimerStarted = True

    $ files = copy.deepcopy(const_l2_files)
    $ folders = copy.deepcopy(const_l2_folders)

    while day5_helpComplete == False:
        call screen level1(files, folders)

        if _return == Incorrect:
            call InCorrect
        
        if _return == Correct:
            call Correct

        if len(files) == 0:
            $ day5_helpComplete = _return
            jump end1

    "The alarms seemed to have stopped. The place has gone into lockdown level 4."
    "As you drive home a convoy of police cars and army vehicles rush past"
    jump end1


label day5Intro_help:
    play music ["audio/Boss.wav"] fadeout 2.0 fadein 2.0
    return   