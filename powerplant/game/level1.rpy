

screen level1(files, folders):
    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        for i, file in enumerate(files):
            drag:
                
                drag_handle (0, 0, 1.0, 1.0)
                drag_name file
                child file.type
                droppable False
                dragged detective_dragged
                xpos file.x ypos file.y

        #Folders
        for i, folder in enumerate(folders):
                drag:
                    drag_name folder.id
                    child folder.type
                    draggable True
                    xpos folder.x ypos folder.y

      
