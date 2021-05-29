init python:
    Incorrect = 0
    Correct = 1
    Completed = 2

    def detective_dragged(drags, drop):
        if not drop:
            return

        if drags[0].drag_name.item.id != drop.drag_name.item.id:
            return Incorrect

        drags[0].drag_name.item_list.remove(drags[0].drag_name.item)
        return Correct

    class player:
        def __init__(self):
            self.availablePower = 100
            self.meltdownLevel = 0
            self.isLightMode = False
            
    class drag_context:
        def __init__(self, item, item_list):
            self.item = item
            self.item_list = item_list

    class item_location:
        def __init__(self, id, x, y, type):
            self.id = id
            self.x = x
            self.y = y
            self.type = type

init python:
    const_l1_files = []
    const_l1_folders = []

    def initLevels():
        global const_l1_files
        global const_l1_folders

        File1 = item_location(0, 300,300, "file white.png")
        Folder1 = item_location(0, 200,120, "folder white.png")

        File2 = item_location(1, 300,100, "file t2.png")
        Folder2 = item_location(1, 200,350, "folder t2.png")

        const_l1_files = [File1, File2]
        const_l1_folders = [Folder1, Folder2]





        return