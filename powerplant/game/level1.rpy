

#image filel1 = DynamicDisplayable(show_countdown)

init -1 python:
    def get_file(st, at, fileContext):
        if player_data.isLightMode == True:
            return Image("File-CalendarDL.png"), 0.1
        else:
            if fileContext.item.type == "":
                return filel1, 0.1
            return fileContext.item.type, 0.1

    def get1_file(st, at):

        if player_data.isLightMode == True:
            return Image("File-CalendarDL.png"), 0.0
        else:
            return Image("Folder-Admin.png"), 0.0
            
        drag = Drag( Image("File-CalendarDL.png"), "test" )    
        drag2 = Drag( Image("Folder-Admin.png"), "test", True )   
        #return drag2, 0.1

        fixed = Fixed( DragGroup( drag, drag2, xfill = True, yfill = True), xfill = True, yfill = True )

        return drag, 0.2


    filel1 = Image("images/Folder-PlantData.png")
 #   filel_d = DynamicDisplayable(get_file, fileContext)

    level_d = ConditionSwitch("player_data.isLightMode == True", "File-CalendarDL.png",
                              "player_data.isLightMode == False", "Folder-Admin.png")

    level_dx = DynamicDisplayable(get1_file)

screen level1_dyn(files, folders):

    drag:
        drag_name "eoe"
        child level_dx
        droppable False




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

    
