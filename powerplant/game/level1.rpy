

#image filel1 = DynamicDisplayable(show_countdown)

init -1 python:
    def get_file(st, at, fileContext):
        if player_data.isLightMode == True:
            return Image("File-CalendarDL.png"), 0.1
        else:
            if fileContext.item.type == "":
                return filel1, 0.1
            return fileContext.item.type, 0.1

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



    File_CalendarDL = DynamicDisplayable(Dyn_File_CalendarDL)
    File_CalendarLL = DynamicDisplayable(Dyn_File_CalendarLL)
    File_CalendarM1L = DynamicDisplayable(Dyn_File_CalendarM1L)

    Folder_PlantData = DynamicDisplayable(Dyn_Folder_PlantData)
    Folder_Admin = DynamicDisplayable(Dyn_Folder_Admin)


screen level1(files, folders):
    timer 0.1 action Function(PowerTimerCallback, player_data) repeat True

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        for i, file in enumerate(files):
            $ global fileContext
            $ fileContext = drag_context(file, files)
            default type = file.type2
           # if player_data.isLightMode == True and file.type2 != "" :
           #     $ type = file.type2

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

    
