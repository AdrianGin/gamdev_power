

#image filel1 = DynamicDisplayable(show_countdown)

init -1 python:

    def Dyn_File_CalendarDL(st, at):
        if player_data.isLightMode == True:
            return Image("File-CalendarDL-Light.png"), 0.0
        else:
            return Image("File-CalendarDL-Dark.png"), 0.0


    def Dyn_File_CalendarLL(st, at):
        if player_data.isLightMode == True:
            return Image("File-CalendarLL-Light.png"), 0.0
        else:
            return Image("File-CalendarLL-Dark.png"), 0.0       

    def Dyn_File_CalendarM1L(st, at):
        if player_data.isLightMode == True:
            return Image("File-CalendarM1L-Light.png"), 0.0
        else:
            return Image("File-CalendarM1L-Dark.png"), 0.0                   


    File_CalendarDL = DynamicDisplayable(Dyn_File_CalendarDL)
    File_CalendarLL = DynamicDisplayable(Dyn_File_CalendarLL)
    File_CalendarM1L = DynamicDisplayable(Dyn_File_CalendarM1L)


    def Dyn_File_GraphDL(st, at):
        if player_data.isLightMode == True:
            return Image("File-GraphDL-Light.png"), 0.0
        else:
            return Image("File-GraphDL-Dark.png"), 0.0

    def Dyn_File_GraphLD(st, at):
        if player_data.isLightMode == True:
            return Image("File-GraphLD-Light.png"), 0.0
        else:
            return Image("File-GraphLD-Dark.png"), 0.0

    def Dyn_File_GraphLL(st, at):
        if player_data.isLightMode == True:
            return Image("File-GraphLL-Light.png"), 0.0
        else:
            return Image("File-GraphLL-Dark.png"), 0.0       

    def Dyn_File_GraphM1L(st, at):
        if player_data.isLightMode == True:
            return Image("File-GraphM1L-Light.png"), 0.0
        else:
            return Image("File-GraphM1L-Dark.png"), 0.0      


    def Dyn_File_GraphM2D(st, at):
        if player_data.isLightMode == True:
            return Image("File-GraphM2D-Light.png"), 0.0
        else:
            return Image("File-GraphM2D-Dark.png"), 0.0    

    File_GraphDL = DynamicDisplayable(Dyn_File_GraphDL)
    File_GraphLL = DynamicDisplayable(Dyn_File_GraphLL)
    File_GraphLD = DynamicDisplayable(Dyn_File_GraphLD)
    File_GraphM1L = DynamicDisplayable(Dyn_File_GraphM1L)
    File_GraphM2D = DynamicDisplayable(Dyn_File_GraphM2D)

    def Dyn_File_DocumentDL(st, at):
        if player_data.isLightMode == True:
            return Image("File-DocumentDL-Light.png"), 0.0
        else:
            return Image("File-DocumentDL-Dark.png"), 0.0


    def Dyn_File_DocumentLL(st, at):
        if player_data.isLightMode == True:
            return Image("File-DocumentLL-Light.png"), 0.0
        else:
            return Image("File-DocumentLL-Dark.png"), 0.0       

    def Dyn_File_DocumentM1D(st, at):
        if player_data.isLightMode == True:
            return Image("File-DocumentM1D-Light.png"), 0.0
        else:
            return Image("File-DocumentM1D-Dark.png"), 0.0      


    File_DocumentDL = DynamicDisplayable(Dyn_File_DocumentDL)
    File_DocumentLL = DynamicDisplayable(Dyn_File_DocumentLL)
    File_DocumentM1D = DynamicDisplayable(Dyn_File_DocumentM1D)
    File_DocumentLD = DynamicDisplayable(Dyn_File_DocumentDL)

    def Dyn_File_ToDoD(st, at):
        if player_data.isLightMode == True:
            return Image("File-ToDoD-Light.png"), 0.0
        else:
            return Image("File-ToDoD-Dark.png"), 0.0


    def Dyn_File_ToDoL(st, at):
        if player_data.isLightMode == True:
            return Image("File-ToDoL-Light.png"), 0.0
        else:
            return Image("File-ToDoL-Dark.png"), 0.0

    File_ToDoD = DynamicDisplayable(Dyn_File_ToDoD)
    File_ToDoL = DynamicDisplayable(Dyn_File_ToDoL)

    def Dyn_File_StickyNoteDD(st, at):
        if player_data.isLightMode == True:
            return Image("File-StickynoteDD-Light.png"), 0.0
        else:
            return Image("File-StickynoteDD-Dark.png"), 0.0


    def Dyn_File_StickyNoteM1D(st, at):
        if player_data.isLightMode == True:
            return Image("File-StickynoteM1D-Light.png"), 0.0
        else:
            return Image("File-StickynoteM1D-Dark.png"), 0.0                   


    File_StickyNoteDD = DynamicDisplayable(Dyn_File_StickyNoteDD)
    File_StickyNoteM1D = DynamicDisplayable(Dyn_File_StickyNoteM1D)


    def Dyn_File_TricksetPhoto(st, at):
        if player_data.isLightMode == True:
            return Image("File-TricksetPhoto-Light.png"), 0.0
        else:
            return Image("File-TricksetPhoto-Dark.png"), 0.0

    File_TricksetPhoto = DynamicDisplayable(Dyn_File_TricksetPhoto)

    def Dyn_File_TricksetGolf(st, at):
        if player_data.isLightMode == True:
            return Image("File-TricksetGolf-Light.png"), 0.0
        else:
            return Image("File-TricksetGolf-Dark.png"), 0.0

    File_TricksetGolf = DynamicDisplayable(Dyn_File_TricksetGolf)

    def Dyn_File_TricksetJeeves(st, at):
        if player_data.isLightMode == True:
            return Image("File-TricksetJeeves-Light.png"), 0.0
        else:
            return Image("File-TricksetJeeves-Dark.png"), 0.0

    File_TricksetJeeves = DynamicDisplayable(Dyn_File_TricksetJeeves)

    def Dyn_File_PlayCoinML(st, at):
        if player_data.isLightMode == True:
            return Image("File-PlayCoin-Light.png"), 0.0
        else:
            return Image("File-PlayCoin-Dark.png"), 0.0

    File_PlayCoinML = DynamicDisplayable(Dyn_File_PlayCoinML)

    def Dyn_File_Diagnostics(st, at):
        if player_data.isLightMode == True:
            return Image("File-Diagnostics-Light.png"), 0.0
        else:
            return Image("File-Diagnostics-Dark.png"), 0.0

    File_Diagnostics = DynamicDisplayable(Dyn_File_Diagnostics)

        def Dyn_File_SignalLogL(st, at):
        if player_data.isLightMode == True:
            return Image("File-SignalLogL-Light.png"), 0.0
        else:
            return Image("File-SignalLogL-Dark.png"), 0.0

    File_SignalLogL = DynamicDisplayable(Dyn_File_SignalLogL)

    def Dyn_Folder_Admin(st, at):
        if player_data.isLightMode == True:
            return Image("Folder-Admin.png"), 0.0
        else:
            return Image("Folder-Admin.png"), 0.0

    def Dyn_Folder_PlantData(st, at):
        if player_data.isLightMode == True:
            return Image("Folder-PlantData-Light.png"), 0.0
        else:
            return Image("Folder-PlantData-Dark.png"), 0.0

    def Dyn_Folder_BinM(st, at):
        if player_data.isLightMode == True:
            return Image("Folder-BinM.png"), 0.0
        else:
            return Image("Folder-BinM.png"), 0.0

    def Dyn_Folder_Disk(st, at):
        if player_data.isLightMode == True:
            return Image("Folder-Disk-Light.png"), 0.0
        else:
            return Image("Folder-Disk-Dark.png"), 0.0            

    Folder_PlantData = DynamicDisplayable(Dyn_Folder_PlantData)
    Folder_Admin = DynamicDisplayable(Dyn_Folder_Admin)
    Folder_BinM = DynamicDisplayable(Dyn_Folder_BinM)
    Folder_Disk = DynamicDisplayable(Dyn_Folder_Disk)

screen level1(files, folders):
    timer 0.1 action Function(PowerTimerCallback, player_data) repeat True

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        for i, file in enumerate(files):
            $ global fileContext
            $ fileContext = drag_context(file, files)

            drag:
                drag_handle (0, 0, 1.0, 1.0)
                drag_name fileContext
                child file.type
                droppable False
                dragged detective_dragged
                xpos file.x ypos file.y
                

        #Folders
        for i, folder in enumerate(folders):
            $ fileContext = drag_context(folder, folders)
            drag:
                drag_name fileContext
                child folder.type
                draggable True
                dragged detective_dragged
                xpos folder.x ypos folder.y

    
