init python:
    def detective_dragged(drags, drop):
        if not drop:
            return

        l1_files.remove(drags[0].drag_name)
        if len(l1_files) == 0:
            return True
    

        return False


    class item_location:
        def __init__(self, id, x, y, type):
            self.id = id
            self.x = x
            self.y = y
            self.type = type

init python:
    l1_files = []
    l2_folders = []

    def initLevels():
        global l1_files
        global l2_folders

        File1 = item_location(0, 300,300, "file white.png")
        Folder1 = item_location(0, 200,120, "folder white.png")

        File2 = item_location(1, 300,100, "file t2.png")
        Folder2 = item_location(1, 200,350, "folder t2.png")

        l1_files = [File1, File2]
        l2_folders = [Folder1, Folder2]
        return