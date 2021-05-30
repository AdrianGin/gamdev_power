init python:
    import copy

    Incorrect = 0
    Correct = 1
    Completed = 2


    def detective_dragged(drags, drop):

        objectIndex = drags[0].drag_name.item_list.index(drags[0].drag_name.item)
        drags[0].drag_name.item_list[objectIndex].x = drags[0].x
        drags[0].drag_name.item_list[objectIndex].y = drags[0].y
        if not drop:
            return None

        if drags[0].drag_name.item.id != drop.drag_name.item.id:
            return Incorrect

        drags[0].drag_name.item_list.remove(drags[0].drag_name.item)
        return Correct

    class player:
        def __init__(self):
            self.meltdownLevel = 0
            self.isLightMode = False
            self.isEnemyCaptured = False

            self.enemyPosition = 200
            self.resetPower()

            self.day3helpsCompany = False
        
        def resetPower(self):
            self.availablePower = 100
            
    class drag_context:
        def __init__(self, item, item_list):
            self.item = item
            self.item_list = item_list

    class item_location:
        def __init__(self, id = 0, x = 0, y = 0, type = "", type2 = "", name = ""):
            self.id = id
            self.x = x
            self.y = y
            
            self.name = name

            self.img = type 
            self.type = type
            self.type2 = type
            if type2 == "":
                self.type2 = type


    class SoftTimer:
        def __init__(self, timeout, callback, context):
            self.timeout = timeout / 50
            self.counter = 0
            self.callback = callback
            self.context = context
            self.enabled = False

        def Service(self):
            self.counter = self.counter + 1
            if self.counter >= self.timeout:
                self.callback(self.context)
                self.counter = 0


init python:
    const_l1_files = []
    const_l1_folders = []
    const_l2_files = []
    const_l2_folders = []

    timers = []
    player_data = player()
    fileContext = drag_context(item_location(), item_location())

    def initGame():
        initLevels()
        initPlayer()
        initTimers()

    def initLevels():

        initLevel1()
        initLevel2()
        return

    def initLevel1():
        global const_l1_files
        global const_l1_folders
        const_l1_files.clear()
        const_l1_folders.clear()

        const_l1_folders.append( item_location(0, 51,62, Folder_Admin) )
        const_l1_folders.append( item_location(1, 155,62, Folder_PlantData) )

        const_l1_files.append( item_location(0, 239,234, File_DocumentM1D) )
        const_l1_files.append( item_location(0, 426,114, File_CalendarDL) )
        const_l1_files.append( item_location(0, 492,338, File_DocumentLL) )
        const_l1_files.append( item_location(0, 649,409, File_CalendarLL) )

        const_l1_files.append( item_location(1, 553,179, File_GraphM1L) )
        const_l1_files.append( item_location(1, 632,90, File_GraphLL) )
        const_l1_files.append( item_location(1, 729,134, File_GraphM1L) )
        const_l1_files.append( item_location(1, 680,242, File_GraphM1L) )

    def initLevel2():
        global const_l2_files
        global const_l2_folders
        const_l2_files.clear()
        const_l2_folders.clear()

        const_l2_folders.append( item_location(0, 51,62, Folder_Admin) )
        const_l2_folders.append( item_location(1, 155,62, Folder_PlantData) )
        const_l2_folders.append( item_location(2, 51,413, Folder_BinM) )

        const_l2_files.append( item_location(2, 287,144, File_StickynoteDD) )
        const_l2_files.append( item_location(1, 429,80, File_GraphLD) )
        const_l2_files.append( item_location(0, 552,55, File_CalendarLL) )
        const_l2_files.append( item_location(0, 576,144, File_DocumentLD) )
        const_l2_files.append( item_location(1, 678,164, File_GraphDL) )
        const_l2_files.append( item_location(2, 488,218, File_StickyNoteDD) )
        const_l2_files.append( item_location(1, 265,268, File_GraphDL) )
        const_l2_files.append( item_location(0, 530,354, File_ToDoL) )
        const_l2_files.append( item_location(0, 389,300, File_ToDoD) )
        const_l2_files.append( item_location(0, 119,289, File_CalendarLL) )
        const_l2_files.append( item_location(1, 233,413, File_GraphM2D) )
        const_l2_files.append( item_location(0, 453,419, File_DocumentDL) )
        const_l2_files.append( item_location(2, 623,433, File_StickyNoteM1D) )
        const_l2_files.append( item_location(1, 708,236, File_ToDoD) )
        const_l2_files.append( item_location(0, 689,330, File_DocumentLD) )

    def initPlayer():
        global player_data
        player_data = player()

    def initTimers():
        global timers
        global player_data
        #timers.append( SoftTimer(100, PowerTimerCallback, player_data) )


    def PowerTimerCallback(context):
        if context.isLightMode == True:
            context.availablePower = context.availablePower - 1
            if context.availablePower <= 0 :
                context.isLightMode = False
                renpy.play("audio/Audio_SFX_UI_Shutdown_01.wav")
        pass


    def EnemyTimerCallback(context):
        if context.enemyPosition != 100:
            context.enemyPosition = context.enemyPosition - 1
            #if context.enemyPosition <= 0 :
             #   context.isLightMode = False
                #renpy.play("audio/Audio_SFX_UI_Shutdown_01.wav")
        pass        

    def periodic_callback():
        for i, timer in enumerate(timers):
            timer.Service()


    def show_countdown(st, at):
        if st > 5.0:
            return Text("0.0", color="#f00"), 0.1
        else:
            d = Text("{:.1f}".format(5.0 - st), color="#f00")
            return d, 0.1

    def SetLightMode():
        player_data.isLightMode = not player_data.isLightMode
        renpy.play("audio/Audio_SFX_UI_Select_01.wav")