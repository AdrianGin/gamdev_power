label day5_comp:
    call reset_level from _call_reset_level
    call day5Intro from _call_day5Intro
    show screen day5Comp_Instructions
    pause
    hide screen day5Comp_Instructions

    default day5Complete = False

    $ files = copy.deepcopy(const_l5_files)
    $ folders = copy.deepcopy(const_l5_folders)

    while day5Complete == False:
        call screen level1(files, folders)

        if _return == Incorrect:
            call InCorrect from _call_InCorrect_1
        
        if _return == Correct:
            call Correct from _call_Correct_1

        call doFailCheck from _call_doFailCheck
        if player_data.isMeltDown == True:
            jump doMeltdown
            return

        if AreFilesAllMoved(files) == 0:
            $ day3Complete = _return
            jump end5_normal

    jump end5_normal

label end5_normal:
    "I never knew what happened to my colleague... nevermind."
    "Just another day at the office I guess."
    return


label day5Intro:
    play music ["audio/Audio_M_01_State05_Loop.wav"] fadeout 4.0 fadein 4.0
    return   


label day5_help:
    
    call reset_level from _call_reset_level_1

    call day5Intro_help from _call_day5Intro_help

    show screen day5Helped_Instructions
    pause
    hide screen day5Helped_Instructions

    Edwy "Hi mate,
        When you will read this I'll already be far away.
        \nThe security unit are closing in on your position. Thanks for all.

        \nOh I nearly forgot.. run through this sequence and we'll both be free:
        \nFind and put Maps into Disk.
        \nPut Script into Plant Data to cause distraction.

        \nEdwy"

    default day5_helpComplete = False
    
    $ player_data.enemyTimerStarted = True

    $ files = copy.deepcopy(const_l5_files)
    $ folders = copy.deepcopy(const_l5_folders)

    while day5_helpComplete == False:
        call screen level1(files, folders)

        if _return == Incorrect:
            call InCorrect from _call_InCorrect_2
        
        if _return == Correct:
            call Correct from _call_Correct_2

        call doFailCheck from _call_doFailCheck_1
        if player_data.isMeltDown == True:
            jump doMeltdown
            return

        if player_data.isEnemyCaptured == True:
            jump youGotCaptured
            return

        if CountOptionalFiles(files) == 0:
            $ day3Complete = _return
            jump end5


    jump end5


label day5Intro_help:
    play music ["audio/Boss.wav"] fadeout 2.0 fadein 2.0
    return  

label end5:
    "The alarms seemed to have stopped. The place has gone into lockdown level 4."
    "As you drive home a convoy of police cars and army vehicles rush past"
    "We made it out!"
    return 